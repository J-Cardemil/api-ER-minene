################################################################################################
## 0: Librerías para uso de programa  ##########################################################
################################################################################################

import json
import simplejson 
import requests as rq
import numpy as np
import pandas as pd

#graficos
import plotnine as p9
from plotnine import ggplot, aes, geom_line, geom_point, labs, theme

#gui
from pandasgui import show

#importar la función API
from API import llamado, api_request


################################################################################################
##### 1: IMPORTAR LLAMADO JSON DE LA API Y CARGA DATOS  ########################################
################################################################################################

#Solo modificar desde acá.
archivo = 'llamado.json'
llamado_dict, formato = llamado(archivo)

#VERIFICACIÓN
#print(llamado_dict)

################################################################################################
##### 2: TRATAMIENTO DE DICCIONARIO A PANDAS Y CARGA DE GUI  ###################################
################################################################################################


#verificación que el llamado solcitó json como salida
if formato != 'json' :
    print("Error: archivo de llamado debe solicitar formato de exportación en JSON")
else:
    df = pd.DataFrame.from_dict(llamado_dict, orient='index')
    print(df.head())

#show(df)