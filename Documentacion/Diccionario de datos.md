# Diccionario de Datos  

## Introducción  

### Descripción General  
Este documento contiene el diccionario de datos del dataset utilizado en el análisis de negocios en Florida, con información proveniente de dos fuentes principales: **Google Maps** y **Yelp**.  

El dataset incluye información sobre los negocios, sus características, su ubicación geográfica, las categorías a las que pertenecen y las reseñas de los usuarios. La estructura de los datos ha sido optimizada mediante procesos de **normalización, consolidación y estandarización**, lo que permite un análisis más eficiente y preciso.  

### Objetivo del Diccionario de Datos  
El propósito de este documento es proporcionar una descripción detallada de cada tabla y sus columnas, permitiendo a cualquier usuario (científicos de datos, analistas, stakeholders del negocio) comprender la estructura de los datos, su significado y cómo pueden ser utilizados en distintos análisis.  

### Estructura del Dataset  
El dataset se compone de **ocho tablas**, organizadas de la siguiente manera:  

#### **Tablas Principales**  
1. **`business`**: Contiene información sobre los negocios extraídos de **Yelp**, incluyendo su ubicación, características y calificaciones.  
2. **`metadata`**: Contiene información sobre los negocios extraídos de **Google Maps**, con detalles similares a los de la tabla `business`.  

#### **Tablas Relacionales**  
3. **`business_categories`**: Relaciona cada negocio con una o más categorías en **Yelp**.  
4. **`business_categories_gm`**: Relaciona cada negocio con una o más categorías en **Google Maps**.  

#### **Tablas de Reseñas**  
5. **`reviews_y`**: Contiene las reseñas de los negocios en **Yelp**, con calificaciones, fecha y análisis de sentimiento.  
6. **`reviews_gm`**: Contiene las reseñas de los negocios en **Google Maps**, con el mismo tipo de información que la tabla anterior.  

#### **Tablas de Referencia**  
7. **`ciudades`**: Contiene información sobre las ciudades de Florida, incluyendo su identificación única y población.  
8. **`categorias`**: Contiene la lista normalizada de categorías utilizadas para clasificar los negocios.  

### Procesos de Normalización  
Dado que los datos provienen de múltiples fuentes con estructuras diferentes, se realizaron las siguientes transformaciones para estandarizar la información:  

- **Reducción de la granularidad en categorías**: Se agruparon categorías similares en un conjunto más manejable y coherente.  
- **Estandarización de nombres de ciudades**: Se agruparon nombres alternativos, suburbios y variaciones tipográficas bajo una única ciudad normalizada.  
- **Tablas intermedias para relaciones muchos a muchos**: Se crearon tablas de relaciones entre negocios y categorías para mejorar la estructura de los datos.  

### Alcance y Uso  
Este diccionario de datos está diseñado para:  
- Servir como referencia para la interpretación y manipulación de los datos.  
- Facilitar la integración de nuevas fuentes de información.  
- Proveer una estructura clara para análisis de tendencias, recomendaciones y segmentación de negocios.  

---

## Diccionario de Datos - Tabla `business`

### Descripción
La tabla `business` contiene información detallada sobre los negocios registrados en la base de datos de Yelp, incluyendo su ubicación, clasificación, características y categorías asociadas.

### Estructura de la Tabla

