################################################################################################
## 0: Librerías para uso de programa  ##########################################################
################################################################################################

import json
import simplejson 
import requests as rq

################################################################################################
## 1: funcion de consulta consulta de punto (función de consulta, contiene lat, lon y periodo)##
################################################################################################
def api_request(llamada):
    # Funcion que realiza la llamada al api y maneja algunas excepciones que es posible que ocurran
    # ENTRADA:
    key_api = '5631b3628dc180cf53c341c2739153a9a5b0401d'
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
##### 2: LLAMADO DE DICCIONARIO PARA OBTENER API RESPONSE   (NO MOFIFICAR)   ###################
################################################################################################

def llamado(archivo): 
    llamado_dict = {}
    # Abrir el archivo y leer su contenido (puede ser llamado 2 o llamado)
    with open(archivo, 'r') as docfile:
        contenido = docfile.read()

    # Cargar el contenido del archivo en un diccionario
    llamado_dict = json.loads(contenido)
    formato =llamado_dict['export']['format']
    #revisión de diccionario para ciertas restrictiones: 
    if len(llamado_dict["position"]) > 10: 
        print('Demasiados puntos en la consulta, reducir y volver a consultar')
    else:
        api_response = api_request(llamado_dict)
        print(f'Respuesta de datos OK, datos disponibles para uso en formato {formato}')
    return api_response, formato 


################################################################################################
##### 3: IMPORTAR LLAMADO JSON DE LA API   #####################################################
################################################################################################

#Solo modificar desde acá.
#archivo = 'llamado.json'
#llamado_dict, formato  = llamado(archivo)

#VERIFICACIÓN
#print(llamado_dict)


