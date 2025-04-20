# Usa una imagen base con Python 3.11 (para evitar problemas con Scipy y NumPy)
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Actualiza pip y setuptools para evitar problemas con dependencias
RUN pip install --upgrade pip setuptools

# Instala las dependencias desde requirements.txt
RUN pip install -r requirements.txt

# Expone el puerto en el que corre Streamlit
EXPOSE 8080

# Comando de inicio de la aplicación
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
