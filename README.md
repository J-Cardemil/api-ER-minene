# api-ER-minene
Aplicación en Python para consultar la API de Energías Renovables del Ministerio de Energía, Chile. https://api.minenergia.cl/

### Forma de uso
1. Registrarse a la herramienta online de la API deEnergías Renovables del Ministerio de Energía: https://api.minenergia.cl/register/
2. Una vez lista su cuenta, enviar un correo a soporte solitando una API_KEY, la cave que permitirá acceder a través del programa "API.py"
3. Con su "API_KEY" puede ingresarla en el código en la linea 22.

![image](https://user-images.githubusercontent.com/121578605/228037015-58b5ae67-f4bd-4ac9-9524-f70a5508ed78.png)

4. Una vez ingresada la API_KEY puede ejecutar el programa que llamará al archivo JSON de ejemplo, que se puede modificar dentro de la misma API. 
5. Si desea re-emplazar el archivo JSON de ejemplo puede obtener otra estructura a gusto de la misma API: https://api.minenergia.cl/api/ en la sección Editor completo.

![image](https://user-images.githubusercontent.com/121578605/228028030-d24d5cd4-7a82-4bd5-a098-459e86b54e36.png)

## Uso de la API y Extracción de un archivo JSON

Una vez dentro de la API, se pueden seleccionar de manera interactiva el o los puntos a evaluar.

![image](https://user-images.githubusercontent.com/121578605/228037622-2dbe099e-e469-4e43-91d8-11796d355919.png)

También es posible agregar los sitios definidos en un archivo del formato CSV o KMZ, siguiendo las instrucciónes proporcionadas en la pestaña "Subir Sitios".

> **HINT: Es importante destacar que no se deben solictar más de 20 puntos simultaneamente, ya que el ancho de banda del servidor podría generar una falla y no entregar una respuesta. Para llamados masivos de más de 20 solicitudes es recomendable contactar al soporte de los Exploradores.**

Luego, se pueden seleccionar las variables a consultar para cada uno de los puntos seleccionados. 

![image](https://user-images.githubusercontent.com/121578605/228038408-a87b1ad4-f4fa-4d52-8367-326aaf3dbe70.png)

> **Mayor información sobre las variables disponibles en la API se encuentran en la última sección del README.md**

Con la información de variables se puede pasar al Paso 4, donde se describe el periodo de tiempo a consultar. Por defecto, se define el periodo como el año 2010 completo, que corresponde al periodo de simulación del modelo WRF. Sin embargo, se puede escoger cualquier periodo dentro del rango 1980 a 2017.

Con el periodo definido, en el paso 5, se puede definir el tipo de operación a relizar a la serie de tiempo (anual, mensual, diaria u horaria) y si desea incluir la estadística de año típico meteorológico (permite estimar los espacios de la serie de tiempo sin información con un año típicio meteorológico). Se puede seleccionar un estadistico a las variables, como: promedio, media, máxima o mínima. 

Con toda esta información se puede psar al ultimo paso donde se selecciona la forma de exportación de los datos. En este punto es donde se puede extraer el llamao en JSON para ser utilizado por el programa "API.py". Con este programa se pueden editar directamente parámetros del formato JSON extraído, lo que permite mayor dinámica en la consulta.

### Archivos que se pueden exportar
La API de Energías renovables permite extraer los datos solicitados en diversos formatos: 
1. JSON
2. Excel: .xlsx
3. CSV
4. Archivo de MATLAB

## Uso del visor Data_view.py

Se puede cargar la consulta directamente al Archivo Data_view.py, en la linea 26.
![image](https://user-images.githubusercontent.com/121578605/228936026-759daef7-df92-4a46-a66b-6b45cea6e645.png)

Ejecutando el archivo, si todo es correcto, debería ejecutar Pandas GUI: un panel interactivo para analizar los datos. Se debería ver de la siguiente manera:

![image](https://user-images.githubusercontent.com/121578605/228937258-4997a3b8-48f5-46ab-86ff-2cbc73355f5c.png)

Se puede graficar los datos por cada sitio en el menu superior donde indica "Grapher":

![image](https://user-images.githubusercontent.com/121578605/228937706-6c3ff64f-53f8-4a24-bbac-231df39b0fe3.png)

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
