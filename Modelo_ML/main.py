import pandas as pd
import ast
from tensorflow.keras.models import load_model
from fastapi import FastAPI, HTTPException


modelo = load_model('Modelo_entrenado.h5')
metadatos=pd.read_csv("metadatos_ML.csv")
categorias=pd.read_csv('categories_normalized.csv')
ciudades=pd.read_csv('ciudades_normal.csv')

app = FastAPI()

app.title="Base de datos de películas"

@app.get("/Sistema_de_recomendación/", tags=["Recomendación por Categoría"])
def Recomendación(categoria:str):
    '''Esta función recibe una categoría de restaurant y devuelve las 3 ciudades más recomendadas en las cuales empezar uno 
    y los atributos qmas importantes que deería tener.'''
    try:
        categoria=categoria.lower()
        categorias["category"]=categorias["category"].str.lower()
        metadatos2=metadatos.copy()
        # Filtramos por categorias
        id_categoria=categorias[categorias["category"]==categoria]
        id_categoria=id_categoria.reset_index(drop=True)
        metadatos2['category_id']=metadatos2['category_id'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
        df_categ=metadatos2[metadatos2['category_id'].apply(lambda x: id_categoria.loc[0,"category_id"] in x)]
        df_categ=df_categ.reset_index(drop=True)
        df_categ['category_id']=id_categoria.loc[0,"category_id"]
        df_categ["P_r"]=(df_categ['reviews_positivas']/df_categ['reviews_negativas'])*df_categ['numero_reviews']
        df_categ["P_c"]=df_categ['stars']*df_categ['numero_reviews']
        df_categ["P_r+P_c"]=df_categ["P_r"]+df_categ["P_c"]
        # Eliminamos los duplicados en las ciudades para que tengamos solo datos de ciudades
        df_categ_ciu=df_categ.drop_duplicates(subset='city_id',ignore_index=True)
        # Creamos el X y el y
        X=df_categ_ciu[['city_id', 'category_id']]
        # Aplico el modelo
        modelo.compile(optimizer='Nadam', loss='mean_squared_error')
        y_pred = modelo.predict(X)
        # Asignar el resultado de la predicción
        df_categ_ciu['Phi'] = y_pred
        # Ordenar por la predicción
        df_categ_ciu = df_categ_ciu.sort_values(by='Phi', ascending=False)
        # Obtener las top 5 ciudades
        top_ciudades = df_categ_ciu["city"].head(3)
        top_ciudades_list=top_ciudades.reset_index(drop=True).to_list()
        # Ordenar por el cálculo de 'P_r+P_c' para los restaurantes
        df_categ = df_categ.sort_values(by='P_r+P_c', ascending=True)
        # Seleccionar las columnas deseadas para el top 5 de restaurantes
        top_restaurants = df_categ.iloc[:, 5:-7].head(5)
        # Contar la cantidad de '1' por columna para encontrar los atributos más relevantes
        atributos_recuento = top_restaurants.sum(numeric_only=True)  # Asegurarse de contar solo las columnas numéricas
        atributos_ordenados = atributos_recuento.sort_values(ascending=False)
        # Obtener los 10 atributos más relevantes
        top_atributos_categoria = atributos_ordenados.index.to_list()[:6]
        dicc={f'Top ciudades para la categoría {categoria}':top_ciudades_list,
            f'Top atributos para la categoría {categoria}':top_atributos_categoria}
        return dicc
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