| Nombre de la columna     | Tipo de dato  | Descripción |
|--------------------------|--------------|-------------|
| `id`                    | `object`      | Identificador único del negocio. |
| `name`                  | `object`      | Nombre del negocio. |
| `postal_code`           | `float64`     | Código postal de la ubicación del negocio. |
| `latitude`              | `float64`     | Latitud de la ubicación del negocio. |
| `longitude`             | `float64`     | Longitud de la ubicación del negocio. |
| `city_id`               | `int64`       | Identificador de la ciudad donde se encuentra el negocio. |
| `category_id`           | `object`      | Identificadores de las categorías asociadas al negocio (puede contener múltiples valores en formato de lista). |
| `stars`                 | `float64`     | Calificación promedio del negocio en Yelp (escala de 1 a 5 estrellas). |
| `review_count`          | `int64`       | Cantidad de reseñas que ha recibido el negocio. |
| `address`               | `object`      | Dirección del negocio. |
| `is_open`               | `int64`       | Indica si el negocio está abierto (`1`) o cerrado (`0`). |
| `delivery`              | `int64`       | Indica si el negocio ofrece servicio de entrega (`1` sí, `0` no). |
| `takeout`               | `int64`       | Indica si el negocio permite pedidos para llevar (`1` sí, `0` no). |
| `outdoor_seating`       | `int64`       | Indica si el negocio tiene asientos al aire libre (`1` sí, `0` no). |
| `drivethrough`          | `int64`       | Indica si el negocio tiene servicio de auto (`1` sí, `0` no). |
| `wheelchair_friendly`   | `int64`       | Indica si el negocio es accesible para sillas de ruedas (`1` sí, `0` no). |
| `alcohol_beverage`      | `int64`       | Indica si el negocio vende alcohol (`1` sí, `0` no). |
| `dancing`              | `int64`       | Indica si el negocio tiene pista de baile o permite bailar (`1` sí, `0` no). |
| `catering`             | `int64`       | Indica si el negocio ofrece servicio de catering (`1` sí, `0` no). |
| `counter_service`      | `int64`       | Indica si el negocio funciona con servicio de mostrador (`1` sí, `0` no). |
| `seating`             | `int64`       | Indica si el negocio tiene área de asientos (`1` sí, `0` no). |
| `dogs_allowed`        | `int64`       | Indica si el negocio permite perros (`1` sí, `0` no). |
| `bike_parking`        | `int64`       | Indica si el negocio tiene estacionamiento para bicicletas (`1` sí, `0` no). |
| `parking`            | `int64`       | Indica si el negocio ofrece estacionamiento (`1` sí, `0` no). |
| `breakfast`          | `int64`       | Indica si el negocio sirve desayuno (`1` sí, `0` no). |
| `lunch`              | `int64`       | Indica si el negocio sirve almuerzo (`1` sí, `0` no). |
| `dinner`             | `int64`       | Indica si el negocio sirve cena (`1` sí, `0` no). |
| `dessert`            | `int64`       | Indica si el negocio ofrece postres (`1` sí, `0` no). |
| `casual`             | `int64`       | Indica si el negocio tiene un ambiente informal (`1` sí, `0` no). |
| `romantic`           | `int64`       | Indica si el negocio tiene un ambiente romántico (`1` sí, `0` no). |
| `formal`             | `int64`       | Indica si el negocio tiene un ambiente formal (`1` sí, `0` no). |
| `trendy`             | `int64`       | Indica si el negocio tiene un ambiente moderno o de tendencia (`1` sí, `0` no). |
| `with_reservation`   | `int64`       | Indica si el negocio permite hacer reservas (`1` sí, `0` no). |
| `live_entertainment` | `int64`       | Indica si el negocio ofrece entretenimiento en vivo (`1` sí, `0` no). |
| `groups`             | `int64`       | Indica si el negocio es adecuado para grupos grandes (`1` sí, `0` no). |
| `kids_friendly`      | `int64`       | Indica si el negocio es apto para niños (`1` sí, `0` no). |
| `wifi`               | `int64`       | Indica si el negocio ofrece conexión WiFi (`1` sí, `0` no). |
| `bar_onsite`         | `int64`       | Indica si el negocio tiene bar propio (`1` sí, `0` no). |
| `credit_cards`       | `int64`       | Indica si el negocio acepta pagos con tarjeta de crédito (`1` sí, `0` no). |

### Notas Adicionales
- La columna `category_id` almacena los identificadores de las categorías asociadas al negocio en formato de lista, lo que indica que un negocio puede pertenecer a múltiples categorías.
- Las columnas de tipo `int64` con valores `1` o `0` representan características binarias del negocio (presente o no presente).
- La columna `postal_code` tiene algunos valores nulos, lo que podría requerir limpieza o imputación si se usa en análisis espaciales.

---

## Diccionario de Datos - Tabla `metadata`

### Descripción
La tabla `metadata` contiene información detallada sobre negocios provenientes de Google Maps, incluyendo su ubicación, características, clasificación y categorías asociadas.

### Estructura de la Tabla

