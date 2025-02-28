# Modelo de Recomendación

El modelo de ML conta de una red neuronal. Tiene como variable de ingreso una categoría dentro del archivo `categories_normalized.csv` y una ciudad dentro de `ciudades_normal.csv`. La variable de salida es un a serie con valores numéricos que sirven como calificación para cada ciudad. Esta calificación mide cuán recomendable es esa ciudad a la hora de comenzar un restaurante de esa categoría allí. La ecuación que describe la calificacion $\phi$ que le da el modelo a cada ciudad es la siguiente:

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

- La función $f$ es una conjunción de función que escalan las variables $P_h$, $\frac{1}{P_c}$ y $\frac{1}{P_r}$ entre 0 y 1 para que puedan ser comparables entre si.
- Las constantes $a$, $b$ y $c$ son los pesos de cada término en la magnitud final $\phi$. Estan allí para poder darle distintas importancias a las desitintas variables. 

### Definiciones

- $n_h$ : Número de habitantes de la ciudad.
- $n_R$ : Número de restaurantes en la ciudad.
- $n_{rp,i}$ : Número de reseñas positivas del $i$-ésimo restaurante de la ciudad.
- $n_{rn,i}$ : Número de reseñas negativas del $i$-ésimo restaurante de la ciudad.
- $n_{r,i}$ : Número total de reseñas del $i$-ésimo restaurante de la ciudad.
- $C_i$ : Calificación del $i$-ésimo restaurante.
