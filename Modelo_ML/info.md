# Modelo de Recomendación

El modelo de ML consta de dos redes neuronales que calculan 2 coeficientes distintos. El primero está relacionado con la cantidad de competencia dentro de una misma ciudad y categoría de restaurante. El segundo coeficiente está relacionado con la calidad de esta competencia, y reune información de las calificaciones y las reviews de los restaurantes. Ambos modelos juntos miden cuán recomendable es esa ciudad a la hora de comenzar un restaurante de esa categoría allí. Estos modelos son entrenados en la noteboock `EntrenamientoML.ipynb`. Luego ambos se combinan en un coeficiente $\phi$ que califica a la ciudad como más o menos recomendable para la categoría en cuestión:

$$
\phi = a \cdot P_h + b \cdot P_C
$$

Donde las variables son:

- $P_h = \frac{n_h}{n_R}$, esta variableresulta de un análisis demográfico de la ciudad. 

-  $P_C = \frac{1}{n_R} \sum_{i=0}^{n_R - 1} \frac{1}{P_{r,i}+P_{c,i}}$
  
- $P_{r,i} = \frac{n_{rp,i}}{n_{rn,i}} \cdot n_{r,i}$

  Esta variable surje de un análisis de las reviews de cada restaurante (de la categoría correspondiente) en cada ciudad.

- $P_{c,i} = C_i \cdot n_{r,i}$

  Esta variable surje de un análisis de las calificaciones de cada restaurante (de la categoría correspondiente) en cada ciudad.

- Las constantes $a$ y $b$ son los pesos de cada término en la magnitud final $\phi$. Estan allí para poder darle distintas importancias a las desitintas variables. Se les dio los valores $a=2.5$, $b=1$ para darle mas peso a la cantidad de la competencia y no tanto a la calidad de esta. 

### Definiciones  
 
- $n_h$ : Número de habitantes de la ciudad.
- $n_R$ : Número de restaurantes en la ciudad.
- $n_{rp,i}$ : Número de reseñas positivas del $i$-ésimo restaurante de la ciudad.
- $n_{rn,i}$ : Número de reseñas negativas del $i$-ésimo restaurante de la ciudad.
- $n_{r,i}$ : Número total de reseñas del $i$-ésimo restaurante de la ciudad.
- $C_i$ : Calificación del $i$-ésimo restaurante.

La variable $\frac{1}{P_{r,i}+P_{c,i}}$ sirve para calificar a cada restaurante como excitoso o no. Mientras mas grande, menos excitoso será el restaurante. Luego se hace un promedio sobre todos los restaurantes una misma ciudad para calcular $P_C$ que sirve para calificar a una ciudad según la calidad y las reviews de sos restaurantes. Mientras mas grande $P_C$, peor es la calidad promedio de los restaurantes de la ciudad, por lo que la ciudad es mas recomendable para poner un restaurante allí. 

La variable $P_h$ califica a la ciudad según la cantidad de restaurantes de la categoría seleccionada relativo a la poblacion que tiene. Mientras mas grande $P_h$, menos competencia hay para esa categoría. Por lo que la ciudad será mas recomendable para poner un restaurante allí.

Tanto la variable $P_h$, como $\frac{1}{P_{r,i}+P_{c,i}}$, estan escaladas entre 0 y 1 para que sean comprables entre si.

### Descripcion de los modelos

EL primer modelo `Modelo_P_h.h5` es el que tiene como variables de salída a $P_h$ ya escalado entre 0 y 1. Este tiene como variables de entrada la poblacion de cada ciudad y su número de restaurantes de la categoría en juego. El segundo modelo es `Modelo_P_C.h5`, que tiene como variable de salida $\frac{1}{P_{r,i}+P_{c,i}}$ ya escalado entre 0 y 1 (para cada restaurante) y como variables de entrada el número de reviews positivas, el número de reviews negativas y la calificación del restaurante. En la notebook `EntrenamientoML.ipynb` se puede ver como estan formados y entrenados los modelos.

### Entrenamiento de los modelos

Lo primero que se debe hacer es preparar todos los datos dentro del archivo `metadatos_ML.csv`. Para poder entrenar los modelos se tuvo que agregar datos artificialmente sobre las variables de entrada de cada modelo. Esto se logró haciendo transformaciones no lineales y ruido a los datos originales. Luego se probaron distintos hiperparámetros y se evaluó la eficiencia del modelo con el coeficiente $r^2$. Todo el procedimiento puede verse con mas detenimiento en la noteboock `EntrenamientoML.ipynb`. Los hiperparámetros finales de cada red neuronal y sus respectivos $r^2$ pueden verse en la siguiente tabla 

| Nombre  | numero de capas    | neuronas capa inicial | neuronas capas ocultas | epoch | bach size | optimiado |    $r^2$  |
|:--------|:------------------:|----------------------:|-----------------------:|------:|----------:|----------:|----------:|
| P_h     |          8         |           2           |           256          |  125  |    100    |   adam    |   0.75    |
| P_C     |          8         |           3           |           256          |  125  |    200    |   adam    |   0.87    |

### Descripcion del end point de la API

El end point de la API en `main.py` utiliza el archivo `metadatos_ML.csv` (unificación de los archivos con info de los restaurantes y los de las reviews de estos), que contiene el análisis de sentimiento de las reviews, clasificándolas como reviews buenas o malas. El problema a la hora de armar `metadatos_ML.csv` (ver en `EntrenamientoML.ipynb`) es que no todos los negocios tienen reviews. Por lo que, a la hora de unificar los dataframes de negocios y de reviews, esto dejó entradas vacías en las columnas relacionadas con el número de reviews positivas y negativas. Para corregir esto se buscó la distribución que mejor ajustara las entradas no vacías de las columnas y luego se rellenó los vacíos con valores aleatorios que siguieran estas distribuciones (ver en `EntrenamientoML.ipynb`). 

Con toda esta información, la función del end point calcula, luego de filtrar `metadatos_ML.csv` por una categoría en particular (variable de ingreso por el usuario), las variables $P_h$ para cada ciudad y $\frac{1}{P_{r,i}+P_{c,i}}$ para cada restaurante (usando el modelo respectivo en cada caso). $\frac{1}{P_{r,i}+P_{c,i}}$ sirve para calificar a un restaurant tomando en cuenta su clasificación y el análisis de sus reviews. Con esto, la función puede destacar los mejores restaurantes de la categoría seleccionada y extraer una lista con los atributos más importantes de estos. 

Con esto hecho, la función calcula la variable $P_C = \frac{1}{n_R} \sum_{i=0}^{n_R - 1} \frac{1}{P_{r,i}+P_{c,i}}$, que sirve para calificar a una ciudad según la calidad y las reviews de sos restaurantes, y luego calcula la variable $\phi= a \cdot P_h + b \cdot P_C$, con $a=2.5$ y $b=1$. 

Con esto, la función devuelve una lista de las 3 ciudades mejor calificadas para la categoría seleccionada teniendo en cuenta la competencia y la calidad de esta. Recordemos que una ciudad bien calificada puede significar que tiene poca competencia de para la categoría, o que la calidad de la competencia es baja. Además, a la salida de las función se agrega una lista con los atributos mas importantes que debe tener un restaurant de la categoría seleccionada.