| Nombre de la columna           | Tipo de dato  | Descripción |
|--------------------------------|--------------|-------------|
| `id`                           | `object`      | Identificador único del negocio. |
| `name`                         | `object`      | Nombre del negocio. |
| `street_address`               | `object`      | Dirección del negocio. |
| `postal_code`                  | `int64`       | Código postal de la ubicación del negocio. |
| `latitude`                     | `float64`     | Latitud de la ubicación del negocio. |
| `longitude`                    | `float64`     | Longitud de la ubicación del negocio. |
| `city_id`                      | `int64`       | Identificador de la ciudad donde se encuentra el negocio. |
| `category_id`                  | `object`      | Identificadores de las categorías asociadas al negocio (puede contener múltiples valores en formato de lista). |
| `stars`                        | `float64`     | Calificación promedio del negocio en Google Maps (escala de 1 a 5 estrellas). |
| `review_count`                 | `int64`       | Cantidad de reseñas recibidas por el negocio. |
| `is_open`                      | `int64`       | Indica si el negocio está abierto (`1`) o cerrado (`0`). |
| `delivery`                     | `int64`       | Indica si el negocio ofrece servicio de entrega (`1` sí, `0` no). |
| `takeout`                      | `int64`       | Indica si el negocio permite pedidos para llevar (`1` sí, `0` no). |
| `dinein`                       | `int64`       | Indica si el negocio permite comer en el lugar (`1` sí, `0` no). |
| `outdoor_seating`              | `int64`       | Indica si el negocio tiene asientos al aire libre (`1` sí, `0` no). |
| `drivethrough`                 | `int64`       | Indica si el negocio tiene servicio de auto (`1` sí, `0` no). |
| `good_for_working_on_laptop`   | `int64`       | Indica si el negocio es adecuado para trabajar con una laptop (`1` sí, `0` no). |
| `solo_dining`                  | `int64`       | Indica si el negocio es adecuado para comer solo (`1` sí, `0` no). |
| `wheelchair_friendly`          | `int64`       | Indica si el negocio es accesible para sillas de ruedas (`1` sí, `0` no). |
| `alcohol_beverage`             | `int64`       | Indica si el negocio vende alcohol (`1` sí, `0` no). |
| `healthy_food`                 | `int64`       | Indica si el negocio ofrece opciones de comida saludable (`1` sí, `0` no). |
| `fast_comfort_food`            | `int64`       | Indica si el negocio ofrece comida rápida o de confort (`1` sí, `0` no). |
| `braille_menu`                 | `int64`       | Indica si el negocio tiene menú en braille (`1` sí, `0` no). |
| `all_you_can_eat`              | `int64`       | Indica si el negocio ofrece servicio de buffet (`1` sí, `0` no). |
| `coffee`                       | `int64`       | Indica si el negocio ofrece café como producto principal (`1` sí, `0` no). |
| `dancing`                      | `int64`       | Indica si el negocio tiene pista de baile o permite bailar (`1` sí, `0` no). |
| `catering`                     | `int64`       | Indica si el negocio ofrece servicio de catering (`1` sí, `0` no). |
| `counter_service`              | `int64`       | Indica si el negocio funciona con servicio de mostrador (`1` sí, `0` no). |
| `pay_ahead`                    | `int64`       | Indica si el negocio permite pagar por adelantado (`1` sí, `0` no). |
| `seating`                      | `int64`       | Indica si el negocio tiene área de asientos (`1` sí, `0` no). |
| `breakfast`                    | `int64`       | Indica si el negocio sirve desayuno (`1` sí, `0` no). |
| `lunch`                        | `int64`       | Indica si el negocio sirve almuerzo (`1` sí, `0` no). |
| `dinner`                       | `int64`       | Indica si el negocio sirve cena (`1` sí, `0` no). |
| `dessert`                      | `int64`       | Indica si el negocio ofrece postres (`1` sí, `0` no). |
| `casual`                       | `int64`       | Indica si el negocio tiene un ambiente informal (`1` sí, `0` no). |
| `romantic`                     | `int64`       | Indica si el negocio tiene un ambiente romántico (`1` sí, `0` no). |
| `formal`                       | `int64`       | Indica si el negocio tiene un ambiente formal (`1` sí, `0` no). |
| `trendy`                       | `int64`       | Indica si el negocio tiene un ambiente moderno o de tendencia (`1` sí, `0` no). |
| `with_reservation`             | `int64`       | Indica si el negocio permite hacer reservas (`1` sí, `0` no). |
| `usually_a_wait`               | `int64`       | Indica si el negocio suele tener tiempo de espera alto (`1` sí, `0` no). |
| `quick_visit`                  | `int64`       | Indica si el negocio es ideal para visitas rápidas (`1` sí, `0` no). |
| `black_owned`                  | `int64`       | Indica si el negocio es propiedad de una persona afroamericana (`1` sí, `0` no). |
| `women_led`                    | `int64`       | Indica si el negocio es dirigido por una mujer (`1` sí, `0` no). |
| `veteran_led`                  | `int64`       | Indica si el negocio es dirigido por un veterano (`1` sí, `0` no). |
| `entertainment`                | `int64`       | Indica si el negocio ofrece actividades de entretenimiento (`1` sí, `0` no). |
| `live_entertainment`           | `int64`       | Indica si el negocio tiene entretenimiento en vivo (`1` sí, `0` no). |
| `lgbtq_friendly`               | `int64`       | Indica si el negocio es amigable con la comunidad LGBTQ+ (`1` sí, `0` no). |
| `fast_service`                 | `int64`       | Indica si el negocio es conocido por su servicio rápido (`1` sí, `0` no). |
| `fireplace`                    | `int64`       | Indica si el negocio tiene chimenea (`1` sí, `0` no). |
| `rooftop_seating`              | `int64`       | Indica si el negocio tiene asientos en la azotea (`1` sí, `0` no). |
| `sports`                       | `int64`       | Indica si el negocio transmite eventos deportivos (`1` sí, `0` no). |
| `college_students`             | `int64`       | Indica si el negocio es popular entre estudiantes universitarios (`1` sí, `0` no). |
| `family_friendly`              | `int64`       | Indica si el negocio es apto para familias (`1` sí, `0` no). |
| `locals`                       | `int64`       | Indica si el negocio es frecuentado por locales (`1` sí, `0` no). |
| `tourists`                     | `int64`       | Indica si el negocio es popular entre turistas (`1` sí, `0` no). |
| `cash_only`                    | `int64`       | Indica si el negocio solo acepta efectivo (`1` sí, `0` no). |
| `credit_cards`                 | `int64`       | Indica si el negocio acepta tarjetas de crédito (`1` sí, `0` no). |
| `nfc_mobile_payments`          | `int64`       | Indica si el negocio acepta pagos móviles NFC (`1` sí, `0` no). |
| `recycling`                    | `int64`       | Indica si el negocio tiene políticas de reciclaje (`1` sí, `0` no). |

