<p align="center">
  <img src="Imagenes-readme/Pro-data banner.png" alt="banner" width="500">
</p>

# Consultora Pro-Data

## 📋 Índice

- [Integrantes](#integrantes)
- [Entendimiento de la Situación Actual](#entendimiento-de-la-situacion-actual)
- [Objetivo General](#objetivo-general)
- [Objetivos Específicos](#objetivos-especificos)
- [Alcance del Proyecto](#alcance-del-proyecto)
- [KPIs](#kpis)
- [Metodología de Trabajo](#metodologia-de-trabajo)


## **Integrantes**

- [Argenis Alexis Bolivar ](https://github.com/Argeboliv05) - *Scrum Master*
- [Ezequiel Lizio](https://github.com/Ezecordoba) - *ML Engineer*
- [Paula Irazoqui](https://github.com/paulairazoqui) - *Data Engineer*
- [Joaquín Rubiolo](https://github.com/joarubiolo) - *DevOps*
- [Sebastian Prats](https://github.com/sebaprats) - *Data Analyst*


## **Entendimiento de la Situación Actual**

📍 **Contexto:** El sector gastronómico en Florida es altamente competitivo y diverso, con una gran cantidad de negocios en constante apertura y cierre. Sin embargo, no siempre existe una distribución equitativa de los diferentes tipos de restaurantes en cada zona, lo que puede generar oportunidades de mercado sin explotar.

📉 **Problema:** La calidad de los negocios existentes varía significativamente, con algunos establecimientos acumulando malas calificaciones y reviews negativas. Esto representa una oportunidad para nuevos emprendedores que deseen establecer negocios con mejores estándares de servicio y calidad.

💡 **Solución:** Mediante el análisis de datos y técnicas de machine learning, es posible identificar áreas con deficiencia en oferta gastronómica y baja calidad de servicio, proporcionando recomendaciones estratégicas para maximizar el éxito de nuevos negocios.

## **Objetivo General**

Desarrollar un sistema de recomendación que, basado en datos de negocios gastronómicos en el estado de  Florida - EEUU, sugiera la mejor ubicación para abrir un nuevo establecimiento.

## **Objetivos Específicos**

1️⃣ Analizar la distribución geográfica de los negocios gastronómicos en Florida para identificar zonas con baja oferta.
2️⃣ Evaluar la calidad de los negocios existentes mediante análisis de reviews y ratings.
3️⃣ Determinar características clave de los negocios exitosos.
4️⃣ Desarrollar un modelo de recomendación basado en carencias del mercado y calidad de la competencia.
5️⃣ Validar la efectividad del sistema con datos históricos.

## **Alcance del Proyecto**

### **¿Qué vamos a hacer?**

📢 Desarrollar un modelo de Machine Learning que prediga si un negocio tendrá éxito. La recomendación se basará en la carencia de cierto tipo de negocio en una zona y la baja calidad de los existentes según reviews. Además, se proporcionarán características clave de los negocios exitosos.

🔹 **Esto incluye:**

✅ Un **EDA (Exploratory Data Analysis)** completo para entender los datos.
✅ Implementación de un **Data Lake / Data Warehouse** para almacenar y gestionar la base de datos de manera eficiente.
✅ Creación de **features clave** que impactan el éxito de un negocio.
✅ Entrenamiento de un **modelo de clasificación** para predecir éxito o fracaso.
✅ Implementación de un **dashboard interactivo** para visualizar los resultados.
✅ **Despliegue del modelo en la nube** para uso en tiempo real.

### **🏆 Base de Recomendación** 

📢 **Nuestro sistema recomendará ubicaciones para nuevos negocios basándose en los siguientes criterios:**

✅ Se ubica en una **zona con baja oferta gastronómica** o con **competencia de baja calidad** según calificaciones y reviews.
✅ Se alinea con las **características clave de los negocios exitosos**, identificadas en el análisis de datos.
✅ Se encuentra en un área con **potencial de demanda insatisfecha**, determinada por la evaluación de check-ins y reviews.

### **🌍 Alcance Geográfico** 

📢 **Limitamos el análisis a negocios en el Estado Florida de EE.UU.**
🔹 Esto permite trabajar con un dataset más limpio y evitar sesgos por diferencias culturales en reseñas.

### **🕒 Limitación en el Tiempo**

📢 **Nuestro modelo solo se entrenará con datos de los últimos 5 años (2018-2023).**
🔹 Evita incluir negocios antiguos cuyo comportamiento puede no ser representativo.
🔹 Nos aseguramos de que los datos sean recientes y relevantes.

### 🛠️ **Stack Tecnologico**

📢 **Usaremos herramientas estándar para garantizar reproducibilidad:**

✅ **Almacenamiento de Datos**

🔹 Local (CSV, Parquet)
🔹 **Google Cloud Storage** como Data Lake
🔹 **PostgreSQL** como Data Warehouse

✅ **Procesamiento y Análisis**
🔹 **Python (Pandas, NumPy, Scikit-learn)**
🔹 **EDA y Visualización:** Seaborn, Matplotlib
🔹 **ML Models:** Random Forest, XGBoost, Regresión Logística

✅ **Despliegue**
🔹 Dashboard en **PowerBI**
🔹  API en **FastAPI** para consultas en tiempo real

## **KPIs**

### 1️⃣ **Tasa de Crecimiento de Calificaciones (Calificación promedio mensual)**

📢 **Objetivo:** Evaluar la evolución en la satisfacción del público con el rubro elegido.

Este KPI mide el cambio en la calificación promedio de los negocios gastronómicos o de una categoría específica en el último trimestre respecto al anterior.

Calculamos cuánto aumentó o disminuyó la calificación promedio en el último trimestre respecto del anterior, entendiendo que una caída puede ser beneficiosa para un nuevo emprendimiento.

📢 **Fórmula:**

![Texto alternativo](./imagen/KPI_2.png)

📌 **Leyenda:**

* **TCC**: Tasa de Crecimiento de Calificaciones.
* **CP_T**: Calificación promedio en el último trimestre.
* **CP_T-1**: Calificación promedio en el trimestre anterior.

### 2️⃣ **Porcentaje de Negocios Exitosos**

📢 **Objetivo:** Evaluar la probabilidad de éxito de un negocio en determinada zona.

Este KPI mide la cantidad de negocios exitosos, medidos por calificaciones recibidas, en relación con la cantidad de negocios abiertos en el último trimestre.

📢 **Fórmula:**

![Texto alternativo](./imagen/KPI_1.png)

📌 **Leyenda:**

* **PNE**: Porcentaje de Negocios Exitosos.
* **NE**: Número de negocios exitosos.
* **TN**: Total de negocios abiertos en el último trimestre.

### 3️⃣ **Tasa de Saturación del Mercado (Ratio de negocios por habitantes)**

📢 **Objetivo:** Evaluar la cantidad de negocios de determinado rubro en relación con la cantidad de hipotéticos consumidores.

Este KPI mide la cantidad de negocios en una categoría específica en relación con la población de la ubicación en el último trimestre en relación con el anterior,a fin de determinar si hay margen para un nuevo local en la zona.

📢 **Fórmula:**

![Texto alternativo](./imagen/KPI_3.png)

📌 **Leyenda:**

* **RNH**: Ratio de Negocios por Habitante.
* **N**: Número de negocios en una categoría y ciudad.
* **P**: Población total de la ciudad.

## **Metodología de Trabajo**

📢 Para garantizar una gestión eficiente del proyecto, se aplicará la metodología **Scrum**, organizando el trabajo en sprints con entregables claros.

### **👥 Roles del Equipo**

✅ **Scrum Master:** Argenis Bolivar
✅ **Data Engineer:** Paula Irazoqui
✅ **Data Analyst:** Sebastián Prat
✅ **ML Engineer:** Ezequiel Lizio
✅ **DevOps:** Joaquin Rubiolo

### **📌 Roles en cada Sprint**

Para distribuir responsabilidades, los roles clave en cada sprint son:

| **Sprint**   | **Product Owner**                                 | **Scrum Master**                                | **Data Engineer**           | **Data Analyst**             | **ML Engineer**      | **DevOps**                               |
| ------------------ | ------------------------------------------------------- | ----------------------------------------------------- | --------------------------------- | ---------------------------------- | -------------------------- | ---------------------------------------------- |
| **Sprint 1** | Definir objetivos y<br />alcance                        | Gestionar<br />backlog y <br />reuniones              | Extraer y<br />limpiar datos      | Explorar datos<br />y definir KPIs | No aplica aún             | Configurar<br />repositorio Git                |
| **Sprint 2** | Priorizar<br />implementación <br />del ETL            | Asegurar<br />que los <br />procesos se <br />cumplan | Implementar<br />y validar el ETL | Analizar calidad<br />de datos     | No aplica aún             | Configurar<br />infraestructura <br />de datos |
| **Sprint 3** | Priorizar desarrollo<br /> del modelo <br />y dashboard | Coordinar la<br />entrega final                       | Optimizar<br />datos para ML      | Visualizar KPIs<br />y resultados  | Entrenar modelo<br />de ML | Desplegar API<br />y dashboard                 |

#### **1️⃣ Épicas Principales**

1. **Definición del Proyecto y Exploración de Datos**
2. **Implementación del Pipeline ETL y Almacenamiento**
3. **Desarrollo del Modelo de Machine Learning**
4. **Implementación del Dashboard Interactivo**
5. **Optimización y Validación del Sistema**

#### **2️⃣ Historias de Usuario por Sprint**

##### **📌 Sprint 1: Definición y Exploración de Datos (03 Feb - 14 Feb)**

**HU1:** *Como analista de datos, quiero realizar un análisis exploratorio (EDA) para entender la calidad y características de los datos disponibles.*

* **Tareas:**
  ✅ Recopilar datasets de negocios gastronómicos y reviews.
  ✅ Identificar valores nulos, duplicados y outliers.
  ✅ Generar reportes visuales sobre la distribución de datos.

**HU2:** *Como equipo de desarrollo, quiero definir los KPIs para medir el éxito del sistema.*

* **Tareas:**
  ✅ Identificar métricas clave para evaluar recomendaciones del modelo.
  ✅ Documentar fórmulas y criterios de medición.

**HU3:** *Como desarrollador, quiero establecer un repositorio en GitHub para el control de versiones.*

* **Tareas:**
  ✅ Crear la estructura del repositorio.
  ✅ Configurar branches y flujos de trabajo Git.
  ✅ Documentar estándares de codificación y colaboración.

##### **📌 Sprint 2: Data Engineering (17 Feb - 28 Feb)**

**HU4:** *Como ingeniero de datos, quiero implementar un pipeline ETL automatizado para garantizar la limpieza y transformación de los datos.*

* **Tareas:**
  ✅ Diseñar el flujo de extracción, transformación y carga (ETL).
  ✅ Configurar un Data Warehouse / Data Lake.
  ✅ Implementar una carga incremental para nuevos datos.

**HU5:** *Como arquitecto de datos, quiero diseñar un modelo relacional para almacenar la información de manera eficiente.*

* **Tareas:**
  ✅ Crear un modelo de base de datos (ERD).
  ✅ Implementar PostgreSQL o BigQuery para almacenamiento.
  ✅ Validar la integridad de los datos mediante consultas SQL.

**HU6:** *Como ingeniero de datos, quiero realizar pruebas de calidad para asegurar que los datos son confiables.*

* **Tareas:**
  ✅ Implementar validaciones de datos en Airflow o Prefect.
  ✅ Generar reportes de calidad de datos.
  ✅ Resolver problemas de datos faltantes o inconsistentes.

##### **📌 Sprint 3: Data Analytics + ML (3 Mar - 15 Mar)**

**HU7:** *Como analista de datos, quiero visualizar las recomendaciones del modelo en un dashboard interactivo.*

* **Tareas:**
  ✅ Implementar gráficos de visualización de KPIs.
  ✅ Integrar el dashboard con la base de datos.
  ✅ Generar filtros interactivos para el análisis de datos.

**HU8:** *Como desarrollador de machine learning, quiero entrenar un modelo de recomendación basado en datos históricos.*

* **Tareas:**
  ✅ Seleccionar el algoritmo de ML más adecuado (clustering, regresión, etc.).
  ✅ Optimizar el modelo con hiperparámetros.
  ✅ Evaluar su rendimiento con métricas de precisión y recall.

**HU9:** *Como DevOps, quiero desplegar el modelo en producción para que pueda ser utilizado en tiempo real.*

* **Tareas:**
  ✅ Crear API con **FastAPI** para consumir el modelo.
  ✅ Integrar el modelo con el dashboard para visualización en tiempo real.
  ✅ Probar la API con datos de prueba y optimizar tiempos de respuesta.

---

#### **3️⃣ Backlog Técnico (Tareas Prioritarias)**

✅ **Sprint 1: Definición y Exploración de Datos**

* Configurar repositorio en **GitHub** con estructura de carpetas.
* Realizar EDA.
* Documentar las fuentes de datos y su confiabilidad.

🏆 **Hitos:**

* Documentación del EDA y calidad de datos.
* Definición de KPIs.
* Creación del repositorio en GitHub.

✅ **Sprint 2: Data Engineering**

* Configurar **Airflow** o **Prefect** para orquestación del ETL.
* Implementar almacenamiento en  **Google BigQuery** .
* Generar logs de procesamiento y validación de datos.

🏆 **Hitos:**

* Implementación del Data Lake y Data Warehouse.
* Pipeline ETL en funcionamiento.
* Validación de datos y reportes de calidad.

✅ **Sprint 3: Data Analytics + ML**

* Conectar el dashboard con la base de datos.
* Entrenar y desplegar el modelo de Machine Learning.
* Evaluar el sistema con datos en tiempo real.

🏆 **Hitos:**

* Dashboard funcional con visualización de KPIs.
* Modelo de ML entrenado y optimizado.
* Despliegue del modelo en la nube.

#### 4️⃣ Diagrama de Gantt

![Texto alternativo](./imagen/GanttProyecto.png)










## **Stack Tecnologico**

📌 Librerias para el ETL y EDACarga el dataset y elimina valores nulos usando Pandas y Numpy

1️⃣ Antes de entrenar cualquier modelo, es fundamental asegurarse de que los datos no contengan valores faltantes. Si hay valores nulos en las reseñas o calificaciones, estos pueden generar errores o sesgos en el modelo.

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


