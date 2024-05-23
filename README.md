![header]("https://github.com/TesterRB/Analisis-de-sentimientos/blob/main/src/banner.png)

## Índice

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li><a href="#Índice">Índice</a></li>
    <li><a href="#Introducción">Introducción</a></li>
    <li><a href="#Objetivo">Objetivo</a></li>
    <li><a href="#Alcance">Alcance</a></li>
    <li><a href="#Tecnologías">Tecnologías utilizadas</a></li>
    <li><a href="#Pipeline">Pipeline</a></li>
    <li><a href="#Desarrolladores">Desarrolladores</a></li>
  </ol>
</details>

## Introducción

Este proyecto tiene como objetivo principal llevar a cabo un proceso de análisis y extracción, transformación y carga (ETL) de las opiniones de los usuarios de un servicio específico, con el fin de desarrollar un sistema automatizado capaz de identificar y visualizar las emociones contenidas en dichas opiniones.
El sistema propuesto aprovechará técnicas avanzadas de procesamiento del lenguaje natural (PLN) y análisis de sentimientos para desglosar y categorizar las opiniones de los usuarios en emociones claras y precisas. A través de la implementación de este sistema, se busca proporcionar a los responsables de la toma de decisiones una herramienta poderosa que permita identificar áreas de mejora, detectar patrones recurrentes en la satisfacción o insatisfacción de los usuarios, y adaptar las estrategias de servicio en función de datos reales y contundentes.

## Objetivo

El objetivo general del proyecto es proporcionar a los responsables del servicio una herramienta accesible y fácil de usar que facilite la toma de decisiones basadas en datos y opiniones de sus usuarios.

## Alcance

En cuanto al alcance del proyecto, conscientes de la gran variedad de productos y servicios que pueden beneficiarse de una herramienta como esta, decidimos enfocarnos en dos puntos importantes. Primero, implementarla y dejarla en funcionamiento para un producto específico. Segundo, asegurarnos de que la estructura sea lo suficientemente clara y flexible para que, sin importar las modificaciones que se realicen para adaptar esta herramienta a otros servicios, el flujo de los datos y la finalidad de entregar esta herramienta de análisis siga siendo la misma.

## Tecnologías

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![Looker Studio](https://img.shields.io/badge/Looker_Studio-4285F4?style=for-the-badge&logo=looker&logoColor=white)![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)![Google Colab](https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)![Deepnote](https://img.shields.io/badge/Deepnote-3793EF?style=for-the-badge&logo=deepnote&logoColor=white)![joblib](https://img.shields.io/badge/joblib-3E4EE3?style=for-the-badge&logo=joblib&logoColor=white)![Canva](https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white)

## Pipeline

![Pipeline]()

- Analisis de datos (EDA) preliminar de las respuestas del formulario: [Link diccionario](https://docs.google.com/spreadsheets/d/1E0B0LYUlOoxMaXuXUV6i2kzVYoTtiZaH/edit?usp=sharing&ouid=110626938180094444619&rtpof=true&sd=true)
- Limpieza de los datos utilizados para entrenar el modelo de machine learning - [Link Preprocesamiento](https://github.com/ksfajardo/PG-YELP-GMAPS/blob/main/ConversionArchivosParquet.ipynb)
- ETL (extracción, transformacion y carga de datos) automatizada del archivo con las respuestas del formulario desde el datalake (Google cloud storage) al data warehouse (Google Bigquery) - [Link ETL](https://github.com/ksfajardo/PG-YELP-GMAPS/tree/main/GMaps_Yelp_ETL)
- Dahsboard que proporciona una interfaz visual interactiva que permite a los usuarios analizar y visualizar los datos cargados en BigQuery. Esto es crucial para la toma de decisiones basada en datos. - [Link desarrollo Data Analytics](https://github.com/ksfajardo/PG-YELP-GMAPS/tree/main/DA)
- Desarrollo de aplicacion flask capaz de recibir una peticion POST para el uso del sistema de analisis de sentimientos en proyectos externos - [Link desarrollo de sistema de recomendación](https://github.com/ksfajardo/PG-YELP-GMAPS/tree/main/ML%20Model%20-%20API),

## Desarrolladores

Esta es la lista de desarrolladores acompañados de los links a sus perfiles de github y linkedin

- Juan David Reyes - [Linkedin](https://www.linkedin.com/in/juan-david-reyes-burbano/) - [Github](https://github.com/TesterRB)
- Marco Antonio Aragon - [Linkedin](https://www.linkedin.com/in/marco-antonio-aragon-vivas-572183289/) - [Github](https://github.com/MarcAragon)
- Daniela Marin Villacorte - [Linkedin](https://www.linkedin.com/in/daniela-mar%C3%ADn-villacorte-ab6558267/) - [Github](https://github.com/TesterRB)
- Dana Isabela Cataño - [Linkedin](https://www.linkedin.com/in/juan-david-reyes-burbano/) - [Github](https://github.com/TesterRB)
