import pandas as pd
import numpy as np 
import ast
from tensorflow.keras.models import load_model
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
import folium
from streamlit.components.v1 import html  # Importar el componente HTML de Streamlit

# Cargar los modelos
modelo_P_h = load_model('Modelo_P_h.h5')
modelo_P_h.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy', 'mse'])

modelo_P_C = load_model('Modelo_P_C.h5')
modelo_P_C.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy', 'mse'])

# Cargar los datos
metadatos1 = pd.read_csv('metadatos_ML.csv')
atributos = pd.read_csv('atributos.csv')
categorias = pd.read_csv('categorias.csv')

# Limpiar los datos
metadatos1.drop(columns=['name', 'street_address', 'postal_code', 'review_count', 'is_open'], inplace=True)

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