---

## Diccionario de Datos - Tabla `ciudades`

### Descripción
La tabla `ciudades` contiene información sobre las ciudades del estado de Florida, incluyendo su identificador único, nombre y población. Esta tabla permite estandarizar la ubicación geográfica de los negocios en otras tablas a través de la clave `city_id`.

### Estructura de la Tabla

| Nombre de la columna  | Tipo de dato  | Descripción |
|----------------------|--------------|-------------|
| `city_id`           | `int64`       | Identificador único de la ciudad. Se usa como clave foránea en otras tablas para asociar negocios con su ubicación geográfica. |
| `city`              | `object`      | Nombre de la ciudad tal como aparece en los registros de la fuente de datos. |
| `population`        | `int64`       | Población total de la ciudad, según los datos disponibles en la fuente de información. |
| `city_normalized`   | `object`      | Nombre de la ciudad en un formato estandarizado. Este campo permite corregir inconsistencias en los nombres de ciudades provenientes de distintas fuentes. |

### Notas Adicionales
- La columna `city_id` es clave primaria en esta tabla y se utiliza en otras tablas como referencia a la ubicación de los negocios.  
- `city_normalized` se usa para unificar nombres de ciudades que pueden aparecer con diferentes formatos o abreviaciones en otras fuentes de datos.  
- `population` permite realizar análisis en función del tamaño de la ciudad, como la densidad de negocios por cantidad de habitantes.  

---

## Diccionario de Datos - Tabla `categorias`

### Descripción
La tabla `categorias` contiene la lista de categorías de negocios en un formato normalizado. Cada categoría está identificada por un código único (`category_id`), lo que permite estandarizar la clasificación de los negocios en otras tablas.

### Estructura de la Tabla

| Nombre de la columna  | Tipo de dato  | Descripción |
|----------------------|--------------|-------------|
| `category_id`       | `int64`       | Identificador único de la categoría. Se usa como clave foránea en otras tablas para clasificar los negocios según su tipo de servicio o producto. |
| `category`          | `object`      | Nombre de la categoría en formato normalizado, agrupando negocios de características similares. |

### Notas Adicionales
- La columna `category_id` es clave primaria en esta tabla y se usa en otras tablas para asignar categorías a cada negocio.  
- `category` contiene la versión estandarizada de las categorías, lo que evita problemas de duplicados, errores ortográficos o nombres inconsistentes en los datos originales.  
- La asignación de negocios a categorías puede incluir agrupaciones de categorías más específicas dentro de grandes grupos (estos detalles se especificarán en la sección de **agrupaciones de categorías** al final del diccionario de datos).  

---

## Diccionario de Datos - Tabla `reviews_gm`

### Descripción
La tabla `reviews_gm` contiene información sobre las reseñas de negocios extraídas de la base de datos de Google Maps. Cada reseña está vinculada a un negocio a través del identificador `id` y contiene datos sobre la calificación dada por el usuario, la presencia de texto en la reseña, su fecha y dos análisis de sentimientos aplicados al contenido de la reseña.

### Estructura de la Tabla

| Nombre de la columna  | Tipo de dato  | Descripción |
|----------------------|--------------|-------------|
| `id`                | `object`      | Identificador único del negocio al que pertenece la reseña. Se relaciona con la tabla `metadata`. |
| `rating`            | `int64`       | Calificación otorgada por el usuario en una escala de 1 a 5 estrellas. |
| `has_text`          | `int64`       | Indica si la reseña contiene texto (`1` sí, `0` no). |
| `vader_score`       | `float64`     | Puntuación de sentimiento de la reseña calculada con el modelo VADER (oscila entre -1 y 1, donde valores positivos indican sentimientos positivos y valores negativos indican sentimientos negativos). |
| `textblob_score`    | `float64`     | Puntuación de sentimiento calculada con el modelo TextBlob (valores entre -1 y 1, similar a VADER pero con una metodología diferente). |
| `date`              | `object`      | Fecha en la que se publicó la reseña (`YYYY-MM-DD`). |

