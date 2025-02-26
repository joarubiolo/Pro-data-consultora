# Modelo de Base de Datos - Proyecto Google-Yelp

## Descripción General

Este modelo de base de datos ha sido diseñado para almacenar y gestionar información de negocios y reseñas provenientes de **Google Maps** y **Yelp**, permitiendo realizar comparaciones y análisis de sentimiento sobre las opiniones de los clientes.

La base de datos sigue un **modelo de estrella**, donde las tablas principales (`business` y `metadata`) almacenan información de los negocios y se relacionan con otras tablas dimensionales, como `reviews_y`, `reviews_gm`, `categoria` y `ciudades`.

![base](/Imagenes-readme/base_modelada.jpg)

---

## **Estructura y Relaciones**

### **Tablas Principales**
Estas tablas almacenan la información central sobre los negocios:

- **`business`**: Contiene los datos de los negocios obtenidos de **Yelp**.
- **`metadata`**: Contiene los datos de los negocios obtenidos de **Google Maps**.

Ambas tablas tienen atributos similares pero están separadas por decisión del equipo de desarrollo.

*Relación:*  
`business` y `metadata` tienen una **relación 1:N** con sus respectivas reseñas en `reviews_y` y `reviews_gm`.

### **Tablas de Reseñas**
Almacenan las opiniones de los clientes sobre los negocios:

- **`reviews_y`**: Contiene las reseñas de Yelp.
- **`reviews_gm`**: Contiene las reseñas de Google Maps.

Cada reseña está relacionada con un negocio a través del campo `id`.

*Relación:*  
- **1:N** con `business` (Yelp) y `metadata` (Google Maps).
- `review_id` proviene de la fuente original, manteniéndose como `VARCHAR(255)`.

### **Tablas de Categorías**
Manejan la clasificación de los negocios en diferentes categorías:

- **`categoria`**: Contiene la lista de categorías disponibles.
- **`business_categories`**: Relaciona `business` con `categoria`.
- **`metadata_categories`**: Relaciona `metadata` con `categoria`.

*Importancia de las Tablas Intermedias:*  
Las relaciones entre negocios y categorías son de **muchos a muchos (N:M)**, ya que:

- Un negocio puede pertenecer a múltiples categorías (por ejemplo, un restaurante puede ser "Italiana" y "Vegetariana").
- Una categoría puede aplicarse a múltiples negocios (por ejemplo, la categoría "Cafetería" se puede asignar a distintos establecimientos).

Para manejar esta relación, se utilizan **tablas intermedias (`business_categories` y `metadata_categories`)** en lugar de almacenar múltiples valores en una sola columna. Esto evita problemas como:

✔ **Redundancia de datos:** Se evita repetir información innecesariamente.  
✔ **Flexibilidad y escalabilidad:** Se pueden agregar nuevas categorías sin alterar la estructura.  
✔ **Consultas eficientes:** Se pueden realizar búsquedas rápidas mediante `JOINs` optimizados.  

*Relación:*  
- **N:M** entre `business` ↔ `categoria` y `metadata` ↔ `categoria`, gestionadas a través de las tablas intermedias.

---

### **Tabla de Ciudades**
Maneja la información de las ciudades donde se ubican los negocios:

- **`ciudades`**: Contiene información sobre las ciudades.

*Relación:*  
- **1:N** con `business` y `metadata` a través de `city_id`.

---

## **Justificación de Decisiones de Diseño**
**Modelo Estrella**  
El diseño sigue el modelo estrella para facilitar la ejecución de consultas analíticas y optimizar la recuperación de datos.

**Separación de Yelp y Google Maps**  
Se mantienen `business` y `metadata` como tablas separadas por decisión del equipo, asegurando flexibilidad para manejar diferencias entre ambas plataformas.

**Tipos de Datos Específicos**  
- `DOUBLE` se usa en `vader_score` y `textblob_score` para evitar errores de truncamiento.
- `category_id` es `VARCHAR(255)` porque puede contener listas de identificadores.

**Clave Primaria y Relaciones**  
- `review_id` se mantiene como `VARCHAR(255)` porque proviene de la fuente original.
- `id` en `business` y `metadata` actúa como clave primaria y se usa en relaciones foráneas.

---

## **Ejemplo de Relaciones**
- Un negocio en Yelp (`business`) puede tener muchas reseñas en `reviews_y`.
- Un negocio en Google Maps (`metadata`) puede tener muchas reseñas en `reviews_gm`.
- Un negocio puede pertenecer a múltiples categorías mediante `business_categories` o `metadata_categories`.
- Un negocio pertenece a una ciudad definida en `ciudades`.

---

## **Resumen**
Este modelo de base de datos está diseñado para almacenar información de negocios y reseñas de Google Maps y Yelp en una estructura relacional optimizada para análisis de datos. Su diseño en estrella facilita la integración con herramientas de ciencia de datos, asegurando escalabilidad y eficiencia en la consulta de datos.
