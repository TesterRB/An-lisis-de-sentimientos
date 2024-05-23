import spacy
from spacy.lang.es.stop_words import STOP_WORDS
import string
import re
import pandas as pd
import joblib
import os

from flask import Flask, jsonify
from google.cloud import storage

app = Flask(__name__)

nlp = spacy.load("es_core_news_sm")

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
            if temp not in app.config['stopwords'] and temp not in app.config['puntuaciones']:
                tokens_limpios.append(temp)

    return tokens_limpios

@app.route("/")
def predict_sentiments():
    clf = joblib.load("ML/nlp.plk")

    # Google Cloud Storage
    storage_client = storage.Client()
    bucket_name = "" # Nombre del bucket donde se esten almacenando los datos
    blob_name = "form_responses.csv"
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.download_to_filename("form_responses.csv")

    df_nlp = pd.read_csv("form_responses.csv")

    df_nlp['Sentimiento'] = predecir_sentimientos(df_nlp, "comentario", clf)

    storage_path = "form_responses_with_sentiment.csv"
    df_nlp.to_csv(storage_path, index=False)

    # Subir resultados a Google Cloud Storage
    blob = bucket.blob(storage_path)
    blob.upload_from_filename(storage_path)

    return jsonify({"message": "Prediction results stored in Cloud Storage."})

def predecir_sentimientos(dataframe, columna_comentarios, modelo):
    comentarios = dataframe[columna_comentarios]
    
    sentimientos_predichos = modelo.predict(comentarios)
    
    return sentimientos_predichos

if __name__ == "__main__":
    app.config['puntuaciones'] = string.punctuation + "¡¿"
    app.config['stopwords'] = set(STOP_WORDS)
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
