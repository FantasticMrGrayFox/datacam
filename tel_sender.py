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

# TOKEN _ DB USER _ DB PASWORD _ DB IP _ DB PORT _ DB NAME

# Combinamos la declaración del Token con la función de la API

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

def send_notification(media,users,bot,ext):
    tb = telebot.TeleBot(token=token, parse_mode=None)
    for each in users:
         tb.send_video(eventos[i].id_chat, media, " " , mensaje)
