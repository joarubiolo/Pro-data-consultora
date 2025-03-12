# Modelo de Recomendación

El modelo de ML consta de una red neuronal. Tiene como variable de ingreso una categoría dentro del archivo `categories_normalized.csv` y una ciudad dentro de `ciudades_normal.csv`. La variable de salida es un a serie con valores numéricos que sirven como calificación para cada ciudad. Esta calificación mide cuán recomendable es esa ciudad a la hora de comenzar un restaurante de esa categoría allí. Este modelo es entrenado en la noteboock `EntrenamientoML.ipynb`. La ecuación que describe la calificacion $\phi$ que le da el modelo a cada ciudad es la siguiente:

$$
\phi = a \cdot f(P_h) + b \cdot f\left(\frac{1}{P_c}\right) + c \cdot f\left(\frac{1}{P_r}\right)
$$

Donde las variables son:

- $P_h = \frac{n_h}{n_R}$, esta variableresulta de un análisis demográfico de la ciudad. 

- $P_r = \frac{1}{n_R} \sum_{i=0}^{n_R - 1} P_{r,i}$
  
  $P_{r,i} = \frac{n_{rp,i}}{n_{rn,i}} \cdot n_{r,i}$

  Esta variable surje de un análisis de las reviews de cada restaurante (de la categoría correspondiente) en cada ciudad.

- $P_c = \frac{1}{n_R} \sum_{i=0}^{n_R - 1} P_{c,i}$
  
  $P_{c,i} = C_i \cdot n_{r,i}$

  Esta variable surje de un análisis de las calificaciones de cada restaurante (de la categoría correspondiente) en cada ciudad.

- La función $f$ es una conjunción de función que escalan las variables $P_h$ , $\frac{1}{P_c}$ y $\frac{1}{P_r}$ entre 0 y 1 para que puedan ser comparables entre si.
- Las constantes $a$, $b$ y $c$ son los pesos de cada término en la magnitud final $\phi$. Estan allí para poder darle distintas importancias a las desitintas variables. En principio de le dio los valores $a=1$, $b=2$ y $c=2.5$ para darle mas peso a la calidad de la competencia y no tanto a la cantidad.

El cálculo de las variables $P_r$ y $P_c$ es un promedio ponderado con el número de reviews para dale mas peso a los restaurantes con mas reviews. 

### Definiciones  
 
- $n_h$ : Número de habitantes de la ciudad.
- $n_R$ : Número de restaurantes en la ciudad.
- $n_{rp,i}$ : Número de reseñas positivas del $i$-ésimo restaurante de la ciudad.
- $n_{rn,i}$ : Número de reseñas negativas del $i$-ésimo restaurante de la ciudad.
- $n_{r,i}$ : Número total de reseñas del $i$-ésimo restaurante de la ciudad.
- $C_i$ : Calificación del $i$-ésimo restaurante.

### Descripcion del end point de la API

El end point de la API en `main.py` utiliza el archivo `metadatos_ML.csv` (unificación de los archivos con info de los restaurantes y los de las reviews de estos), que contiene el análisis de sentimiento de las reviews, clasificándolas como reviews buenas o malas. El problema a la hora de armar `metadatos_ML.csv` (ver en `EntrenamientoML.ipynb`) es que no todos los negocios tienen reviews. Por lo que, a la hora de unificar los dataframes de negocios y de reviews, esto dejó entradas vacías en las columnas relacionadas con el número de reviews positivas y negativas. Para corregir esto se buscó la distribución que mejor ajustara las entradas no vacías de las columnas y luego se rellenó los vacíos con valores aleatorios que siguieran estas distribuciones (ver en `EntrenamientoML.ipynb`). 

Con toda esta información, la función del end point calcula, luego de filtrar `metadatos_ML.csv` por una categoría en particular (variable de ingreso por el usuario), las variables $P_{r,i}$ y $P_{c,i}$ y las escala para que sean comprables. Con estas calcula, también, una variable $\gamma=d \cdot P_{r,i}+e \cdot P_{c,i}$ ( $d=1$ y $e=c/b=1.25$ ) que sirve para calificar a un restaurant tomando en cuenta su clasificación y el análisis de sus reviews. Con esto, la función puede destacar los mejores restoranes de esa categoría y extraer una lista con los atributos más importantes de estos. 

Con esto hecho, la función utiliza el modelo entrenado `Modelo_entrenado.h5` para calcular la variable $\phi$ y dar una lista de las ciudades mejor calificadas teniendo en cuenta la competencia y la calidad de esta se quisiera poner un nuevo restaurant allí dentro de la categoría ingresada. 

Las variables de salida de las función son una lista con los atributos mas importantes que debe tener un restaurant de la categoría seleccionada y las 3 ciudades mas recomendadas para poner un restaurant allí. 

 
