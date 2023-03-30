################################################################################################
## 0: Librerías para uso de programa  ##########################################################
################################################################################################

import numpy as np
import pandas as pd
import datetime
import pytz

#graficos
#import plotnine as p9
#from plotnine import ggplot, aes, geom_line, geom_point, labs, theme

#gui
from pandasgui import show

#importar la función API
from API import llamado, api_request


################################################################################################
##### 1: IMPORTAR LLAMADO JSON DE LA API Y CARGA DATOS  ########################################
################################################################################################

#Solo modificar el parámetro archivo desde acá.
archivo = 'llamado4.json'
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

    lista_sitio = []
    lista_tiempo_unix = []
    tupla_datos = []
    for i in range(sitios):
        for j in range(tiempo):
            lista_sitio.append(sitios_label[i])
            lista_tiempo_unix.append(llamado_dict['time'][j])
        lista_aux = []
        for k in range(vars):
            lista_aux.append(llamado_dict['data'][k+i*vars])
        tupla_datos.append(lista_aux)
    # transformación valores UNIX de timestamp
    print(lista_tiempo_unix)
    lista_tiempo = []
    for timestamp in lista_tiempo_unix:
        date_time = datetime.datetime.fromtimestamp(timestamp, pytz.UTC)
        lista_tiempo.append(date_time.strftime('%d/%m/%Y %H:%M'))

    dict_arrange = {
        'sitios' : lista_sitio,
        'tiempo': lista_tiempo,
    }       

    for i in range(sitios):
        for j, datos_j in enumerate(tupla_datos[i]):
            nombre_columna = f'datos_{j+1}'
            if nombre_columna not in dict_arrange:
                dict_arrange[nombre_columna] = datos_j
            else:
                dict_arrange[nombre_columna].extend(datos_j) 
    
    df = pd.DataFrame(dict_arrange)
show(df)
