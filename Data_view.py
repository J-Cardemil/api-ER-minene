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

################################################################################################
##### 2: TRATAMIENTO DE DICCIONARIO A PANDAS Y CARGA DE GUI  ###################################
################################################################################################


#verificación que el llamado solcitó json como salida
if formato != 'json' :
    print("Error: archivo de llamado debe solicitar formato de exportación en JSON")
else:
    sitios = len(llamado_dict['site_info'])
    sitios_label = []
    for i in range(sitios):
        sitios_label.append(llamado_dict['site_info'][i]['label'])
    vars = len(llamado_dict['variable_info'])
    tiempo = len(llamado_dict['time'])
    vars_name = []
    for i in range(vars):
        vars_name.append(llamado_dict['variable_info'][i]['label'])
    
    #contrucción de matriz de datos: sitio, tiempo, variables
    #dict_arrange = {}

    lista_sitio = []
    lista_tiempo = []
    tupla_datos = []
    #print(dict_arrange)
    for i in range(sitios):
        for j in range(tiempo):
            lista_sitio.append(sitios_label[i])
            lista_tiempo.append(llamado_dict['time'][j])
        lista_aux = []
        for k in range(vars):
            lista_aux.append(llamado_dict['data'][k+i*vars])
        tupla_datos.append(lista_aux)
    
    print(len(tupla_datos[0]))
    
    dict_arrange = {
        'sitios' : lista_sitio,
        'tiempo': lista_tiempo,
    }       
    print(dict_arrange)
    df = pd.DataFrame(dict_arrange)
