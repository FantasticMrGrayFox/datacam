import telebot # Importamos las librería
import time
import requests
import sys
import os
from configparser import ConfigParser
     ## LEYENDO LAS SETTINGS ###
parser = ConfigParser()
parser.read("configs/config_bot.ini")
token = parser.get("Settings","TOKEN")
ip_server = parser.get("Settings","IP db server")
port_server = parser.get("Settings","Port db server")
        #sys.stdout.write('This is stdout text\n')
        #print(sys.argv)
if len(sys.argv) > 1 :
    token  = sys.argv[1]
    ip_server = sys.argv[2]
    port_server = sys.argv[3]
    ### CREANDO EL ACHIVO DE GUADADO ###
    config = ConfigParser()
    config['Settings'] = {'TOKEN': token,'IP db server': ip_server,'Port db server':port_server}
    with open('config_bot.ini', 'w') as configfile:
        config.write(configfile)

#TOKEN = '1412544928:AAERoGWd3jwaLt9RpduLScw4ToyNIdCPkVE' # Ponemos nuestro Token generado con el @BotFather
tb = telebot.TeleBot(token = token, parse_mode = None) # Creamos el objeto bot pasando como parametro el token
@tb.message_handler(commands=['registro'])
def send_welcome(message):
    id_usuario = message.text.split(" ")
    URL = "http://"+ ip_server +":"+ port_server +"/update_user_chat_id/"+str(id_usuario[1])+"/"+ str(message.chat.id)
    respuesta = requests.put(url = URL)
    if str(respuesta) == "<Response [500]>":
        tb.send_message(message.chat.id,"Error intente ingresar su telefono nuevamente.Contacte con un administrador si el error persiste")
    else:
        resp = str(respuesta.text)
        respuesta = resp.replace('"',' ')
        tb.send_message(message.chat.id,respuesta)

@tb.message_handler(commands=['restart'])
def send_welcome(message):
	os.system("sudo systemctl restart datacam_app.service")
	tb.send_message(message.chat.id, "app reinciado")
	os.system("sudo systemctl restart datacam_smtp.service")
	tb.send_message(message.chat.id,"smtp receiver reninicaido")

@tb.message_handler(commands=['modo'])
def send_welcome(message):
    id_usuario = message.text.split(" ")
    URL = "http://"+ ip_server +":"+ port_server +"/update_user_mode/"+str(id_usuario[1])+"/"+ str(message.chat.id)
    respuesta = requests.put(url = URL)
    resp = str(respuesta.text)
    respuesta = resp.replace('"',' ')
    tb.send_message(message.chat.id, respuesta)

@tb.message_handler(commands=['test'])
def send_welcome(message):
	tb.send_message(message.chat.id, "el bot esta activo")
#@tb.message_handler(func=lambda m: True)
#def echo_all(message):
	#tb.reply_to(message, message.text)

tb.polling()

chatid = "1381883495"
#text = "hola mundo"
#photo = open('C:\TRABAJO\proyectos\pyTelegramBotAPI-master\meme.jpg', 'rb')
#tb.send_photo(chatid, photo) # Ejemplo tb.send_message('109556849', 'Hola mundo!')
