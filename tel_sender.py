from fileinput import close
from urllib import response
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from pymysql import *
from model import *
from os import remove
import telebot  # Importamos las librería
import time
import datetime
import sys
import os
import glob
from configparser import ConfigParser
from sqlalchemy import create_engine, false, true
from sqlalchemy.orm import session,sessionmaker,relationship#import sqlAlchemy

image_folder = ""
server_ip = ""
server_port = ""
path = ""
## LEYENDO LAS SETTINGS ###
parser = ConfigParser()
parser.read("configs/config_app.ini")
db_port = parser.get("DB Server Setting", "DB_PORT")
db_ip = parser.get("DB Server Setting", "DB_IP")
db_name = parser.get("DB Server Setting", "DB_NAME")
db_username = parser.get("DB Server Setting", "DB_UserName")
db_user_pw = parser.get("DB Server Setting", "DB_PW")
token = parser.get("Bot Setting", "TOKEN")
search_path = parser.get("DB Server Setting", "Search_path")

#sys.stdout.write('This is stdout text\n')
# print(sys.argv)
if len(sys.argv) > 3:
    db_port = sys.argv[1]
    db_ip = sys.argv[2]
    db_name = sys.argv[3]
    db_username = sys.argv[4]
    db_user_pw = sys.argv[5]
    token = sys.argv[6]
    image_folder = sys.argv[7]
    ### CREANDO EL ACHIVO DE GUADADO ###
    config = ConfigParser()
    config['DB Server Settings'] = {
        'DB_NAME': db_name, 'DB_UserName': db_username, 'DB_PW': db_user_pw, 'DB_PORT': db_port, 'BD_IP': db_ip}
    config['Bot Setting'] = {'token': token}
    with open('config/config.ini', 'w') as configfile:
        config.write(configfile)

# TOKEN _ DB USER _ DB PASWORD _ DB IP _ DB PORT _ DB NAME

# Combinamos la declaración del Token con la función de la API
tb = telebot.TeleBot(token=token, parse_mode=None)
app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://' + \
    db_username+':'+db_user_pw+'@'+db_ip+':'+db_port+'/'+db_name
db.init_app(app)

#db_connect = create_engine('mysql+pymysql://'+db_username+':'+db_user_pw+'@'+db_ip+':'+db_port+'/'+db_name)
#Session = sessionmaker(db_connect)
#session = Session()

def save_log(arg):
    f = open("app_log.txt", "a")
    f.write(str(datetime.datetime.now()) + " " +str(arg) + "\n\n")
    f.close()
    return

def event_notification(self,id,image_path):
    try:
        path = str(search_path)+str(image_path)
        media = open(path, 'rb')
        try:
            evento = db.session.query(Events).filter_by(id = id).first()
            ##evento = Events.query.get(id)
            user = evento.device.usuarios
            TK = user[0].empresa.bot.token
            tb = telebot.TeleBot(token=TK, parse_mode=None)
            eventos = evento.device.usuarios
            camara = evento.device
            camara_FQHN = camara.FQHN
            camara_nombre = camara.nombre
        except Exception as Argument:
            save_log(Argument)
            media.close()
            #remove(path)
            return
        i = 0
        j = 0
        exito = true
        for User in eventos:
            mensaje = camara_nombre
            if eventos[i].avanzado == 1:
                mensaje = camara_FQHN
            if mensaje == None:
                mensaje = camara_FQHN
            if eventos[i].id_chat != None:
                try:
                    nombre = eventos[i].username
                    #name = nombre.split(" ")
                    if(evento.attach_path.endswith(".mp4")):
                        try:
                            # Ejemplo tb.send_message('109556849', 'Hola mundo!')
                            tb.send_video(eventos[i].id_chat, media, " " ,media)
                            print("OK")
                            evento.hora_confirmacion = datetime.datetime.now()
                            j = j + 1
                        except Exception as Argument:
                            save_log(Argument)
                            print("time out")
                            #evento.respuesta =  "Time Out " + str(j) + "/" + str(i)
                            exito = false
                            #media.close()
                            #remove(path)
                    else:
                        try:
                            #print("se intento viejo :C")
                            tb.send_photo(eventos[i].id_chat, media, mensaje)
                            print("OK")
                            evento.hora_confirmacion = datetime.datetime.now()
                            j = j + 1
                        except Exception as Argument:
                            save_log(Argument)
                            print("time out")
                            #evento.respuesta = "Time Out " + str(j) + "/" + str(i)
                            exito = false
                            #media.close()
                            #remove(path)
                except Exception as Argument:
                    save_log(Argument)
            i = i+1
        if (exito == true):
            evento.respuesta = "OK " + str(j) + "/" + str(i)
        else :
            evento.respuesta =  "Time Out " + str(j) + "/" + str(i)
        #evento.hora_confirmacion = datetime.datetime.now()
        db.session.commit()
        db.session.close()
        media.close()
        remove(path)
        No_of_files = len(os.listdir(search_path))
        print(No_of_files)
        if(No_of_files > 20):
            os.chdir(search_path)
            all_files = os.listdir()
            for f in all_files:
                os.remove(f)
        return
    except Exception as Argument:
        save_log(Argument)

def update_id_chat(self, telefono, chat):
    usuario = db.session.query(User).filter_by(telefono=telefono).first()
    #usuario = User.query.filter_by(telefono = telefono).first()
    usuario.id_chat = chat
    db.session.commit()
    return("Bienvenido a DATACAM")
    
def update_user_mode(self, modo, chat):
    usuario = db.session.query(User).filter_by(id_chat=chat).first()
    if modo == "avanzado":
        usuario.avanzado = True
        db.session.commit()
        return("Asignado como usuario Avanzado")
    if modo == "simple":
        usuario.avanzado = False
        db.session.commit()
        return("Asignado como usuario Simple")
    return("Modo desconocido, unicos modos conocidos: Avanzado,Simple")