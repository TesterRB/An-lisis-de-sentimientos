# Usa la imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias de Python
RUN pip install --no-cache-dir spacy pandas google-cloud-storage scikit-learn

# Descarga el modelo de spacy en español
RUN python -m spacy download es_core_news_sm

# Expone el puerto si es necesario
# EXPOSE 8080

# Ejecuta el script de Python
CMD ["python", "start_ml.py"]