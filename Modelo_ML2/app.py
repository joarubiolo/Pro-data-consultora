import streamlit as st
import pandas as pd
import joblib
from xgboost import XGBClassifier

import io


# Cargar modelo y datos
modelo_xgb = joblib.load("./modelo_xgb_1.pkl")


ciudad_categoria = pd.read_csv("./ciudad_categoria_procesado.csv")

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