### Notas Adicionales
- La columna `id` permite vincular cada reseña con un negocio en la tabla `metadata`.  
- `has_text` es útil para filtrar reseñas con y sin contenido textual, lo que puede influir en el análisis de sentimientos.  
- `vader_score` y `textblob_score` proporcionan dos perspectivas distintas sobre el sentimiento de la reseña:  
  - **VADER** es más preciso para lenguaje informal y opiniones en redes sociales.  
  - **TextBlob** usa técnicas de análisis gramatical y es más adecuado para textos formales.  
- La variable `date` permite realizar análisis temporales sobre la evolución de las calificaciones y sentimientos de los negocios.  

---

## Diccionario de Datos - Tabla `reviews_y`

### Descripción
La tabla `reviews_y` almacena información sobre reseñas de negocios extraídas de la base de datos de Yelp. Cada reseña está asociada a un negocio mediante el identificador `id` y contiene datos sobre la calificación dada por el usuario, la presencia de texto en la reseña, su fecha y dos análisis de sentimientos aplicados al contenido textual.

### Estructura de la Tabla

| Nombre de la columna  | Tipo de dato  | Descripción |
|----------------------|--------------|-------------|
| `id`                | `object`      | Identificador único del negocio al que pertenece la reseña. Se relaciona con la tabla `business`. |
| `rating`            | `int64`       | Calificación otorgada por el usuario en una escala de 1 a 5 estrellas. |
| `has_text`          | `int64`       | Indica si la reseña contiene texto (`1` sí, `0` no). |
| `vader_score`       | `float64`     | Puntuación de sentimiento de la reseña calculada con el modelo VADER (oscila entre -1 y 1, donde valores positivos indican sentimientos positivos y valores negativos indican sentimientos negativos). |
| `textblob_score`    | `float64`     | Puntuación de sentimiento calculada con el modelo TextBlob (valores entre -1 y 1, con interpretación similar a VADER pero metodología distinta). |
| `date`              | `object`      | Fecha en la que se publicó la reseña (`YYYY-MM-DD`). |

### Notas Adicionales
- La columna `id` permite vincular cada reseña con un negocio en la tabla `business`.  
- `has_text` facilita la distinción entre reseñas con contenido textual y aquellas que solo incluyen una calificación numérica.  
- `vader_score` y `textblob_score` permiten evaluar la polaridad del sentimiento expresado en la reseña:  
  - **VADER** es más preciso para lenguaje coloquial y comentarios breves.  
  - **TextBlob** aplica un análisis basado en gramática y es más adecuado para textos formales.  
- La columna `date` permite realizar análisis temporales de la evolución de la percepción de los negocios en Yelp.  

---

## Diccionario de Datos - Tabla `business_categories`

### Descripción
La tabla `business_categories` es una tabla intermedia diseñada para manejar la relación **muchos a muchos** entre los negocios y sus respectivas categorías. En lugar de asignar una única categoría a cada negocio, esta estructura permite que un negocio pueda estar asociado a múltiples categorías y, a su vez, que cada categoría pueda agrupar múltiples negocios.

En términos prácticos, esta tabla actúa como un puente entre la tabla de negocios (`business` o `metadata`, según la fuente de datos) y la tabla de categorías (`categorias`), asegurando que la información sobre la clasificación de cada negocio sea estructurada y eficiente.

### Estructura de la Tabla

| Nombre de la columna  | Tipo de dato  | Descripción |
|----------------------|--------------|-------------|
| `id`                | `object`      | Identificador único del negocio. Se relaciona con la tabla `business` (si proviene de Yelp) o `metadata` (si proviene de Google Maps). |
| `category_id`       | `int64`       | Identificador único de la categoría asociada al negocio. Se relaciona con la tabla `categorias`. |

### Ejemplo de Uso
Si en la base de datos de Yelp un negocio identificado con `id = "aapizzaxxxxx283578826647"` pertenece a tres categorías (`27`, `26` y `19`), en esta tabla encontraremos tres registros distintos para ese negocio, cada uno representando una de sus categorías:

| id                        | category_id |
|---------------------------|------------|
| aapizzaxxxxx283578826647  | 27         |
| aapizzaxxxxx283578826647  | 26         |
| aapizzaxxxxx283578826647  | 19         |

