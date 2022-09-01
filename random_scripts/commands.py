import requests
import sys
import json
import os
accion = sys.argv[1]

if (accion == "put"):

    user_name = sys.argv[2]
    user_tel = sys.argv[3]
    URL = " http://127.0.0.1:5000/usuarios"
    payload = {"nombre": user_name,"telefono": user_tel}
    r = requests.post(URL, json = payload)
    print(r)
if(accion =="get"):
    URL = "http://127.0.0.1:5000/usuarios"
    r = requests.get(URL)
    print(r.text)
if(accion == "put"):
	URL = "http://127.0.0.1:5000/camaras"
	payload = {"id_camara": sys.argv[2],"id_usuario": sys.argv[3]}
	r = requests.put(URL, json = payload)
	print(r.text)