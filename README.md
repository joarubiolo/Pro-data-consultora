<p align="center">
  <img src="Imagenes-readme/Pro-data banner.png" alt="banner" width="500">
</p>

# Consultora Pro-Data

## **📋 Índice**

- [**📋 Índice**](#índice)
- [**Integrantes**](#integrantes)
- [**Introducción a Consultora Pro-Data**](#introducción-a-Pro-Data)
- [**Contexto**](#contexto)
- [**🚀 Desarrollo del proyecto**](#desarrollo-del-proyecto)
- [**🌐 Alcance del proyecto**](#alcance-del-proyecto)
- [**🎯Objetivos**](#objetivos)
  - [**🌟 Objetivos Comunes**](#objetivos-comunes)
- [**📊 KPI´s:**](#kpis)
- [**🔧 Flujo de Trabajo**](#flujo-de-trabajo)
  - [1. ETL](#1-etl)
  - [Pipeline](#pipeline)
- [**DashBoard Interactivo** 📊](#dashboard-interactivo-de-restaurantes-en-florida-)
  - [Caracteristicas Principales](#caracteristicas-principales)
  - [Requerimientos del Proyecto:](#requerimientos-del-proyecto)
  - [Ilustración](#ilustración)
- [**Modelo de recomendacion**](#modelo-de-recomendacion)
- [**🔧 Metodología del Trabajo**](#-metodología-del-trabajo)
  - [1. **Sprint 1 - Comprensión del Negocio y de los Datos:**](#1-sprint-1---comprensión-del-negocio-y-de-los-datos)
  - [2. **Sprint 2 - Preparación de los Datos y Modelado:**](#2-sprint-2---preparación-de-los-datos-y-modelado)
- [**Conclusiones**](#conclusiones)


## **Integrantes**

- [Argenis Alexis Bolivar ](https://github.com/Argeboliv05) - *Data Engineer*
- [Ezequiel Lizio](https://github.com/Ezecordoba) - *Data Scientist*
- [Paula Irazoqui](https://github.com/paulairazoqui) - *Data Analist*
- [Joaquín Rubiolo](https://github.com/joarubiolo) - *Data Scientist*
- [Sebastian Prats](https://github.com/sebaprats) - *Data Analist*


## **Stack Tecnologico**

1️⃣ Carga el dataset y elimina valores nulos usando Pandas y Numpy
    📌 ¿Por qué es importante?
    Antes de entrenar cualquier modelo, es fundamental asegurarse de que los datos no contengan valores faltantes. Si hay valores nulos en las reseñas o calificaciones, estos pueden generar errores o sesgos en el modelo.

2️⃣ Convierte texto en características numéricas usando TF-IDF, Word2Vec o BERT
    📌 ¿Por qué es importante?
    Los modelos de Machine Learning no pueden procesar texto directamente. TF-IDF (Term Frequency - Inverse Document Frequency) transforma las palabras en valores numéricos, asignando más peso a términos importantes y reduciendo el peso de palabras comunes.

  🔹 Ejemplo de salida de TF-IDF:
  Si la reseña es "La comida es excelente", el vector numérico podría verse así: [0.12, 0.34, 0.05, ..., 0.67]

3️⃣ Escala los datos numéricos usando StandardScaler
  ¿Por qué es importante?
  Los modelos de Machine Learning funcionan mejor cuando las características numéricas están en la misma escala. StandardScaler convierte todas las variables en valores con media 0 y desviación estándar 1, evitando que una variable con valores grandes domine a otras.

🔹 Ejemplo antes y después de la escala:

Calificación Original	Calificación Escalada
    4.5	                    0.82
    3.0	                    -1.25
    5.0	                    1.35
    🔹 Razón para usar escalado:
    Si tenemos variables en distintas escalas (ej. calificación de 1 a 5 y valores TF-IDF de 0 a 1), el modelo podría dar más peso a las características con valores más grandes.

4️⃣ Entrena y evalúa 4 modelos distintos
  📌 ¿Por qué es importante?
  Cada modelo tiene sus ventajas y desventajas. Probamos 4 enfoques distintos para comparar cuál funciona mejor.

  📌 LogisticRegression:
  Modelo simple basado en probabilidad.
  Útil si los datos son linealmente separables.
  Bueno para interpretabilidad.
  
  📌 DecisionTreeClassifier:
  Divide los datos en ramas de decisiones.
  Bueno para entender la importancia de las características.
  Puede sobreajustarse con datos pequeños.
  
  📌 Random Forest:
  Usa múltiples Árboles de Decisión y hace votación de resultados.
  Reduce el sobreajuste.
  Funciona bien con muchos datos.
  
  📌 XGBoost:
  Algoritmo avanzado basado en boosting (aprendizaje secuencial).
  Optimiza la precisión y reduce errores.
  Es el modelo más poderoso para datos tabulares.

  5️⃣ Compara su rendimiento con accuracy_score y classification_report
  📌 ¿Por qué es importante?
  Nos permite medir qué modelo hace mejores predicciones. Usamos accuracy_score para comparar la precisión general y classification_report para ver métricas más detalladas.

📌 Google Cloud para el despliegue del modelo:

  1️⃣ Costos y comparación con otras plataformas  
  Google Cloud ofrece precios competitivos en comparación con AWS y Azure, especialmente en:  
  - Compute Engine: Máquinas virtuales escalables con precios bajos.  
  - Cloud Run: Para desplegar FastAPI en un entorno sin servidor, con pago solo por uso.  
  - AI Platform: Servicios optimizados para entrenar y servir modelos de ML.   

  2️⃣ Servicios específicos que ofrece Google Cloud para ML
  Google Cloud tiene varias opciones para desplegar el modelo de predicción:  

  | Requerimiento               | Servicio recomendado    | Justificación                                                 |
  |-----------------------------|-------------------------|---------------------------------------------------------------|
  | 'Entrenar el modelo'        | Vertex AI / AI Platform | Plataforma optimizada para ML, con soporte para TensorFlow, Scikit-Learn, XGBoost. |
  | 'Preprocesar datos (ETL)'   | Dataflow / BigQuery     | Manejo eficiente de grandes volúmenes de datos.               |
  | 'Almacenar datos de reviews'| Cloud SQL (PostgreSQL)  | Base de datos gestionada, escalable y compatible con FastAPI. |
  | 'Desplegar API (FastAPI)'   | Cloud Run               | Escalabilidad sin servidor, bajo costo.                       |
  | 'Monitorización del modelo' | AI Platform Predictions | Métricas en tiempo real, detección de degradación del modelo. |

  3️⃣ Rendimiento y escalabilidad
  🔹 Ventajas técnicas de Google Cloud
  - Mejor costo-beneficio en GPUs: Soporte nativo para NVIDIA T4 y A100 con optimización para TensorFlow y PyTorch.  
  - Integración con BigQuery: Permite consultas rápidas sobre grandes volúmenes de datos sin necesidad de ETL manual.  
  - Cloud Run vs AWS Lambda: AWS tiene tiempos de arranque fríos más largos, mientras que Cloud Run mantiene mejor disponibilidad.  
  - Autoescalado nativo: Google Cloud ajusta los recursos dinámicamente según la demanda, reduciendo costos.  

  4️⃣ Seguridad y cumplimiento
  Google Cloud cumple con estándares globales:  
  ✅ ISO 27001, SOC 1/2/3, GDPR, HIPAA, lo que garantiza que los datos de clientes y negocios están protegidos.  

  Además, ofrece:  
  - Cloud Identity & Access Management (IAM) para controlar accesos.  
  - Cifrado de datos en tránsito y en reposo.  
  - Cloud Audit Logs para rastrear actividad y detectar anomalías.  

  📌 Conclusión Final
  🔹 Google Cloud es la opción más económica y ofrece beneficios adicionales:  
  ✅ Menor costo en computación y almacenamiento.  
  ✅ Mejor integración con herramientas de Machine Learning (Vertex AI, BigQuery).  
  ✅ Mayor escalabilidad con Cloud Run y AI Platform.  
  ✅ Alto nivel de seguridad y cumplimiento normativo.  

  📌 Recomendación: Utilizar Cloud Run para la API, AI Platform para el modelo y BigQuery para almacenar datos. Esto reducirá costos y mejorará el rendimiento del sistema. 🚀







Creación de un sistema de analisis de rentabilidad para la instalación de locales gastronómicos en el estado de Florida, Estados Unidos


