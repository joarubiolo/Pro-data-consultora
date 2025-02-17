# **Diccionario de Datos - `metadata_fl`**

## **Introducción**  
El presente diccionario de datos documenta la estructura y contenido del conjunto de datos `metadata_fl`, el cual ha sido generado a partir de información extraída de Google Maps. Este dataset ha sido sometido a un exhaustivo proceso de limpieza, transformación y normalización con el objetivo de proporcionar información estructurada y relevante sobre establecimientos comerciales ubicados en Florida, EE.UU.  

El propósito de este diccionario es servir como referencia para analistas de datos, científicos de datos y otros profesionales que utilicen esta información en la construcción de modelos de Machine Learning, análisis de KPIs y toma de decisiones estratégicas.  

A lo largo del proceso de transformación, se han consolidado y redefinido diversas categorías para mejorar la interpretabilidad de los datos. Además, se han estandarizado los nombres de las variables y se han aplicado reglas de consistencia para garantizar su usabilidad en distintos contextos analíticos.  

En las siguientes secciones, se detallan cada una de las variables incluidas en `metadata_fl`, describiendo su significado, tipo de dato y posibles valores.


## Estructura de Datos

La siguiente tabla describe la estructura del DataFrame `metadata_fl`, detallando cada variable, su tipo de dato y una breve descripción de su contenido.

