## Índice

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Contenido</summary>
  <ol>
    <li><a href="#Índice">Índice</a></li>
    <li><a href="#Contexto">Contexto</a></li>
    <li><a href="#Objetivo">Objetivo</a></li>
    <li><a href="#Análisis-de-Datos">Análisis de Datos</a></li>
    <ul>
      <li><a href="#Primer-EDA">Primer EDA</a></li>
      <li><a href="#Segundo-EDA">Segundo EDA</a></li>
      <li><a href="#Dashboard-Final">Dashboard Final</a></li>
    </ul>
  </ol>
</details>

## Contexto

<p align="justify">
En este proyecto, se realizó un análisis exhaustivo de los datos obtenidos de formularios de Google con el fin de extraer información valiosa a partir de los comentarios de los usuarios. El análisis de datos incluyó dos fases de Análisis Exploratorio de Datos (EDA) y la creación de un dashboard final para visualizar los resultados de manera interactiva.

</p>

<br/>

## Objetivo

El objetivo del análisis de datos es transformar los comentarios textuales recopilados a través de formularios de Google en información estructurada y comprensible, que permita identificar tendencias, patrones y sentimientos expresados por los usuarios. Esto facilita la toma de decisiones basada en datos y mejora la comprensión de la retroalimentación de los usuarios.

<br/>

## Análisis de Datos

### **`Primer EDA`**

En el primer Análisis Exploratorio de Datos (EDA), se analizó el archivo CSV extraído de los formularios de Google para entender la estructura y el contenido de los datos. Este análisis incluyó:

#### **`Descripcion de los datos`**

- Se generaron estadísticas descriptivas básicas de las variables, como la distribución de respuestas segun la carrera que estuviera cursando el usuario, de igual forma en relacion con el semestre y la edad. Ademas de la identificación de valores faltantes, identificacion de valores duplicados y una visualizacion basica de las palabras clave contenidas dentro de los comentarios.

#### **`Visualización de Datos:`**

- Se crearon gráficos de barras y diagramas de torta para visualizar la distribución de las respuestas en categorías como carrera, semestre y edad.
- Se utilizaron histogramas para analizar la distribución de variables cuantitativas.
- Se Utilizo un grafico con estilo word cloud para generar la visualizacion de las caracteristicas contenidas dentro de los comentarios.

#### **`Limpieza de Datos::`**

- Al ser un analisis tan prematuro en terminos del desarrollo del proyecto, no se realizo una limpieza significativa a los datos a nalizados puesto que no se considero necesario, mas sin embargo, la experiencia obtenida dentro de este proceso de analisis se aplico durante las limpiezas a los datos hechas en el proceso de ETL

### **`Segundo EDA`**

El segundo EDA se llevó a cabo después de aplicar el análisis de sentimientos a los comentarios. Este análisis incluyó:

#### **`Descripción de los Datos con Sentimientos:`**

- Se agregó la nueva columna que refleja los sentimientos (positivo, negativo, neutral) de cada comentario.
- Se generaron estadísticas descriptivas de las nuevas variables, incluyendo la distribución de los sentimientos.

#### **`Visualización de Sentimientos:`**

- Se crearon gráficos de barras y pastel para visualizar la proporción de sentimientos en los comentarios.
- Se realizaron análisis de correlación para explorar relaciones entre características demográficas y sentimientos.

#### **`Insights Clave:`**

- Se identificaron patrones y tendencias significativas en los comentarios.
- Se destacaron áreas con mayor feedback positivo o negativo, proporcionando información útil para la toma de decisiones.

## Dashboard Final

Para facilitar la visualización y el análisis continuo de los datos, se desarrolló un dashboard interactivo. Este dashboard incluye:

#### **`Filtros Interactivos:`**

- Permiten a los usuarios filtrar los datos por variables demográficas como carrera, semestre y edad.
- Ofrecen la posibilidad de seleccionar el tipo de percepción (Positiva, negativa o neutral) para tener un rapido acceso a la data general de la percepción deseada.

#### **`Gráficos Dinámicos:`**

- Visualizaciones dinámicas que muestran la evolución de los sentimientos a lo largo del tiempo y en diferentes categorías.
- Gráficos de barras y tablas para proporcionar una visión comprensiva de los datos.

#### **`Acceso a Datos en Tiempo Real:`**

- El dashboard se actualiza automáticamente con los datos más recientes extraídos y analizados.
- Proporciona información actualizada y relevante para la toma de decisiones basada en datos.

Este enfoque integral del análisis de datos asegura que se obtenga una comprensión profunda y detallada de los comentarios de los usuarios, facilitando la identificación de tendencias y áreas de mejora.
