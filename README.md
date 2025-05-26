# api-ER-minene
Aplicación en Python para consultar la API de Energías Renovables del Ministerio de Energía, Chile. https://api.minenergia.cl/

### Forma de uso

Para utilizar `API.py`, un script de Python que interactúa con la API de Energías Renovables del Ministerio de Energía de Chile, sigue estos pasos:

1.  **Regístrate en la plataforma de la API:**
    *   Accede a [https://api.minenergia.cl/register/](https://api.minenergia.cl/register/) y completa el proceso de registro.

2.  **Solicita tu API Key:**
    *   Una vez que tu cuenta esté activa, envía un correo electrónico al soporte de la API solicitando tu `API_KEY`. Esta clave es esencial para autenticar tus solicitudes al utilizar el script `API.py`.

3.  **Configura tu API Key en el script:**
    *   Abre el archivo `API.py` en un editor de texto.
    *   Localiza la línea 22, que debería verse similar a: `API_KEY = "TU_API_KEY"`
    *   Reemplaza `"TU_API_KEY"` con la `API_KEY` que recibiste.

    ![image](https://user-images.githubusercontent.com/121578605/228037015-58b5ae67-f4bd-4ac9-9524-f70a5508ed78.png)

4.  **Ejecuta el script `API.py`:**
    *   Abre una terminal o línea de comandos.
    *   Navega hasta el directorio donde guardaste el archivo `API.py`.
    *   Ejecuta el script usando el comando: `python API.py`
    *   Por defecto, el script utilizará un archivo JSON de ejemplo para realizar una consulta. Puedes modificar este archivo JSON directamente o generar uno nuevo desde la interfaz de la API.

5.  **Personaliza tu consulta (Opcional):**
    *   Si deseas utilizar una estructura JSON diferente para tu consulta, puedes generarla desde el "Editor completo" en la plataforma de la API: [https://api.minenergia.cl/api/](https://api.minenergia.cl/api/).
    *   Una vez que hayas generado tu JSON personalizado, puedes reemplazar el contenido del archivo JSON de ejemplo que utiliza `API.py` o modificar el script para que apunte a tu nuevo archivo.

![image](https://user-images.githubusercontent.com/121578605/228028030-d24d5cd4-7a82-4bd5-a098-459e86b54e36.png)

## Guía Detallada para Montar Consultas

Para obtener datos de la API de Energías Renovables, es fundamental construir una "consulta" o "llamado" que especifique exactamente qué información necesitas. Esta consulta define los puntos geográficos, las variables de interés, el periodo temporal y cómo se deben procesar los datos. Hay dos enfoques principales para montar estas consultas para ser utilizadas con el script `API.py`:

1.  **A través de la Interfaz Web de la API (Recomendado para empezar):**
    *   La plataforma de la API ([https://api.minenergia.cl/api/](https://api.minenergia.cl/api/)) ofrece un "Editor completo" que te permite seleccionar visualmente e interactivamente los parámetros de tu consulta.
    *   **Proceso general en la interfaz web:**
        *   **Selección de Sitios:** Defines los puntos geográficos de interés, ya sea haciendo clic en un mapa o subiendo un archivo con coordenadas.
        *   **Selección de Variables:** Eliges las variables meteorológicas o energéticas que deseas (e.g., velocidad del viento, radiación solar).
        *   **Definición del Periodo:** Especificas el rango de fechas para los datos.
        *   **Operaciones y Estadísticas:** Decides la granularidad temporal (horaria, diaria, mensual) y las funciones estadísticas a aplicar (promedio, suma, etc.).
        *   **Exportación a JSON:** El paso crucial es exportar tu consulta configurada en formato JSON. Este archivo JSON es el que `API.py` utilizará.
    *   Para una guía paso a paso detallada sobre cómo usar la interfaz web para generar tu archivo JSON, consulta la sección: **"[Uso de la API y Extracción de un archivo JSON](#uso-de-la-api-y-extracción-de-un-archivo-json)"**.

2.  **Mediante la Modificación Directa de un Archivo JSON (Avanzado):**
    *   Si ya tienes un archivo JSON de una consulta previa (o un ejemplo como `llamado.json`), puedes editarlo directamente con un editor de texto para ajustar los parámetros.
    *   **Beneficios de este método:**
        *   **Precisión y Control:** Permite un ajuste fino de cada parámetro.
        *   **Eficiencia para Cambios Menores:** Ideal para modificar rápidamente coordenadas, fechas o variables sin pasar por toda la interfaz web.
        *   **Automatización:** Facilita la creación o modificación de consultas de forma programática si estás integrando `API.py` en flujos de trabajo más grandes.
        *   **Consultas Complejas:** Puede ser más sencillo definir múltiples sitios o combinaciones de variables complejas editando el JSON.
    *   Para instrucciones detalladas sobre la estructura del archivo JSON y ejemplos de modificación, consulta la sección: **"[Modificación Avanzada de Consultas JSON para `API.py`](#modificación-avanzada-de-consultas-json-para-apipy)"**.

**Consideraciones Clave al Montar tus Consultas:**

Independientemente del método que elijas, es vital entender:

*   **Las Variables Disponibles:** Familiarízate con qué datos puedes solicitar. Cada variable tiene un identificador (`id`) específico que se usa en el JSON y representa un tipo de dato particular (e.g., temperatura, velocidad del viento a cierta altura, tipo de radiación). Consulta la sección **"[Variables disponibles en la API](#variables-disponibles-en-la-api)"** para una descripción detallada de cada una.
*   **Impacto de los Parámetros:** La información que recibas dependerá directamente de cómo configures tu consulta:
    *   **Sitios seleccionados:** Determinan la ubicación geográfica de los datos.
    *   **Rango de fechas:** Define el alcance temporal.
    *   **Variables escogidas:** Especifican qué mediciones obtendrás.
    *   **Tipo de agregación (intervalo):** Afecta la resolución temporal de los resultados (e.g., datos horarios vs. promedios mensuales).

Una comprensión clara de estos elementos te permitirá construir consultas efectivas y obtener precisamente los datos que necesitas para tus análisis energéticos.

## Uso de la API y Extracción de un archivo JSON

Esta sección te guiará a través de la interfaz web de la API de Energías Renovables para generar la consulta en formato JSON que luego podrás utilizar con el script `API.py`. Sigue estos pasos en el "Editor completo" de la API ([https://api.minenergia.cl/api/](https://api.minenergia.cl/api/)):

**1. Selección de Sitios (Puntos a Evaluar):**

*   **Interactivamente en el mapa:** La forma más directa de seleccionar tus puntos de interés es haciendo clic directamente sobre el mapa en la interfaz de la API. Cada clic registrará una coordenada geográfica.
*   **Subiendo un archivo:** Alternativamente, si tienes múltiples sitios definidos, puedes usar la pestaña "Subir Sitios". Aquí podrás cargar un archivo en formato CSV (valores separados por comas) o KMZ (Google Earth) con las coordenadas de tus puntos. Sigue las instrucciones proporcionadas en dicha pestaña para el formato correcto del archivo.

![image](https://user-images.githubusercontent.com/121578605/228037622-2dbe099e-e469-4e43-91d8-11796d355919.png)

> **IMPORTANTE (Límite de Puntos):** No se deben solicitar más de 20 puntos simultáneamente. Este límite existe debido al ancho de banda del servidor, y superarlo podría generar una falla en la solicitud, impidiendo que se entregue una respuesta. Para consultas masivas que involucren más de 20 puntos, es **recomendable contactar directamente al soporte de los Exploradores** para evaluar alternativas.

**2. Selección de Variables a Consultar:**

Una vez que hayas definido los sitios de interés, el siguiente paso es seleccionar las variables meteorológicas o energéticas que deseas obtener para dichos puntos.

*   La interfaz te presentará una lista de variables disponibles, como velocidad del viento, radiación solar, temperatura, etc. Marca las casillas correspondientes a las variables que necesitas.

![image](https://user-images.githubusercontent.com/121578605/228038408-a87b1ad4-f4fa-4d52-8367-326aaf3dbe70.png)

> **Nota:** Para una descripción detallada de cada una de las variables disponibles y lo que representan, consulta la sección "**Variables disponibles en la API**" al final de este README.

**3. Definición del Periodo de Tiempo (Paso 4 en la API):**

Con los sitios y variables ya seleccionados, procederás al "Paso 4" en la interfaz de la API, donde se define el rango temporal para tu consulta.

*   Puedes especificar fechas de inicio y fin para el periodo que te interesa.
*   Por defecto, la API podría sugerir el año 2010 completo, que es relevante para ciertas simulaciones del modelo WRF.
*   Sin embargo, tienes la flexibilidad de escoger cualquier periodo dentro del rango histórico disponible, generalmente desde 1980 hasta 2017.

**4. Definición del Tipo de Operación y Estadísticas (Paso 5 en la API):**

El "Paso 5" te permite refinar aún más tu solicitud, definiendo cómo se procesarán los datos de series temporales y qué estadísticas deseas obtener.

*   **Tipo de operación en la serie de tiempo:** Puedes elegir la granularidad de los datos (anual, mensual, diaria u horaria).
*   **Año típico meteorológico:** Tienes la opción de incluir la estadística de "año típico meteorológico". Esta función es útil para estimar valores en periodos donde no hay información directa, utilizando un año meteorológico representativo.
*   **Estadísticas para las variables:** Puedes seleccionar funciones estadísticas a aplicar sobre las variables escogidas, como el promedio, la mediana, el valor máximo o el mínimo.

**5. Exportación de Datos en Formato JSON (Último Paso en la API):**

Finalmente, llegarás al último paso en la interfaz de la API, donde seleccionarás cómo deseas exportar los datos configurados.

*   **Selecciona JSON:** Para que la salida sea compatible con el script `API.py`, es crucial que en este punto elijas "JSON" como el formato de exportación. Esto generará un archivo `.json` que contiene la estructura de tu consulta.
*   El script `API.py` está diseñado para leer este archivo JSON. Además, te permite editar directamente los parámetros dentro de este archivo JSON, ofreciendo una mayor flexibilidad y dinámica para ajustar tus consultas sin necesidad de volver a la interfaz web para cada pequeño cambio.

### Archivos que se pueden exportar
Aunque para el uso con `API.py` nos enfocamos en JSON, la API de Energías Renovables permite extraer los datos solicitados en otros formatos útiles:
1. JSON (para usar con `API.py` y otras aplicaciones)
2. Excel: .xlsx (para análisis en hojas de cálculo)
3. CSV (formato de texto plano, fácil de importar)
4. Archivo de MATLAB (para usuarios de este software)

## Modificación Avanzada de Consultas JSON para `API.py`

Una vez que hayas exportado una consulta en formato JSON desde la interfaz web de la API (como se describe en la sección anterior), puedes optar por modificar este archivo JSON directamente antes de usarlo con el script `API.py`. Esta aproximación ofrece una flexibilidad y un control más granular sobre tus consultas, permitiendo ajustes rápidos o la creación de escenarios complejos que podrían ser tediosos de configurar a través de la interfaz web.

El archivo JSON (por ejemplo, `llamado.json` o el nombre que le hayas dado) tiene una estructura definida con varias claves principales:

*   **`action`**: Define la operación a realizar sobre los datos.
    *   `action`: Generalmente `"series"` para series de tiempo.
    *   `interval`: La agregación temporal de los datos. Puede ser `"hour"`, `"day"`, `"month"`, o `"year"`.
    *   `stat`: La operación estadística a aplicar. Valores comunes son `"mean"` (promedio), `"sum"` (suma), `"min"` (mínimo), `"max"` (máximo).
    *   `tmy`: Booleano (`true` o `false`) para indicar si se debe usar el Año Típico Meteorológico (Typical Meteorological Year).
*   **`period`**: Especifica el rango de fechas para la consulta.
    *   `start`: Fecha de inicio en formato `"YYYY-MM-DD"`.
    *   `end`: Fecha de fin en formato `"YYYY-MM-DD"`.
*   **`export`**: Define parámetros de exportación (generalmente no es necesario modificarlo si ya se exportó como JSON).
    *   `label`: Un nombre para la exportación.
    *   `format`: Debería ser `"json"` para ser compatible con `API.py`.
*   **`variables`**: Un arreglo (lista) de las variables a consultar. Cada variable es un objeto.
    *   `id`: El identificador único de la variable. Para saber qué `id` corresponde a cada variable (por ejemplo, "vel" para velocidad de viento, "rad_ghi" para Radiación Global Horizontal), **debes consultar la documentación de la API o la sección "Variables disponibles en la API" en este mismo README.** A menudo, los `id` son abreviaturas intuitivas.
    *   `options`: Opciones específicas de la variable.
        *   `label`: Etiqueta para la variable en la salida.
        *   `stat`: Estadística específica para esta variable si es diferente de la global en `action`.
        *   `recon`: `"on"` o `"off"` para reconstrucción de series.
        *   `hgt`: Altura (en metros) para variables como la velocidad del viento (e.g., `10`, `50`, `100`, `120`, `150`, `200`).
*   **`position`**: Un arreglo (lista) de los puntos geográficos para la consulta. Cada punto es un objeto.
    *   `label`: Un nombre o identificador para el sitio (e.g., `"S1"`, `"Punto_Interes"`).
    *   `type`: Generalmente `"point"`.
    *   `lon`: Longitud en grados decimales.
    *   `lat`: Latitud en grados decimales.

### Ejemplos de Modificación Directa del JSON

**Ejemplo 1: Cambiar las coordenadas y el nombre de un sitio**

Supongamos que tu `llamado.json` original tiene:

```json
{
  "position": [
    {
      "label": "S1",
      "type": "point",
      "lon": -70.89298248291014,
      "lat": -32.343761859867335
    }
  ]
}
```

Para consultar un nuevo sitio llamado "Planta_Solar_Norte" en las coordenadas Lon: -70.123, Lat: -23.456, modificarías la sección `position` así:

```json
{
  "position": [
    {
      "label": "Planta_Solar_Norte",
      "type": "point",
      "lon": -70.123,
      "lat": -23.456
    }
  ]
}
```

**Ejemplo 2: Cambiar el periodo de consulta y la agregación temporal**

Si tu JSON original solicita datos mensuales para 2010:

```json
{
  "action": {
    "action": "series",
    "interval": "month",
    "stat": "mean",
    "tmy": false
  },
  "period": {
    "start": "2010-01-01",
    "end": "2010-12-31"
  }
}
```

Para obtener datos diarios para los primeros tres meses de 2015, lo cambiarías a:

```json
{
  "action": {
    "action": "series",
    "interval": "day",  // Cambiado de "month" a "day"
    "stat": "mean",
    "tmy": false
  },
  "period": {
    "start": "2015-01-01", // Año y mes cambiados
    "end": "2015-03-31"    // Año y mes cambiados
  }
}
```

**Ejemplo 3: Solicitar una variable diferente (Radiación Global Horizontal) a una altura específica para viento**

Si originalmente pedías velocidad de viento (`vel`) a 100m:

```json
{
  "variables": [
    {
      "id": "vel",
      "options": {
        "label": "Vel",
        "stat": "default",
        "recon": "off",
        "hgt": 100
      }
    }
  ]
}
```

Para solicitar Radiación Global Horizontal (supongamos que su `id` es `ghi` según la documentación) y mantener la velocidad del viento pero ahora a 80m:

```json
{
  "variables": [
    {
      "id": "vel", // Mantenemos la velocidad del viento
      "options": {
        "label": "Vel_80m", // Cambiamos la etiqueta para claridad
        "stat": "default",
        "recon": "off",
        "hgt": 80 // Cambiamos la altura
      }
    },
    { // Agregamos una nueva variable
      "id": "ghi", // ID para Radiación Global Horizontal
      "options": {
        "label": "GHI",
        "stat": "default", // O la estadística que necesites
        "recon": "off" // Asumiendo que no aplica o no se desea reconstrucción
        // "hgt" no suele ser aplicable a GHI
      }
    }
  ]
}
```
*(Nota: La estructura exacta de `options` para cada `id` de variable debe ser consultada en la documentación de la API para asegurar la compatibilidad y obtener los resultados esperados.)*

### Beneficios de la Modificación Directa

*   **Eficiencia:** Realizar pequeños cambios (como ajustar coordenadas o fechas) es mucho más rápido que volver a generar la consulta desde la interfaz web.
*   **Consultas Complejas:** Puedes añadir múltiples sitios o variables con diferentes opciones de forma más estructurada.
*   **Automatización:** Si estás generando consultas mediante scripts o programas externos, puedes construir o modificar estos archivos JSON programáticamente antes de pasarlos a `API.py`.
*   **Control Preciso:** Tienes un control exacto sobre cada parámetro de la solicitud.

Al modificar el JSON, asegúrate de mantener la estructura correcta (llaves `{}` para objetos, corchetes `[]` para arreglos, comas entre elementos, y comillas dobles para claves y valores de cadena). Un JSON malformado causará errores cuando `API.py` intente procesarlo.

## Uso del visor `Data_view.py`

El script `Data_view.py` es una herramienta útil para visualizar y realizar un análisis exploratorio inicial de los datos obtenidos a través de `API.py`. Utiliza `pandasgui`, que proporciona una interfaz gráfica interactiva para trabajar con DataFrames de Pandas.

**1. Carga de Datos en `Data_view.py`:**

Para cargar tus datos en el visor, necesitas especificar el nombre del archivo JSON que contiene la respuesta de la API.

*   **Modificar el script:** Abre el archivo `Data_view.py` con un editor de texto.
*   **Localiza la línea de carga de archivo:** Alrededor de la línea 24, encontrarás una línea similar a:
    ```python
    archivo = 'llamado4.json' 
    ```
*   **Actualiza el nombre del archivo:** Cambia `'llamado4.json'` por el nombre exacto de tu archivo JSON (el que generaste con `API.py` o modificaste). Por ejemplo, si tu archivo se llama `mis_datos_solares.json`, la línea debería quedar:
    ```python
    archivo = 'mis_datos_solares.json'
    ```
    Asegúrate de que este archivo JSON se encuentre en el mismo directorio que `Data_view.py`, o proporciona la ruta completa al archivo.

    *(La imagen anterior que mostraba la línea 26 es una referencia visual; la línea exacta puede variar ligeramente si el código ha tenido pequeños cambios, pero siempre buscarás la asignación a la variable `archivo`.)*

**2. Ejecución del Visor:**

Una vez que hayas configurado el archivo JSON correcto:

*   Abre una terminal o línea de comandos.
*   Navega hasta el directorio donde guardaste `Data_view.py` y tu archivo JSON.
*   Ejecuta el script usando el comando: `python Data_view.py`

Si todo es correcto, se abrirá la interfaz de Pandas GUI mostrando tus datos.

**3. Funcionalidades de Pandas GUI para Análisis de Datos:**

La interfaz de Pandas GUI te permite interactuar con tus datos de diversas maneras:

*   **Visualización del DataFrame:** La vista principal muestra tus datos en un formato tabular, similar a una hoja de cálculo. Puedes desplazarte y examinar los valores directamente.
    ![image](https://user-images.githubusercontent.com/121578605/228937258-4997a3b8-48f5-46ab-86ff-2cbc73355f5c.png)
*   **Filtrado de Datos (Querying):**
    *   Puedes aplicar filtros para seleccionar subconjuntos de tus datos. Busca la pestaña o sección "Query" o "Filtro".
    *   Se utiliza una sintaxis similar a las consultas de Pandas. Por ejemplo, para ver datos solo del sitio 'S1', podrías escribir `sitios == "S1"`.
*   **Ordenamiento de Datos:**
    *   Haz clic en el encabezado de cualquier columna para ordenar los datos en orden ascendente o descendente según esa columna. Esto es útil para encontrar valores máximos o mínimos rápidamente.
*   **Estadísticas Descriptivas (Summary Statistics):**
    *   Pandas GUI a menudo incluye una pestaña o sección "Statistics" o "Resumen" que muestra estadísticas descriptivas básicas para las columnas numéricas (como media, mediana, desviación estándar, mínimo, máximo).
*   **Graficación (Grapher):**
    *   La pestaña "Grapher" (Graficador) es una herramienta poderosa para la visualización.
        ![image](https://user-images.githubusercontent.com/121578605/228937706-6c3ff64f-53f8-4a24-bbac-231df39b0fe3.png)
    *   Puedes crear diversos tipos de gráficos, seleccionando las variables para los ejes X e Y, y opcionalmente agrupando por otras columnas:
        *   **Gráficos de Líneas:** Ideales para visualizar series temporales (por ejemplo, la radiación solar a lo largo del tiempo).
        *   **Gráficos de Dispersión (Scatter Plots):** Útiles para ver la relación entre dos variables numéricas.
        *   **Histogramas:** Para entender la distribución de una variable numérica.
        *   **Gráficos de Barras:** Para comparar valores entre diferentes categorías.
        *   (La disponibilidad exacta de tipos de gráficos puede depender de la versión de `pandasgui`).

**4. Ejemplo de Tarea Analítica:**

Supongamos que tu archivo JSON cargado contiene datos de velocidad del viento (`datos_Vel`) y la etiqueta del sitio (`sitios`) para varios puntos y quieres comparar la velocidad del viento a lo largo del tiempo para dos sitios específicos, "Torre_A" y "Torre_B".

1.  **Carga los datos:** Asegúrate de que `Data_view.py` apunte al archivo JSON correcto y ejecútalo.
2.  **Filtra los datos (Opcional, pero útil para claridad):**
    *   Ve a la sección de "Query" o "Filtro".
    *   Introduce una condición como: `sitios == "Torre_A" or sitios == "Torre_B"` y aplica el filtro. Esto limitará el DataFrame solo a los datos de estos dos sitios.
3.  **Usa el Graficador:**
    *   Ve a la pestaña "Grapher".
    *   Selecciona la columna de tiempo (por ejemplo, `tiempo`) para el eje X.
    *   Selecciona la columna de velocidad del viento (por ejemplo, `datos_Vel`) para el eje Y.
    *   Busca una opción para "agrupar por" o "color por" y selecciona la columna `sitios`.
    *   Elige un gráfico de líneas.
    *   Esto debería generar un gráfico con dos líneas, una para cada sitio, mostrando cómo varía su velocidad de viento a lo largo del tiempo, permitiéndote una comparación visual directa.

Otro ejemplo: Para encontrar la temperatura máxima (`datos_Temp`) registrada para el sitio "S3":

1.  **Filtra por sitio:** En "Query", introduce `sitios == "S3"`.
2.  **Ordena por temperatura:** Haz clic en el encabezado de la columna `datos_Temp` para ordenarla en forma descendente. El primer valor en la tabla será la temperatura máxima para ese sitio. Alternativamente, revisa la pestaña de "Statistics" para la columna `datos_Temp` después de filtrar.

`Data_view.py` y `pandasgui` ofrecen una forma accesible de realizar una primera exploración de tus datos energéticos antes de pasar a análisis más profundos con scripts de Python y librerías como Pandas y Matplotlib/Seaborn directamente.

## Guía para el Análisis de Datos con `Data_view.py`

Una vez que hayas cargado tus datos en `Data_view.py` (consulta la sección **"[Uso del visor `Data_view.py`](#uso-del-visor-data_viewpy)"** para las instrucciones de carga), puedes comenzar a explorar y analizar la información energética que has recuperado. La interfaz de Pandas GUI que utiliza `Data_view.py` ofrece herramientas visuales para una primera aproximación al análisis.

**Posibles Flujos de Trabajo y Tipos de Análisis:**

Aquí te sugerimos algunas formas comunes en las que puedes analizar tus datos utilizando las funcionalidades de `Data_view.py`:

1.  **Análisis de Series Temporales:**
    *   **Objetivo:** Observar cómo cambian ciertas variables a lo largo del tiempo para un sitio específico.
    *   **Cómo hacerlo:**
        *   Filtra los datos para el sitio de interés usando la función "Query" (e.g., `sitios == "Mi_Parque_Eolico"`).
        *   Utiliza el "Grapher" para crear un gráfico de líneas.
        *   Selecciona la columna de tiempo (`tiempo`) para el eje X.
        *   Selecciona la variable de interés (e.g., `datos_Vel` para velocidad de viento, `datos_GHI` para Radiación Global Horizontal) para el eje Y.
    *   **Interpretación:** Busca tendencias (aumento, disminución), estacionalidad (patrones que se repiten anualmente/mensualmente), o eventos anómalos.

2.  **Análisis Comparativo entre Sitios:**
    *   **Objetivo:** Comparar el rendimiento o las condiciones entre diferentes ubicaciones.
    *   **Cómo hacerlo:**
        *   Filtra los datos para incluir los sitios que quieres comparar (e.g., `sitios == "Sitio_A" or sitios == "Sitio_B"`).
        *   En el "Grapher", crea un gráfico de líneas o de barras.
        *   Eje X: `tiempo` (para series temporales) o nombres de los sitios (si comparas un valor agregado).
        *   Eje Y: La variable a comparar (e.g., `datos_WG_Power` para Potencia de Aerogenerador, `datos_PV_Power` para Potencia Sistema Fotovoltaico).
        *   Usa la opción de agrupar por la columna `sitios` (a menudo seleccionando un color diferente para cada sitio en gráficos de líneas).
    *   **Interpretación:** Identifica qué sitios tienen mayor potencial, producción o exposición a ciertos recursos.

3.  **Detección Visual de Correlaciones:**
    *   **Objetivo:** Inspeccionar visualmente si existe una relación potencial entre dos variables.
    *   **Cómo hacerlo:**
        *   Utiliza el "Grapher" para crear un gráfico de dispersión (Scatter Plot).
        *   Selecciona una variable para el eje X (e.g., `datos_Temp` para Temperatura en 2m).
        *   Selecciona otra variable para el eje Y (e.g., `datos_RH` para Humedad relativa, o `datos_Vel` vs `datos_WG_Power`).
    *   **Interpretación:** Observa si los puntos tienden a agruparse siguiendo un patrón (lineal, curvo). Esto no prueba causalidad, pero puede sugerir relaciones para investigar más a fondo. Por ejemplo, ¿tiende a aumentar la potencia del aerogenerador cuando aumenta la velocidad del viento?

4.  **Análisis de Distribución de Variables:**
    *   **Objetivo:** Entender cómo se distribuyen los valores de una variable particular.
    *   **Cómo hacerlo:**
        *   Utiliza el "Grapher" para crear un histograma.
        *   Selecciona la variable de interés (e.g., `datos_PV_Power` para Potencia Sistema Fotovoltaico, `datos_Vel` para Velocidad de viento).
    *   **Interpretación:** Observa la forma de la distribución. ¿Es simétrica? ¿Tiene picos? ¿Hay valores atípicos? Esto te da una idea de la frecuencia de diferentes niveles de la variable (e.g., ¿con qué frecuencia la potencia fotovoltaica alcanza su máximo?).

**Interpretando Variables Clave (Consulta "[Variables disponibles en la API](#variables-disponibles-en-la-api)" para una lista completa):**

*   **`Velocidad de viento` (e.g., `datos_Vel`):**
    *   **A diferentes alturas (`hgt` en la consulta JSON):** El viento suele ser más fuerte y constante a mayor altura. Analizar esto es crucial para determinar la altura óptima de las turbinas eólicas.
    *   **Relación con `Potencia de Aerogenerador` (`datos_WG_Power`):** Esperarías una correlación positiva fuerte. La potencia generada aumenta con la velocidad del viento hasta alcanzar la potencia nominal de la turbina, luego puede estabilizarse o incluso disminuir a velocidades muy altas (parada por seguridad).
*   **`Radiación Global Horizontal` (e.g., `datos_GHI`):**
    *   Un valor alto de GHI implica una mayor cantidad de energía solar llegando a la superficie. Es un indicador clave del potencial de generación de energía solar fotovoltaica. Compara GHI entre sitios para evaluar su idoneidad solar.
*   **`Temperatura en 2m` (`datos_Temp`):**
    *   Puede influir en la eficiencia de algunos componentes (e.g., paneles fotovoltaicos, cuya eficiencia tiende a disminuir con temperaturas muy altas).
    *   Su correlación con la demanda energética también puede ser de interés.
*   **`Presencia Nubes` y `Presencia de Sombras`:**
    *   Estos son factores booleanos (verdadero/falso) que pueden explicar caídas en la radiación solar y, por ende, en la producción fotovoltaica.

**Para Análisis Más Avanzados:**

Si bien `Data_view.py` es excelente para una exploración inicial, para análisis estadísticos más profundos, modelado o visualizaciones personalizadas complejas, querrás llevar tus datos a entornos más potentes:

*   **Exportar desde Pandas GUI (si la funcionalidad está disponible):** Algunas versiones de Pandas GUI podrían ofrecer una opción para exportar el DataFrame visualizado (e.g., a CSV).
*   **Utilizar el archivo JSON/CSV directamente:**
    *   El script `API.py` ya guarda la respuesta de la API (a menudo en formato JSON). Puedes cargar este archivo JSON directamente en un entorno de análisis de Python como:
        *   **Jupyter Notebooks o JupyterLab:** Ideales para análisis interactivo.
        *   Utilizando librerías como **Pandas** (para manipulación de datos), **Matplotlib** y **Seaborn** (para visualización avanzada), y **SciPy/Statsmodels** (para análisis estadístico).

Esta guía te proporciona un punto de partida para transformar los datos crudos de la API en información útil. ¡La clave es experimentar con las herramientas y pensar críticamente sobre lo que los datos te están mostrando!

## Variables disponibles en la API
A continuación se muestra una descripción detallada a cada variable disponible en el API.

#### Velocidad de viento
La velocidad de viento (en metros por segundo) simulado por el modelo WRF (Weather Research and Forecasting). Se disponen datos de simulaciones realizadas para 2010 y 2015. Además, es posible acceder a datos reconstruidos para el periodo 1980 a 2017.

#### Potencia de Aerogenerador
Generación (kW) de una turbina eólica calculada a partir del viento simulado por el modelo numérico WRF

#### Dirección del viento
Dirección del viento (grados) simulado por el modelo numérico WRF

#### Temperatura en 2m
Temperatura ambiental (°C) modelada a 2m del suelo para el periodo 1980-2017

#### Humedad relativa
Humedad relativa a partir de la modelación de temperatura.

#### Evaporación
Evaporación de bandeja. Estimada con en método Penman-Montieth y calibrada con observaciones de la evaporación de bandeja de las observaciones nacionales de la DGA

#### Temperatura del suelo
Temperatura del suelo (°C) calculado a partir variables atmosféricas modeladas

#### Densidad del aire
Densidad del aire (kg/m3) simulado por el modelo WRF

#### Presión Atmosférica
Presión Atmosférica (hPa) simulada por el modelo WRF

#### Radiación Global Horizontal (WRF)
Radiación global (W/m2) que incide sobre un plano horizontal fijo, simulada por el modelo WRF

#### Radiación Global Horizontal
Radiación global (W/m2) que incide sobre un plano horizontal fijo, simulada por el modelo CLIRAD

#### Radiación Directa Normal
Radiación Directa Normalizada (W/m2) que incide sobre un plano que siempre está perpendicular al sol, simulada por el modelo CLIRAD

#### Radiación Global
Radiación global (W/m2) simulada por el modelo CLIRAD que incide sobre un plano de características definidas por el usuario

#### Radiación Directa
Radiación directa (W/m2) simulada por el modelo CLIRAD que incide sobre un plano de características definidas por el usuario

#### Radiación Difusa
Radiación difusa (W/m2) simulada por el modelo CLIRAD que incide sobre un plano de características definidas por el usuario

#### Radiación Reflejada del Suelo
Radiación reflejada del suelo (W/m2) simulada por el modelo CLIRAD que incide sobre un plano de características definidas por el usuario

#### Presencia Nubes
Presencia de Nubes (booleano) según imágenes visibles del satélite GOES

#### Presencia de Sombras
Presencia de sombras topográficas (booleano) calculado para cada sitio mediante un modelo de elevación digital del terreno de origen satelital

#### Elevación del sol
Elevación del sol (grados) con respecto al horizonte

#### Azimut del Sol
Azimut del sol (grados) respecto al Norte

#### Potencia Sistema Fotovoltaico
Generación (kW) de un sistema fotovoltaico calculada a partir de la radiación del modelo CLIRAD

#### Altura significativa
Altura significativa del Oleaje (m) corresponde a la media aritmética del tercio de olas más altas de un conjunto de olas, calculado a mediante los modelos numéricos SWAN y WWIII

#### Periodo medio
Periodo medio del Oleaje (s) es la media aritmética de los periodos del oleaje, calculado mediante los modelos numéricos SWAN y WWIII

#### Potencia de oleaje
Potencia del Oleaje (kW/m) es el flujo de energía obtenido de la relación entre Altura Significativa y Periodo Medio del oleaje, calculado mediante los modelos numéricos SWAN y WWIII
