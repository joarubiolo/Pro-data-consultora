import streamlit as st
import pandas as pd
import numpy as np
import pickle
from google.cloud import bigquery
from google.cloud import storage
import collections
from collections import Counter
import ast
import plotly.express as px
from sklearn.cluster import KMeans
import os
import io
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import xgboost as xgb
from xgboost import XGBClassifier
import joblib
import folium
from streamlit.components.v1 import html
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error
from tensorflow.keras.layers import Dropout


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\rubio\Documents\SoyHenry\Proyecto Final 2.0\clave json\deft-sight-449512-e3-19ad4d3c18f0.json"

client = bigquery.Client()

metadatos = client.get_table('datos_procesados.metadatos')

st.title("Pro-Data: Anlisis de mercado gastronomico")

tab1, tab2, tab3, tab4 = st.tabs(["Analisis general", "Modelo de recomendacion #1", "Modelo de recomendacion #2", "Modelo de recomendacion #3"])

with tab1:
    st.subheader('Descubra aqui su proximo negocio gastronomico')
    st.write("A continuacion elija una ciudad donde desee establecer su negocio")

    metadatos = client.list_rows(metadatos).to_dataframe()

    city = st.selectbox("Seleccionar Ciudad", metadatos["city"].unique())

    # Función para obtener datos de BigQuery
    @st.cache_data
    def obtener_metadatos(city):
        consulta = f"""
        SELECT  *
        FROM `deft-sight-449512-e3.datos_procesados.metadatos`
        WHERE city = '{city}'
        """
        return client.query(consulta).to_dataframe()

    @st.cache_data
    def obtener_reviews(city):
        consulta = f"""
        SELECT  *
        FROM `deft-sight-449512-e3.datos_procesados.reviews`
        ORDER BY date DESC
        """
        return client.query(consulta).to_dataframe()

    datos = obtener_metadatos(city)
    reseñas = obtener_reviews(city)

    datos_ordenados = datos[['name', 'stars', 'review_count']].sort_values(by='review_count', ascending=False)

    st.dataframe(
        data=datos_ordenados, use_container_width=True, 
        hide_index=True, column_config=None, key=None, 
        on_select="ignore", selection_mode="multi-row", row_height=None
        )
    st.write(f"📍 Negocios en {city}: {len(datos)}")


    # Cargar datos
    st.subheader(f"📊 Análisis de Negocios en {city}")
    #st.sidebar.header("Configuración")

    

    categorias = datos["categories"].value_counts().reset_index()
    categorias.columns = ["categories", "count"]  # Renombrar columnas

    st.write(f'categorias mas relevantes:')
    st.dataframe(categorias.head(5), use_container_width=True, height=215)

    st.write(f"🍔 Cantidad de Categorías de Negocios: {len(categorias)}")

    
    # 🌎 Mapa de distribución geográfica

    st.subheader("🌍 Mapa de Distribución de Negocios")
    st.write("Utilice los controles para navegar en el mapa")

    if not datos.empty:
        centro_lat = datos["latitude"].mean()
        centro_lon = datos["longitude"].mean()

        # Definir automáticamente el zoom según la dispersión de los datos
        lat_min, lat_max = datos["latitude"].min(), datos["latitude"].max()
        lon_min, lon_max = datos["longitude"].min(), datos["longitude"].max()

        # Calcular el nivel de zoom (menor dispersión = más zoom)
        zoom_nivel = 12 if (lat_max - lat_min) < 0.1 and (lon_max - lon_min) < 0.1 else \
                    10 if (lat_max - lat_min) < 0.5 and (lon_max - lon_min) < 0.5 else 8

        fig_mapa = px.scatter_mapbox(
            datos, lat="latitude", lon="longitude", hover_name="name",
            hover_data={"categories": True, "stars": True, "review_count": True},
            color="review_count",
            labels={"review_count": "Cantidad de reseñas"},  # 🔹 Cambiar la etiqueta
            color_continuous_scale=["#FF6347", "#1E90FF"],  # Rojo → Azul
            size="stars",
            mapbox_style="open-street-map",
            zoom=zoom_nivel,
            center={"lat": centro_lat, "lon": centro_lon}  # Centrar en los negocios
        )

        st.plotly_chart(fig_mapa, use_container_width=True)
    else:
        st.warning("No hay negocios disponibles para mostrar en el mapa.")


    # 🎯 Modelo de recomendación basado en carencias del mercado

    st.subheader("📌 Zonas con caracteristicas Gastronómica")
    st.write("A continuación se muestran las zonas y sus características relevantes")


    if not datos.empty:
        # Aplicar KMeans para segmentar en zonas
        coordenadas = datos[["latitude", "longitude"]]
        modelo = KMeans(n_clusters=5, random_state=42, n_init=10)
        datos["zona"] = modelo.fit_predict(coordenadas)

        # Encontrar la categoría más frecuente en cada zona
        categoria_relevante = datos.groupby("zona")["categories"].agg(lambda x: x.mode()[0]).reset_index()
        categoria_relevante.rename(columns={"categories": "categoria_relevante"}, inplace=True)

        # Calcular el centroide de cada zona
        centroides = datos.groupby("zona").agg({
            "latitude": "mean",
            "longitude": "mean"
        }).reset_index()

        # Unir el centroide con la categoría más frecuente
        centroides = centroides.merge(categoria_relevante, on="zona", how="left")

        # Crear nombres personalizados para las zonas
        centroides["zona_nombre"] = centroides["zona"].astype(str) + " -> " + centroides["categoria_relevante"]

        # Calcular centro del mapa
        centro_lat = centroides["latitude"].mean()
        centro_lon = centroides["longitude"].mean()

        # Crear el mapa con un solo punto por zona
        fig_zonas = px.scatter_mapbox(
            centroides, lat="latitude", lon="longitude",
            text="zona_nombre",  # Mostrar el nombre personalizado de la zona
            hover_data={"zona_nombre": True, "latitude": False, "longitude": False, "categoria_relevante": False},
            labels={"zona_nombre": "Zona"},  # Etiqueta en español
            mapbox_style="open-street-map", zoom=10,
            center={"lat": centro_lat, "lon": centro_lon}
        )

        fig_zonas.update_traces(marker=dict(size=14))  # Tamaño adecuado

        st.plotly_chart(fig_zonas, use_container_width=True)

    else:
        st.warning("⚠️ No hay negocios disponibles para mostrar en el mapa.")



    # 📈 Análisis de calidad (ratings y reviews)
    st.subheader("⭐ Calidad de los Negocios")

    # Contar la cantidad de reseñas por calificación
    df_count = reseñas["rating"].value_counts().reset_index()
    df_count.columns = ["rating", "count"]

    # Ordenar los valores por rating
    df_count = df_count.sort_values("rating")

    # Crear bar plot
    fig_bar = px.bar(df_count, x="rating", y="count", 
                    title="Cantidad de Reseñas por Calificación",
                    labels={"rating": "Calificación", "count": "Cantidad de Reseñas"},
                    color="count", color_continuous_scale="blues")

    # Mostrar en Streamlit
    st.plotly_chart(fig_bar, use_container_width=True)

    # Mostrar la evolucion de reviews a traves del tiempo
    st.subheader("📅 Evolución de Reviews")

    # Agrupar por fecha para contar la cantidad de reviews por día
    df_count = reseñas.groupby("date").size().reset_index(name="count")

    # Crear line plot
    fig_line = px.line(df_count, x="date", y="count", 
                    title="Cantidad de Reseñas a lo Largo del Tiempo",
                    labels={"date": "Fecha", "count": "Cantidad de Reseñas"},
                    markers=True)

    # Mostrar en Streamlit
    st.plotly_chart(fig_line, use_container_width=True)


