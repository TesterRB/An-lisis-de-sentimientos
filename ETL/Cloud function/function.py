import os
import json
import pandas as pd
import functions_framework
from google.cloud import storage
from google.oauth2 import service_account
from googleapiclient import discovery
import base64

print("importaciones")

SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

file_content = "" # Contenido del archivo de credenciales de google cloud
try:
   file_content=base64.b64decode(file_content)
   with open("nlp-420222-3d2431be7eb9.json","w+") as f:
        f.write(file_content.decode("utf-8"))
except Exception as e:
   print(str(e))

print("credenciales")

# Configuración de Google Cloud Storage
storage_client = storage.Client.from_service_account_json("nlp-420222-3d2431be7eb9.json")
print("carga credenciales")
bucket_name = "" # Nombre del bucket donde se almacenaran los archivos

print("quemadas")

@functions_framework.http
def process_form(request):
    with open("nlp-420222-3d2431be7eb9.json", "r") as archivo:
        json_str = archivo.read()
        objeto_json= json.loads(json_str)

    print("inicio de metodo")
    creds = service_account.Credentials.from_service_account_info(objeto_json, scopes=[SCOPES])

    service = discovery.build(
        "forms", "v1", credentials=creds, discoveryServiceUrl=DISCOVERY_DOC,
        static_discovery=False,
    )

    form_id = "" # Id del formulario donde se recolectan los datos
    result = service.forms().responses().list(formId=form_id).execute()

    responses = []
    for response in result["responses"]:
        answers = {}
        for answer in response["answers"].values():
            question_id = answer["questionId"]
            text_answers = [text_answer["value"] for text_answer in answer["textAnswers"]["answers"]]
            answers[question_id] = ", ".join(text_answers)
        responses.append(answers)

    df = pd.DataFrame(responses)
    df.rename(columns={"3dea074b":"comentario",
                    "54f44b7c":"carrera",
                    "3c29115c":"autorizacion",
                    "7b94312e":"semestre",
                    "58abe8b9":"edad",
                    "240431f4":"usuario",
                    "7c52d453":"rol"}, inplace=True)
    df['comentario'] = df['comentario'].str.replace('[,"*/\n;]', '', regex=True)
    

    # Guardar el DataFrame como un archivo CSV en un bucket de Google Cloud Storage
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob("form_responses.csv")
    blob.upload_from_string(df.to_csv(index=False, encoding='utf-8'), content_type="text/csv")

    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Archivo CSV guardado en el bucket de Google Cloud Storage.'