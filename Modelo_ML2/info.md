# Documentación del Proyecto de Recomendación de Negocios

## Descripción General

Este proyecto implementa un sistema de recomendación de negocios basado en Machine Learning utilizando Streamlit como interfaz de usuario. El modelo de aprendizaje automático analiza datos de diferentes ciudades y categorías de negocios, evaluando factores como competencia y puntuaciones de reseñas para sugerir las mejores opciones de negocio.

## Tecnologías Utilizadas

* **Python** : Lenguaje de programación principal.
* **Streamlit** : Para la interfaz de usuario interactiva.
* **Pandas** : Para la manipulación y análisis de datos.
* **XGBoost** : Algoritmo de aprendizaje automático para la clasificación.
* **Joblib** : Para la serialización y carga del modelo entrenado.

## Estructura del Proyecto

El proyecto incluye los siguientes archivos clave:

1. **app.py** : Script principal que maneja la interfaz en Streamlit y la lógica de predicción.
2. **ciudad_categoria_procesado.csv** : Conjunto de datos con información de las ciudades y categorías de negocios.
3. **modelo_xgb_1.pkl** : Modelo de aprendizaje entrenado y guardado en formato pickle.
4. **requirements.txt** : Lista de dependencias necesarias para ejecutar el proyecto.
5. **ML_modelo.ipynb** : Cuaderno de Jupyter donde se encuentra el proceso de entrenamiento del modelo.

## Instalación y Configuración

Para ejecutar este proyecto en un entorno local, sigue estos pasos:

1. Clona el repositorio o descarga los archivos necesarios.
2. Instala las dependencias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación en Streamlit:
   ```bash
   streamlit run app.py
   ```

## Funcionamiento

La aplicación permite a los usuarios ingresar el nombre de una ciudad y recibir recomendaciones sobre las categorías de negocio con menor competencia o mejores oportunidades.

* Se carga el modelo de Machine Learning desde `modelo_xgb_1.pkl`.
* Se procesa la información de la ciudad seleccionada.
* Se genera una predicción basada en las características del dataset.
* Se muestran las categorías recomendadas en la interfaz de Streamlit.

## Características del Dataset

El dataset contiene información relevante sobre cada ciudad y las categorías de negocio. A continuación, se describen los atributos utilizados en el modelo:

1. **`city`** *(string)*
   * Nombre de la ciudad en la que se evaluarán las oportunidades de negocio.
2. **`category`** *(string)*
   * Categoría del negocio (Ej: Restaurantes, Tiendas de Ropa, Cafeterías, etc.).
3. **`competencia`** *(numérico - continuo)*
   * Cantidad de negocios existentes en la ciudad para una categoría específica.
   * **Interpretación** : Un valor alto indica que la categoría está saturada en esa ciudad, mientras que un valor bajo sugiere menos competencia.
4. **`avg_rating`** *(numérico - continuo, rango: 1 a 5)*
   * Calificación promedio de los negocios en esa categoría dentro de la ciudad, basada en reseñas de usuarios.
   * **Interpretación** : Un valor alto indica que los negocios existentes tienen buenas valoraciones, lo que puede significar alta calidad o satisfacción del cliente.
5. **`avg_vader_score`** *(numérico - continuo, rango: -1 a 1)*
   * Puntuación de sentimiento calculada con **VADER** (Análisis de Sentimiento basado en Regla Lexical).
   * **Interpretación** :
   * **Valores negativos** (cercanos a -1) → Sentimiento negativo en reseñas.
   * **Valores positivos** (cercanos a 1) → Sentimiento positivo en reseñas.
   * **Valores cercanos a 0** → Opiniones neutrales.
6. **`avg_textblob_score`** *(numérico - continuo, rango: -1 a 1)*
   * Puntuación de sentimiento calculada con **TextBlob** (Modelo Estadístico de Análisis de Sentimiento).
   * **Interpretación** : Similar al `avg_vader_score`, ayuda a validar la tendencia del sentimiento de las reseñas.
7. **`poblacion`** *(numérico - entero)*
   * Número de habitantes de la ciudad.
   * **Interpretación** : Ciudades con mayor población pueden tener mayor demanda de ciertos negocios, mientras que ciudades pequeñas pueden representar mercados más nicho.

### **Variable Objetivo (Target)**

* **`recomendado`** *(binario: 0 o 1)*
  * Indica si la categoría de negocio en la ciudad es recomendada (1) o no (0).
  * **Criterios utilizados por el modelo para recomendar una categoría:**
    * Baja competencia.
    * Buenas calificaciones en reseñas.
    * Opiniones positivas (según análisis de sentimiento).
    * Ciudad con suficiente población para sostener el negocio.

## Desarrollo y Entrenamiento del Modelo

El modelo XGBoost fue entrenado utilizando datos que incluyen:

* Nivel de competencia por categoría.
* Puntuaciones promedio de las reseñas (sentimientos y valoraciones numéricas).
* Población de la ciudad.

El código de entrenamiento se encuentra en `ML_modelo.ipynb`, donde se realizan las transformaciones necesarias y la evaluación del modelo.

## Futuras Mejoras

* Integrar bases de datos en la nube para actualizar en tiempo real los datos de negocios.
* Optimizar el modelo incluyendo nuevas variables para mejorar la precisión.
* Implementar una versión web más avanzada con dashboards interactivos.
