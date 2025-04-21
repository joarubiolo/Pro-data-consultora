import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model


st.title("Pro-Data: Anlisis de mercado gastronomico")

st.subheader("Modelo de Seleccion de Caracteristicas")

st.write("Elija las opciones que desee agregar para su negocio y la prediccion se arrojara automaticamente")
 
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


# Cargar el modelo entrenado
model= load_model('trained-model.h5')

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

# Mostrar la predicción redondeando el resultado a 1 digito
prediction = np.round(prediction,1)

if prediction == 1:
    st.write("🔮 La predicción de éxito del negocio es:", "✅ Positiva")
else:
    st.write("🔮 La predicción de éxito del negocio es:", "❌ Negativa")