### Notas Adicionales
- La estructura de esta tabla optimiza la eficiencia de las consultas y evita la redundancia de datos en la tabla principal de negocios.  
- Para conocer todas las categorías de un negocio, se puede realizar una consulta que busque todas las `category_id` asociadas a su `id`.  
- Para listar todos los negocios dentro de una categoría específica, se puede filtrar la tabla por `category_id`.  
- Esta tabla permite expandir fácilmente la clasificación de negocios sin necesidad de modificar la estructura principal de las tablas `business` o `metadata`.  

---

## Diccionario de Datos - Tabla `business_categories_gm`

### Descripción
La tabla `business_categories_gm` es una tabla intermedia que gestiona la relación **muchos a muchos** entre los negocios y sus respectivas categorías en la base de datos de Google Maps. Su función es la misma que la de la tabla `business_categories`, pero aplicada a los datos extraídos de Google Maps.

Dado que un negocio puede pertenecer a múltiples categorías y que cada categoría puede incluir varios negocios, esta tabla permite organizar la clasificación de manera eficiente sin duplicar información en la tabla principal de negocios.

### Estructura de la Tabla

| Nombre de la columna  | Tipo de dato  | Descripción |
|----------------------|--------------|-------------|
| `id`                | `object`      | Identificador único del negocio en la base de Google Maps. Se relaciona con la tabla `metadata`. |
| `category_id`       | `int64`       | Identificador único de la categoría asociada al negocio. Se relaciona con la tabla `categorias`. |

### Ejemplo de Uso
Si en la base de datos de Google Maps un negocio identificado con `id = "abbalételavi257688801366"` pertenece a la categoría `37`, este negocio tendrá un único registro en esta tabla. Sin embargo, si otro negocio pertenece a múltiples categorías, tendrá múltiples registros, uno por cada `category_id` asociado.

| id                        | category_id |
|---------------------------|------------|
| aagrillxxxxx261688801011  | 45         |
| abacoagolfcl268885801199  | 61         |
| abacusbusine284586814547  | 37         |
| abbalételavi257688801366  | 37         |
| abbesdonutsh270467822499  | 37         |

### Notas Adicionales
- La columna `id` permite vincular cada negocio con sus categorías en la tabla `metadata`.  
- La estructura de esta tabla optimiza la consulta de categorías sin necesidad de almacenar múltiples valores dentro de una misma celda en la tabla de negocios.  
- Para conocer todas las categorías de un negocio, se puede hacer una consulta filtrando por `id`.  
- Para listar todos los negocios dentro de una categoría específica, se puede filtrar la tabla por `category_id`.  
- Este diseño permite expandir y modificar la clasificación de los negocios sin afectar la estructura de la tabla `metadata`.  

---

## Agrupaciones de Categorías  

### Descripción  
Dado que las categorías originales de los negocios presentaban una gran granularidad, se realizó un proceso de **agrupación y normalización** con el objetivo de consolidar la clasificación en grupos más manejables y coherentes.  

Las nuevas categorías **reemplazan** a las originales, es decir, cada negocio fue asignado a una o más categorías dentro de esta estructura agrupada. No existen negocios sin categoría asignada.  

La metodología utilizada para la agrupación se basó en **afinidad semántica**, agrupando categorías con características similares en cuanto a:  
- Tipo de cocina o región de origen (ej. *Asian, Mediterranean, Latin American*).  
- Modelo de negocio o tipo de servicio (ej. *Fast Food, Fine Dining, Buffets*).  
- Enfoque en dietas específicas (ej. *Vegetarian & Vegan, Halal*).  
- Características distintivas del lugar (ej. *Bars & Nightlife, Cafés*).  

Esta clasificación permite simplificar los análisis y facilitar la interpretación de los datos sin perder información relevante.  

### Estructura de la Agrupación de Categorías  

