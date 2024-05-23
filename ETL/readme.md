## Índice

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Contenido</summary>
  <ol>
    <li><a href="#Índice">Índice</a></li>
    <li><a href="#Contexto">Contexto</a></li>
    <li><a href="#Objetivo">Objetivo</a></li>
    <li><a href="#Alcance">Alcance</a></li>
  </ol>
</details>

## Contexto

<p align="justify">
El proceso de Extracción, Transformación y Carga (ETL) en este proyecto se encarga de recopilar datos de formularios de Google, analizar los comentarios obtenidos utilizando técnicas de procesamiento de lenguaje natural (NLP), y almacenar los resultados en un repositorio accesible para su posterior análisis. Este flujo de trabajo está compuesto por dos partes principales: Una Cloud Function encargada de la extracción inicial de datos, y una aplicación Flask cargada en Cloud Run que realiza el análisis de sentimientos.

</p>

<br/>

## Objetivo

El objetivo del proceso de ETL es automatizar la obtención y análisis de datos provenientes de formularios de Google, con el fin de proporcionar información útil sobre los comentarios recibidos. Esto permite identificar tendencias, patrones y sentimientos expresados por los usuarios, lo que facilita la toma de decisiones basadas en datos.

<br/>

## Alcance

El alcance del proceso de ETL es flexible y adaptable, ya que la solución planteada, en particular el modelo de clasificación de sentimientos aplicado en la fase de análisis, es altamente escalable y puede ser empleado en diversos proyectos. Desde la extracción inicial de datos de formularios de Google hasta el análisis de sentimientos de los comentarios obtenidos, este proceso proporciona una estructura sólida para abordar diferentes necesidades de análisis de datos. Esta flexibilidad permite su aplicación en una variedad de contextos, asegurando la relevancia y utilidad del proceso en múltiples proyectos.

### **`Extracción de Datos`**

- Utilización de una Cloud Function programada con Cloud Scheduler para extraer respuestas de formularios de Google de manera automatizada.
- La Cloud Function accede a los datos utilizando la API de Google Forms y los almacena en un archivo CSV en Google Cloud Storage.

### **`Análisis de Sentimientos`**

- Desarrollo de una aplicación Flask que realiza el análisis de sentimientos de los comentarios obtenidos.
- Los comentarios se procesan utilizando técnicas de limpieza de datos y procesamiento de lenguaje natural.
- El modelo de análisis de sentimientos se aplican a los comentarios para predecir el sentimiento asociado a cada uno.
- Los resultados del análisis se almacenan en un archivo CSV en Google Cloud Storage.

### **`Dockerización e Implementación`**

- La aplicación Flask se dockeriza para garantizar su portabilidad y se carga en Container Registry de Google.
- La aplicación Flask dockerizada se despliega en Google Cloud Run para su ejecución escalable y sin servidor.

Ambas partes del proceso, la Cloud Function y la aplicación Flask, son activadas periódicamente mediante consultas GET programadas con Cloud Scheduler, lo que asegura la actualización continua de los datos y la disponibilidad de los resultados para su posterior análisis.