with tab2:
    st.subheader("Modelo de Recomendación de Negocios")

    # Cargar datos
    # Función para obtener datos de BigQuery
    @st.cache_data
    def obtener_metadatos():
        consulta = f"""
        SELECT  *
        FROM `deft-sight-449512-e3.datos_procesados.metadatos`
        """
        return client.query(consulta).to_dataframe()

    def obtener_reviews():
        consulta = f"""
        SELECT  *
        FROM `deft-sight-449512-e3.datos_procesados.reviews`
        ORDER BY date DESC
        """
        return client.query(consulta).to_dataframe()

    st.write("Elija las opciones que desee agregar para su negocio y la prediccion se arrojara automaticamente")

    caracteristicas = ['delivery', 'takeout', 'dinein',
       'outdoor_seating', 'drivethrough', 'good_for_working_on_laptop',
       'solo_dining', 'wheelchair_friendly', 'alcohol_beverage',
       'healthy_food', 'fast_comfort_food', 'braille_menu', 'all_you_can_eat',
       'coffee', 'dancing', 'catering', 'counter_service', 'pay_ahead',
       'seating', 'breakfast', 'lunch', 'dinner', 'dessert', 'casual',
       'romantic', 'formal', 'trendy', 'with_reservation', 'usually_a_wait',
       'quick_visit', 'black_owned', 'women_led', 'veteran_led',
       'entertainment', 'live_entertainment', 'lgbtq_friendly', 'fast_service',
       'fireplace', 'rooftop_seating', 'sports', 'college_students',
       'family_friendly', 'groups', 'locals', 'tourists', 'kids_friendly',
       'wi_fi', 'bar_onsite', 'cash_only', 'checks', 'credit_cards',
       'debit_cards', 'nfc_mobile_payments', 'recycling']

    caracteristicas_esp = ['delivery', 'para llevar', 'comer en el local',
        'asientos al aire libre', 'autoservicio', 'bueno para trabajar con laptop',
        'cenas en solitario', 'accesible para sillas de ruedas', 'bebidas alcohólicas',
        'comida saludable', 'comida rápida confort', 'menú en braille', 'todo lo que puedas comer',
        'café', 'baile', 'servicio de catering', 'servicio en mostrador', 'pago por adelantado',
        'asientos', 'desayuno', 'almuerzo', 'cena', 'postre', 'casual',
        'romántico', 'formal', 'moderno', 'con reservación', 'suele haber espera',
        'visita rápida', 'liderado por personas de color', 'liderado por mujeres', 'liderado por veteranos',
        'entretenimiento', 'espectáculos en vivo', 'amigable con LGBTQ+', 'servicio rápido',
        'chimenea', 'asientos en azotea', 'deportes', 'para estudiantes universitarios',
        'familiar', 'grupos', 'lugareños', 'turistas', 'amigable para niños',
        'wifi', 'bar en el lugar', 'solo efectivo', 'cheques', 'tarjetas de crédito',
        'tarjetas de débito', 'pagos móviles NFC', 'reciclaje']


    # crear cliente de storage
    storage = storage.Client()
    bucket = storage.bucket("ml_databases")
    blob = bucket.blob("trained_model.h5")
    blob.download_to_filename("trained_model.h5")

    # Cargar el modelo entrenado
    # model = storage.bucket('ml_databases').blob('trained_model.h5')
    model = tf.keras.models.load_model('trained_model.h5')

    input_data = np.zeros((1, 54))

    # Crear tres columnas
    col1, col2, col3 = st.columns(3)

    # Distribuir los checkboxes en las columnas
    for i, caracteristica in enumerate(caracteristicas_esp):
        col = [col1, col2, col3][i % 3]  # Alternar entre columnas
        with col:
            if st.checkbox(caracteristica):
                input_data[0, i] = 1
                
    # Hacer la predicción
    prediction = model.predict(input_data)

    prediction = np.round(prediction,1)

    if prediction == 1:
        st.write("🔮 La predicción de éxito del negocio es:", "✅ Positiva")
    else:
        st.write("🔮 La predicción de éxito del negocio es:", "❌ Negativa")