| Categoría Agrupada            | Categorías Originales Incluidas |
|--------------------------------|--------------------------------|
| **Chinese**                   | chinese, taiwanese, chinese noodle, cantonese, sichuan, dim sum, delivery chinese, hong kong style fast food, mandarin |
| **Japanese**                   | japanese, authentic japanese, japanese curry, izakaya, modern izakaya, ramen, sushi, teppanyaki, udon noodle, yakitori |
| **Korean**                     | korean, korean barbecue |
| **Thai**                       | thai |
| **Vietnamese**                 | vietnamese, pho |
| **Pacific & Filipino**         | filipino, hawaiian |
| **Indian**                     | indian, modern indian, indian muslim, indian sizzler, kerala, biryani |
| **Pakistani & Afghani**        | pakistani, afghani, bangladeshi |
| **Middle Eastern**             | middle eastern, lebanese, israeli, falafel, shawarma, persian, turkish, gyro |
| **Pan-Asian**                  | asian, asian fusion, panasian |
| **North African**              | moroccan, egyptian |
| **West African**               | west african, cape verdean |
| **General African**            | african, ethiopian, south african |
| **Mexican**                    | mexican, mexican torta, taco, texmex, burrito |
| **Centroamerican**             | central american, costa rican, guatemalan, honduran, nicaraguan, salvadoran |
| **Southern Cone**              | argentinian, chilean, uruguayan |
| **Tropical South American**    | brazilian, colombian, ecuadorian, peruvian, venezuelan |
| **Caribbean**                  | caribbean, cuban, dominican, haitian, jamaican, puerto rican |
| **Western European**           | french, modern french, french steakhouse, belgian, dutch, spanish, portuguese, italian, modern european, tuscan, northern italian, southern italian, neapolitan |
| **Central European**           | german, austrian, swiss, czech, polish, hungarian |
| **Eastern European**           | eastern european, bulgarian, romanian, russian, serbian, georgian, uzbeki |
| **Nordic & Scandinavian**      | scandinavian, swedish, icelandic |
| **British & Irish**            | british, modern british, english, irish |
| **North American**             | canadian, american, new american, traditional american, southern us, southwestern us, cajun, creole, contemporary louisiana, down home cooking, floridian, new england, californian |
| **Australian**                 | australian |
| **Pizza**                      | pizza |
| **Burgers & Fast Food**        | fast food, hamburger, cheesesteak, chicken wings, hot dog, hoagie, po boys |
| **Seafood**                    | seafood, angler fish, fish chips, seafood donburi, seafood farm, seafood market, seafood wholesaler |
| **Poke**                       | poke, poke bar |
| **Steakhouse & Grilled**       | chophouse, barbecue, mongolian barbecue |
| **Breakfast & Brunch**         | breakfast, brunch |
| **Vegetarian & Vegan**         | vegetarian, vegan, glutenfree, organic, raw food, tofu |
| **Desserts & Bakeries**        | dessert, pancake, sundae |
| **Fondue & Raclette**          | fondue, raclette |
| **Rice & Grain-Based**         | rice, biryani |
| **Cafés**                      | or cafe, espresso bar, coffee |
| **Buffet**                     | buffet |
| **Fine Dining**                | fine dining |
| **Bars & Nightlife**           | bar, bar grill, cocktail bar, cider bar, dart bar, gay bar, hookah bar, karaoke bar, live music bar, piano bar, sports bar, stand bar, tiki bar, wine bar |
| **Food Markets & Wholesale**   | fresh food market, frozen food store, frozen food manufacturer, self service, wholesale food store, dried seafood store, seafood market |
| **Food Industry & Supply**     | catering food and drink supplier, food and beverage consultant, food and beverage exporter, food bank, food broker, food court, food delivery, food machinery supplier, food manufacturer, food manufacturing supply, food processing company, food processing equipment, food producer, food products supplier, food seasoning manufacturer, food service, food store, supply store |
| **Ethnic & Fusion**            | eclectic, ethnic, fusion, panlatin, nuevo latino |
| **Family & Traditional**       | family, traditional, country food, soul food |
| **Snacks & Small Plates**      | snack bar, small plates, tapas, tapas bar |
| **Soup & Noodles**             | soup, chinese noodle, udon noodle, ramen, pho |
| **Mediterranean & Greek**      | mediterranean, greek |
| **Southeast Asian**            | southeast asian, cambodian, laotian, indonesian, singaporean |
| **South Asian**                | south asian, nepalese |
| **Jewish & Kosher**            | jewish, kosher |
| **Halal**                      | halal |
| **Health & Organic**           | health food, health food store, organic food store |
| **Chicken & Meat Dishes**      | chicken, meat dish |
| **Wok & Stir-Fry**             | wok |
| **Oyster Bars**                | oyster bar |
| **Karaoke**                    | karaoke |
| **Delivery & Takeout**         | delivery, takeout |
| **Lunch**                      | lunch |
| **Hot Pot**                    | hot pot |
| **Continental**                | continental |
| **European**                   | european |
| **Armenian**                   | armenian |

---

## Agrupaciones de Ciudades  

### Descripción  
En la base de datos original, los nombres de las ciudades presentaban **variaciones y subregiones** que dificultaban los análisis y la normalización de datos. Para solucionar esto, se realizó un proceso de **agrupación y estandarización**, consolidando nombres equivalentes bajo una única ciudad principal.  

El propósito de esta normalización es:  
- Unificar nombres de ciudades que aparecían con diferentes formatos o denominaciones.  
- Agrupar localidades o áreas menores bajo la ciudad principal correspondiente.  
- Mejorar la coherencia en los análisis de distribución geográfica de los negocios.  

