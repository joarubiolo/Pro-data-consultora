import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf


st.title("Pro-Data: Anlisis de mercado gastronomico")

st.subheader("Modelo de Seleccion de Caracteristicas")


'''
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
'''

st.write("Elija las opciones que desee agregar para su negocio y la prediccion se arrojara automaticamente")

'''
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
'''
 
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


'''# crear cliente de storage
storage = storage.Client()
bucket = storage.bucket("ml_databases")
blob = bucket.blob("trained_model.h5")
blob.download_to_filename("trained_model.h5")'''

# Cargar el modelo entrenado
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

# Mostrar la predicción redondeando el resultado a 1 digito
prediction = np.round(prediction,1)

if prediction == 1:
    st.write("🔮 La predicción de éxito del negocio es:", "✅ Positiva")
else:
    st.write("🔮 La predicción de éxito del negocio es:", "❌ Negativa")