with tab3:
    st.write('Recomendacion de ciudades para el negocio')

    blob2 = bucket.blob("Modelo_P_h.h5")
    blob3 = bucket.blob("Modelo_P_C.h5")
    blob2.download_to_filename("Modelo_P_h.h5")
    blob3.download_to_filename("Modelo_P_C.h5")

    modelo_P_h = load_model('Modelo_P_h.h5')
    modelo_P_h.compile(optimizer='Nadam', loss='mean_squared_error', metrics=['accuracy', 'mse'])

    modelo_P_C = load_model('Modelo_P_C.h5')
    modelo_P_C.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy', 'mse'])

    client = bigquery.Client()

    query = "SELECT * FROM `datos_ML.metadatos_ML`"
    getquery = client.query(query)

    query2 = "SELECT * FROM `datos_ML.atributos`"
    getquery2 = client.query(query2)

    query3 = "SELECT * FROM `datos_ML.categorias`"
    getquery3 = client.query(query3)

    metadatos1 = getquery.to_dataframe()
    atributos = getquery2.to_dataframe()
    categorias = getquery3.to_dataframe()

    lista_categorias = categorias['category'].tolist()

    metadatos1.drop(columns=['name', 'street_address', 'postal_code','review_count', 'is_open'],inplace=True)

    def atributos_destacados(df, atributos):
        '''Devuelve los atributos que más se repiten ordenados de mayor a menor '''
        # Expandimos la lista de atributo_id para obtener el nombre del atributo correspondiente
        df['atributo_nombres'] = df['atributo_id'].apply(lambda x: [atributos[atributos['atributo_id'] == id_]['atributo'].values[0] for id_ in x])
        # Luego, unimos todos los atributos de todas las filas
        todos_los_atributos = df['atributo_nombres'].explode().tolist()
        # Contamos las frecuencias de los atributos
        frecuencia_atributos = pd.Series(todos_los_atributos).value_counts()
        atributos_ordenados = frecuencia_atributos.index.tolist()
        return atributos_ordenados

    # Crear la interfaz de usuario con Streamlit
    st.title("Sistema de Recomendación por Categoría de Restaurantes")

    # Crear el menú desplegable para seleccionar la categoría
    categoria = st.selectbox('Selecciona una categoría de restaurante:', [''] + categorias['category'].tolist())


    if categoria:
        try:
            categoria = categoria.lower()
            categorias["category"] = categorias["category"].str.lower()
            metadatos2 = metadatos1.copy()
            
            # Filtramos por categorías
            id_categoria = categorias[categorias["category"] == categoria]
            id_categoria = id_categoria.reset_index(drop=True)
            metadatos2['category_id'] = metadatos2['category_id'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
            metadatos2['atributo_id'] = metadatos2['atributo_id'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
            df_categ = metadatos2[metadatos2['category_id'].apply(lambda x: id_categoria.loc[0, "category_id"] in x)]
            df_categ = df_categ.reset_index(drop=True)
            
            # Número de restaurantes por ciudad
            numero_restaurantes = df_categ.groupby('city_id').size()
            df_categ["numero_restaurantes"] = df_categ['city_id'].map(numero_restaurantes)
            df_categ['category_id'] = id_categoria.loc[0, "category_id"]
            
            # Usamos el primer modelo
            scaler = MinMaxScaler()
            X_c = df_categ[['reviews_positivas', 'reviews_negativas', 'stars']]
            X_c[['reviews_positivas', 'reviews_negativas', 'stars']] = scaler.fit_transform(X_c[['reviews_positivas', 'reviews_negativas', 'stars']])
            y_c = modelo_P_C.predict(X_c)
            df_categ["(1/P_C)_i"] = y_c
            df_categ["1/P_C"] = df_categ.groupby('city_id')["(1/P_C)_i"].transform('sum') / df_categ["numero_restaurantes"]

            # Usamos el segundo modelo
            df_categ_ciu = df_categ.drop_duplicates(subset='city_id', ignore_index=True)
            X_h = df_categ_ciu[['population', 'numero_restaurantes']]
            X_h[['population', 'numero_restaurantes']] = scaler.fit_transform(X_h[['population', 'numero_restaurantes']])
            y_h = modelo_P_h.predict(X_h)
            df_categ_ciu["P_h"] = y_h

            a = 2.5
            b = 1
            df_categ_ciu["Phi"] = a * df_categ_ciu["P_h"] + b * df_categ["1/P_C"]
            
            # Ordenar por la predicción
            df_categ_ciu = df_categ_ciu.sort_values(by='Phi', ascending=False)

            # Obtener las top 3 ciudades
            top_ciudades = df_categ_ciu[["city", "latitude", "longitude"]].head(3)
            top_ciudades = top_ciudades.reset_index(drop=True)
            top_ciudades_list = top_ciudades["city"]

            # Mostrar las ciudades con latitudes y longitudes en formato DataFrame
            st.subheader(f'Top 3 ciudades para la categoría {categoria.title()}')
            st.dataframe(top_ciudades_list)  # Mostrar las ciudades con latitudes y longitudes

            # Crear el mapa de las ciudades en Florida
            map_florida = folium.Map(location=[27.9944024, -81.7602544], zoom_start=7)  # Centrado en Florida
            for idx, row in top_ciudades.iterrows():
                folium.Marker(
                    location=[row['latitude'], row['longitude']],
                    popup=row['city']
                ).add_to(map_florida)

            # Mostrar el mapa
            st.subheader("Mapa de las 3 ciudades principales")
            map_html = map_florida._repr_html_()  # Obtener el mapa como HTML
            st.components.v1.html(map_html, height=500)

            # Ordenar por el cálculo de '1/P_C' para los restaurantes
            df_categ = df_categ.sort_values(by='1/P_C', ascending=True)
            top_atributos = atributos_destacados(df_categ, atributos)
            top10_atributos = pd.DataFrame(top_atributos, columns=["Atributos"])
            
            st.subheader(f'Top 10 atributos más destacados para la categoría {categoria.title()}')
            st.write(top10_atributos.head(10))  # Mostrar los 10 atributos más destacados

        except Exception as e:
            st.error(f"Error: {str(e)}")

with tab4:
    # Cargar modelo y datos
    #modelo_xgb = joblib.load("./modelo_xgb_1.pkl")

    #storage = storage.Client()
    bucket = storage.bucket("ml_databases")
    blob = bucket.blob("modelo_xgb_1.pkl")
    blob.download_to_filename("modelo_xgb_1.pkl")

    with open("modelo_xgb_1.pkl", "rb") as f:
        modelo_xgb = pickle.load(f)

    client = bigquery.Client()

    query = "SELECT * FROM `datos_procesados.ciudad_categoria_procesado`"
    getquery4 = client.query(query)

    ciudad_categoria = getquery4.to_dataframe()

    # ------------------- Función de Predicción -------------------
    def predecir_categoria_recomendada(ciudad, df, modelo):
        df_ciudad = df[df["city"] == ciudad][["city", "category", "competencia", "avg_rating", "avg_vader_score", "avg_textblob_score", "poblacion"]]

        if df_ciudad.empty:
            return f"No hay datos disponibles para la ciudad: {ciudad}"

        # Seleccionar solo las columnas relevantes
        X_nueva_ciudad = df_ciudad[["competencia", "avg_rating", "avg_vader_score", "avg_textblob_score", "poblacion"]]

        # Hacer predicciones
        df_ciudad["recomendado"] = modelo.predict(X_nueva_ciudad)

        # Filtrar solo las categorías recomendadas
        categorias_recomendadas = df_ciudad[df_ciudad["recomendado"] == 1]["category"]

        return categorias_recomendadas

    # ------------------- Interfaz en Streamlit -------------------
    st.title("🛍️ Recomendador de Negocios en Streamlit")

    # Input del usuario para ingresar la ciudad
    ciudad_usuario = st.text_input("Ingresa la ciudad:")

    if st.button("Predecir"):
        if ciudad_usuario:
            categorias = predecir_categoria_recomendada(ciudad_usuario, ciudad_categoria, modelo_xgb)

            if isinstance(categorias, str):
                st.warning(categorias)  # Si no hay datos, mostrar mensaje de advertencia
            else:
                st.success(f"Categorías recomendadas para {ciudad_usuario}:")
                st.write(categorias.to_frame().reset_index(drop=True))  # Mostrar en formato tabular
        else:
            st.error("Por favor, ingresa una ciudad.")    