Esta agrupación reemplaza las denominaciones originales, asegurando que todas las localidades se registren bajo una ciudad normalizada.  

### Estructura de la Agrupación de Ciudades  

| Ciudad Normalizada         | Nombres Originales Incluidos |
|---------------------------|--------------------------------|
| **Islamorada, Village Of Islands** | Islamorada, Tavernier |
| **St. Cloud**             | St Cloud, Kenansville, Harmony |
| **Port St. Joe**          | Port St Joe |
| **Wesley Chapel**         | Wesley Chapel South |
| **Northdale**             | Greater Northdale |
| **Carrollwood**           | Greater Carrollwood |
| **Tampa**                 | Ybor City |
| **St. Pete Beach**        | St Pete Beach, Pass-A-Grille Beach |
| **Clearwater**            | Clearwater Beach |
| **Rotonda**               | Rotonda West |
| **Lake Worth Beach**      | Lake Worth |
| **Plantation City**       | Plantation |
| **Miami Gardens**         | Carol City |
| **Hollywood**             | Hollywood Beach |
| **Miami**                 | Coconut Grove |
| **St. James City**        | St James City |
| **Port St. John**         | Port St John |
| **Glen St. Mary**         | Glen St Mary |
| **Laurel**                | Laurel Hill |
| **Pensacola**             | Pensacola Beach, Cantonment |
| **Pace**                  | Milton |
| **Crestview**             | Holt, Baker |
| **Fort Walton Beach**     | Shalimar |
| **Destin**                | Santa Rosa Beach, Sandestin |
| **Marianna**              | Alford |
| **Panama City**           | Wewahitchka, Ebro, Southport |
| **Panama City Beach**     | Inlet Beach, Alys Beach, Seacrest, Rosemary Beach |
| **DeFuniak Springs**      | Redbay, Ponce De Leon |
| **Brandon**               | Lithia |
| **Bradenton**             | Parrish |
| **Sarasota**              | University Park, Myakka City |
| **Port Charlotte**        | Placida |
| **Cape Coral**            | Boca Grande |
| **Key West**              | Little Torch Key, Summerland Key, Naval Air Station Key West |
| **West Palm Beach**       | Singer Island, Golden Lakes, Loxahatchee |
| **Boca Raton**            | Sandalfoot Cove |
| **Naples**                | Everglades City, Ochopee, Goodland |
| **Fort Myers**            | Miromar Lakes, Tice |
| **Sebring**               | Lorida, Palmdale |
| **Kissimmee**             | Reunion, Intercession City |
| **Lake Wales**            | River Ranch |
| **Melbourne**             | Patrick AFB, Melbourne Beach, Patrick Space Force Base, Patrick Afb |
| **Jacksonville**          | St. Johns, Ponte Vedra Beach, Mayport, St Johns |
| **Fernandina Beach**      | Amelia Island |
| **Palatka**               | Florahome, Georgetown, San Mateo, East Palatka, Satsuma |
| **Gainesville**           | Keystone Heights, Melrose, Hawthorne, Jonesville, 3720 NW 13th St Suite #14 Gainesville |
| **Ocala**                 | Fort McCoy, Citra, Sparr, Fort McCoy, Salt Springs, Belleview, Anthony |
| **St. Augustine**         | Elkton, Hastings, St Augustine Beach |
| **Sanford**               | Lake Monroe |
| **Deltona**               | Osteen, Pierson, DeLand |
| **Orlando**               | Chuluota, Sand Lake |
| **Mount Dora**            | Mt Dora, Mt Plymouth |
| **The Villages**          | Oxford, Summerfield, Weirsdale, Sumterville |
| **Beverly Hills**         | Pine Ridge |
| **Lake City**             | Branford, White Springs, Wellborn, Sanderson |
| **Chiefland**             | Old Town |
| **Perry**                 | Steinhatchee, Horseshoe Beach |
| **Apalachicola**          | St George Island |
| **Tallahassee**           | Lamont, St Marks, Wakulla Springs |
| **Madison**               | Lee |
| **Live Oak**              | Mayo, Jennings |
| **Lake Butler City**      | Lake Butler |
| **Starke**                | Raiford |
| **Brooksville**           | Brooksville, Springhill |
| **Holmes Beach**          | Holmes Beach, Westville |

### Notas Adicionales  
- Cada nombre en la columna de **"Nombres Originales Incluidos"** ha sido **normalizado** bajo la ciudad principal correspondiente.  
- Esta agrupación mejora la coherencia en los análisis y evita la dispersión de datos debida a nombres alternativos o subdivisiones dentro de una misma área metropolitana.  
- Para identificar la ubicación real de un negocio en la base de datos, se recomienda usar la columna **`city_normalized`** en la tabla `ciudades`.  

---


