# Modelo de Recomendación

La ecuación que describe el modelo es la siguiente:

$$
\phi = a \cdot f(P_h) + b \cdot f\left(\frac{1}{P_c}\right) + c \cdot f\left(\frac{1}{P_r}\right)
$$

Donde:

- $P_h = \frac{n_h}{n_R}$

- $P_r = \frac{1}{n_R} \sum_{i=0}^{n_R - 1} P_{r,i}$

\[
P_{r,i} = \frac{n_{rp,i}}{n_{rn,i}} \cdot n_{r,i}
\]

- \( P_c = \frac{1}{n_R} \sum_{i=0}^{n_R - 1} P_{c,i} \)

\[
P_{c,i} = C_i \cdot n_{r,i}
\]

### Definiciones

- \( n_h \): Número de habitantes de la ciudad.
- \( n_R \): Número de restaurantes en la ciudad.
- \( n_{rp,i} \): Número de reseñas positivas del \( i \)-ésimo restaurante de la ciudad.
- \( n_{rn,i} \): Número de reseñas negativas del \( i \)-ésimo restaurante de la ciudad.
- \( n_{r,i} \): Número total de reseñas del \( i \)-ésimo restaurante de la ciudad.
- \( C_i \): Calificación del \( i \)-ésimo restaurante.
