import spacy
from spacy.lang.es.stop_words import STOP_WORDS
import string
import re
from google.cloud import storage
import pandas as pd
import importlib
import joblib
import os

nlp= spacy.load("es_core_news_sm")
def limpieza_de_datos(oracion):
    # Eliminar emojis utilizando expresiones regulares
    oracion = re.sub(r'[^\w\s,]', '', oracion)

    doc = nlp(oracion)

    tokens_limpios = []
    for token in doc:
        # Ignorar tokens de longitud uno y caracteres no alfabéticos
        if token.is_alpha and len(token.text) > 1:
            # Convertir a minúsculas y lematizar sustantivos y adjetivos
            if token.lemma_ != "-PRON-" and token.pos_ in ['NOUN', 'ADJ']:
                temp = token.lemma_.lower().strip()
            else:
                temp = token.lower_

            # Filtrar stopwords y puntuaciones
            if temp not in stopwords and temp not in puntuaciones:
                tokens_limpios.append(temp)

    return tokens_limpios

clf = joblib.load("ML/nlp.plk")

nombre_bucket = "almacen_de_archivos"
archivo_bucket = "form_responses.csv"
cliente_storage = storage.Client(project="nlp-420222")
# Obtener el bucket
bucket = cliente_storage.bucket(nombre_bucket)
archivo = "ML/files/" + archivo_bucket
blob = bucket.blob(archivo_bucket)
blob.download_to_filename(archivo)
# Leer el archivo CSV
df_nlp = pd.read_csv("ML/files/form_responses.csv")

puntuaciones = string.punctuation + "¡¿"
stopwords = set(STOP_WORDS)


def predecir_sentimientos(dataframe, columna_comentarios, modelo):
    # Obtener los comentarios de la columna especificada
    comentarios = dataframe[columna_comentarios]
    
    # Hacer predicciones de sentimientos para los comentarios
    sentimientos_predichos = modelo.predict(comentarios)
    
    # Crear un nuevo DataFrame para almacenar los resultados
    resultados = pd.DataFrame({
        'Comentario': comentarios,
        'Sentimiento_predicho': sentimientos_predichos
    })
    
    return resultados

resultados_prediccion = predecir_sentimientos(df_nlp, "3dea074b", clf)
resultados_prediccion.to_csv("resultados_prediccion.csv", index=False)

storage_path = "resultados_prediccion.csv"
blob = bucket.blob(storage_path)
blob.upload_from_filename("resultados_prediccion.csv")
print("Resultados subidos a Cloud Storage")