| #  | Nombre de la columna          | Tipo de Dato | Descripción |
|----|------------------------------|-------------|-------------|
| 0  | `gmap_id`                     | object      | Identificador único del negocio en Google Maps. |
| 1  | `name`                         | object      | Nombre del negocio. |
| 2  | `street_address`               | object      | Dirección exacta del negocio. |
| 3  | `city`                         | object      | Ciudad donde se encuentra el negocio. |
| 4  | `state`                        | object      | Estado donde se encuentra el negocio. |
| 5  | `postal_code`                   | int64       | Código postal del negocio. |
| 6  | `latitude`                      | float64     | Latitud de la ubicación del negocio. |
| 7  | `longitude`                     | float64     | Longitud de la ubicación del negocio. |
| 8  | `categories`                    | object      | Categorías en las que se clasifica el negocio. |
| 9  | `stars`                         | float64     | Calificación promedio del negocio en estrellas. |
| 10 | `review_count`                  | int64       | Número total de reseñas del negocio. |
| 11 | `is_open`                       | int64       | Indica si el negocio está abierto (`1`) o cerrado permanentemente (`0`). |
| 12 | `delivery`                      | int64       | Indica si el negocio ofrece servicio de entrega (`1`: Sí, `0`: No). |
| 13 | `takeout`                       | int64       | Indica si el negocio ofrece servicio para llevar (`1`: Sí, `0`: No). |
| 14 | `dinein`                        | int64       | Indica si el negocio permite comer en el local (`1`: Sí, `0`: No). |
| 15 | `outdoor_seating`               | int64       | Indica si el negocio tiene asientos al aire libre (`1`: Sí, `0`: No). |
| 16 | `drivethrough`                  | int64       | Indica si el negocio cuenta con servicio de autoservicio (`1`: Sí, `0`: No). |
| 17 | `good_for_working_on_laptop`    | int64       | Indica si el negocio es adecuado para trabajar con laptop (`1`: Sí, `0`: No). |
| 18 | `solo_dining`                   | int64       | Indica si el negocio es adecuado para comer solo (`1`: Sí, `0`: No). |
| 19 | `wheelchair_friendly`           | int64       | Indica si el negocio es accesible para sillas de ruedas (`1`: Sí, `0`: No). |
| 20 | `alcohol_beverage`              | int64       | Indica si el negocio ofrece bebidas alcohólicas (`1`: Sí, `0`: No). |
| 21 | `healthy_food`                  | int64       | Indica si el negocio ofrece opciones de comida saludable (`1`: Sí, `0`: No). |
| 22 | `fast_comfort_food`             | int64       | Indica si el negocio ofrece comida rápida o reconfortante (`1`: Sí, `0`: No). |
| 23 | `braille_menu`                  | int64       | Indica si el negocio ofrece menú en braille (`1`: Sí, `0`: No). |
| 24 | `all_you_can_eat`               | int64       | Indica si el negocio ofrece servicio de "todo lo que puedas comer" (`1`: Sí, `0`: No). |
| 25 | `coffee`                        | int64       | Indica si el negocio ofrece café como producto destacado (`1`: Sí, `0`: No). |
| 26 | `dancing`                       | int64       | Indica si el negocio tiene pista o área para bailar (`1`: Sí, `0`: No). |
| 27 | `catering`                      | int64       | Indica si el negocio ofrece servicio de catering (`1`: Sí, `0`: No). |
| 28 | `counter_service`               | int64       | Indica si el negocio tiene servicio en mostrador (`1`: Sí, `0`: No). |
| 29 | `pay_ahead`                     | int64       | Indica si el negocio permite pagar por adelantado (`1`: Sí, `0`: No). |
| 30 | `seating`                       | int64       | Indica si el negocio cuenta con espacio para sentarse (`1`: Sí, `0`: No). |
| 31 | `breakfast`                     | int64       | Indica si el negocio ofrece desayuno (`1`: Sí, `0`: No). |
| 32 | `lunch`                         | int64       | Indica si el negocio ofrece almuerzo (`1`: Sí, `0`: No). |
| 33 | `dinner`                        | int64       | Indica si el negocio ofrece cena (`1`: Sí, `0`: No). |
| 34 | `dessert`                     | int64       | Indica si el negocio ofrece postres (`1`: Sí, `0`: No). **(Fusión de `Popular_for_dessert` y `Dessert`)** |
| 35 | `casual`                       | int64       | Indica si el ambiente del negocio es casual (`1`: Sí, `0`: No). |
| 36 | `romantic`                     | int64       | Indica si el negocio tiene un ambiente romántico (`1`: Sí, `0`: No). |
| 37 | `formal`                       | int64       | Indica si el ambiente del negocio es formal (`1`: Sí, `0`: No). |
| 38 | `trendy`                       | int64       | Indica si el negocio es popular y sigue tendencias (`1`: Sí, `0`: No). |
| 39 | `with_reservation`             | int64       | Indica si el negocio permite o recomienda reservaciones (`1`: Sí, `0`: No). **(Fusión de varias opciones en `Planning`)** |
| 40 | `usually_a_wait`               | int64       | Indica si usualmente hay que esperar para ser atendido (`1`: Sí, `0`: No). |
| 41 | `quick_visit`                  | int64       | Indica si el negocio es adecuado para visitas rápidas (`1`: Sí, `0`: No). |
| 42 | `black_owned`                  | int64       | Indica si el negocio es identificado como propiedad de personas afrodescendientes (`1`: Sí, `0`: No). |
| 43 | `women_led`                    | int64       | Indica si el negocio es identificado como liderado por mujeres (`1`: Sí, `0`: No). |
| 44 | `veteran_led`                  | int64       | Indica si el negocio es identificado como propiedad de veteranos (`1`: Sí, `0`: No). |
| 45 | `entertainment`                | int64       | Indica si el negocio tiene entretenimiento general (`1`: Sí, `0`: No). **(Agrupación de `play_area`, `trivia_night`, `bar_games`)** |
| 46 | `live_entertainment`           | int64       | Indica si el negocio ofrece entretenimiento en vivo (`1`: Sí, `0`: No). **(Agrupación de `live_performances`, `karaoke`, `live_music`)** |
| 47 | `lgbtq_friendly`               | int64       | Indica si el negocio es amigable con la comunidad LGBTQ+ (`1`: Sí, `0`: No). **(Fusión de `lgbtq_friendly`, `transgender_safespace` y `gender_neutral_restroom`)** |
| 48 | `fast_service`                 | int64       | Indica si el negocio tiene un servicio rápido (`1`: Sí, `0`: No). |
| 49 | `fireplace`                    | int64       | Indica si el negocio tiene chimenea (`1`: Sí, `0`: No). |
| 50 | `rooftop_seating`              | int64       | Indica si el negocio tiene asientos en la azotea (`1`: Sí, `0`: No). |
| 51 | `sports`                       | int64       | Indica si el negocio está orientado a eventos deportivos (`1`: Sí, `0`: No). |
| 52 | `college_students`             | int64       | Indica si el negocio es frecuentado por estudiantes universitarios (`1`: Sí, `0`: No). |
| 53 | `family_friendly`              | int64       | Indica si el negocio es apto para familias (`1`: Sí, `0`: No).|
| 54 | `groups`                       | int64       | Indica si el negocio es adecuado para grupos (`1`: Sí, `0`: No). |
| 55 | `locals`                       | int64       | Indica si el negocio es frecuentado por residentes locales (`1`: Sí, `0`: No). |
| 56 | `tourists`                     | int64       | Indica si el negocio es frecuentado por turistas (`1`: Sí, `0`: No). |
| 57 | `kids_friendly`                | int64       | Indica si el negocio tiene opciones adecuadas para niños (`1`: Sí, `0`: No). **(Fusión de `kids` y `kids_friendly`)** |
| 58 | `wi_fi`                        | int64       | Indica si el negocio ofrece acceso a Wi-Fi (`1`: Sí, `0`: No). |
| 59 | `bar_onsite`                   | int64       | Indica si el negocio tiene un bar en sus instalaciones (`1`: Sí, `0`: No). |
| 60 | `cash_only`                    | int64       | Indica si el negocio solo acepta pagos en efectivo (`1`: Sí, `0`: No). |
| 61 | `checks`                       | int64       | Indica si el negocio acepta cheques como método de pago (`1`: Sí, `0`: No). |
| 62 | `credit_cards`                 | int64       | Indica si el negocio acepta tarjetas de crédito (`1`: Sí, `0`: No). |
| 63 | `debit_cards`                  | int64       | Indica si el negocio acepta tarjetas de débito (`1`: Sí, `0`: No). |
| 64 | `nfc_mobile_payments`          | int64       | Indica si el negocio acepta pagos móviles mediante NFC (`1`: Sí, `0`: No). |
| 65 | `recycling`                    | int64       | Indica si el negocio tiene programas de reciclaje (`1`: Sí, `0`: No). **(Fusión de `plastic_bags` y `glass_bottles`)** |
