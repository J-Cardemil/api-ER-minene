################################################################################################
## 0: Librerías para uso de programa  ##########################################################
################################################################################################

import json
import simplejson 
import requests as rq
import numpy as np
import time
import platform
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import os




################################################################################################
## 1: funcion de consulta consulta de punto (función de consulta, contiene lat, lon y periodo)##
################################################################################################
def api_request(llamada):
    # Funcion que realiza la llamada al api y maneja algunas excepciones que es posible que ocurran
    # ENTRADA:
    key_api = 'INSERTAR API KEY SOLICITADA'
    API_URL = 'https://api.minenergia.cl/api/proxy'
    # llamada: Dict con la configuracion de la llamada siguiendo el formato del API
    # SALIDA:
    # api_response: Dict con la respuesta del API. El contenido depende de la llamada que haya
    # 	sido realizada, por lo que el chequeo de esta info se debe realizar en el caller de esta funcion.
    # EXCEPCIONES MANEJADAS:
    # - No route to api host: Cuando no es posible realizar el request. 
    # - Sin conexion al API: engloba varios posibles errores en el lado del API. 
    # - Api no ha respondido con un JSON valido: A veces el API devuelve un string vacio. 
    # - Error en respuesta del API: Para cuando el API devuelve "server error"
    # print "Realizando peticion al API"
    llamadaJson = simplejson.dumps(llamada).encode('utf8')
    headers = {'Content-type': 'application/json', 'Accept': '*/*', "Authorization": "Token "+key_api}
    try:
        r = rq.post(API_URL, data = llamadaJson, headers=headers)
        print('Consulta OK, status:'+str(r.status_code))
        
    except Exception as inst:
        raise Exception('No route to api host: ' + API_URL + '. ' + str(inst))

    if not r.status_code == 200:
        raise Exception('SIN CONEXION AL API')
    try:
        api_response = json.loads(r.text)
    except:
        raise Exception('Api no ha respondido con un JSON valido')
    try:
        server_error = api_response['_ERROR']
        # print api_response
    except:
        return api_response
    raise Exception('Error en respuesta del API: '+str(server_error)+'. Configuracion: '+str(llamadaJson))



################################################################################################
## 2: LLAMADO DE DICCIONARIO PARA OBTENER API RESPONSE   #######################################
################################################################################################

llamado = {}

# Abrir el archivo y leer su contenido
with open('llamado.json', 'r') as archivo:
    contenido = archivo.read()

# Cargar el contenido del archivo en un diccionario
llamado = json.loads(contenido)

api_response = api_request(llamado)
print(api_response)