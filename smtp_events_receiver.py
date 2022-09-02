from email.mime import image
from sqlalchemy.sql.expression import func
import smtpd
import asyncore
import email
import mimetypes
from sqlalchemy import create_engine
from sqlalchemy.orm import session,sessionmaker,relationship#import sqlAlchemy
from model import *
import os
import sys
import time
from configparser import ConfigParser
from email.policy import default
import datetime
import requests

def save_log(arg):
    f = open("logs/smtp_log.txt", "a")
    f.write(str(datetime.datetime.now()) + " " +str(arg) + "\n\n")
    f.close()
    return
i = 0
class CustomSMTPServer(smtpd.SMTPServer):
	def process_message(self, peer, mailfrom, rcpttos, data, mail_options=None, rcpt_options=None):
		try:
			i = 0
			print('Receiving message from:', peer)
			print('Message addressed from:', mailfrom)
			print('Message addressed to  :', rcpttos)
			print('Message length        :', len(data))
			event_json = {}
			event_json['hora'] = now = datetime.datetime.now()
			event_json['length'] = len(data)
			#print(now)
			device_id_correction = mailfrom.split("@")
			event_json['device_id'] = device_id_correction[0]
			event_json['clon'] = 0
			event_json['spam'] = 0
			camara = session.query(Cams).filter(Cams.FQHN == device_id_correction[0]).first()
			event = session.execute("SELECT id FROM eventos where (device_id = "+"'"+device_id_correction[0]+"'"+") ORDER BY id DESC LIMIT 1;")
			last_event = event.fetchall()
			try:
				event = session.query(Events).filter(Events.id == last_event[0][0]).first()
			except:
				event = None
			if(event != None):
				tarpit = camara.tarpit
				if(tarpit == 0):
					event.spameos = 0
					session.add(event)
					session.commit()
				if(tarpit == None):
					tarpit = 20
				if(now < event.hora + datetime.timedelta(seconds = tarpit) and camara.tarpit != 0):
					if (event.spameos == None):
						event.spameos = 0
					event.spameos = event.spameos + 1
					session.add(event)
					session.commit()
					print("Hora acutal",now,"Hora limite",event.hora +  datetime.timedelta(seconds = tarpit) )
					print("spam")
					#return
				if( int(event.image_length) == len(data)):
					event.repetidas = event.repetidas + 1
					session.add(event)
					session.commit()
					print("clon")
					#return
				event_json['spam'] = event.spameos
				event_json['clon'] = event.spameos
			msg = email.message_from_bytes(data, policy=default)
			counter = 1
			for part in msg.walk():
				# multipart/* are just containers
				if part.get_content_maintype() == 'multipart':
					continue
				# Applications should really sanitize the given filename so that an
				# email message can't be used to overwrite important files
				filename = part.get_filename()
				#ext = mimetypes.guess_extension(part.get_content_type())
				if not filename:
					ext = mimetypes.guess_extension(part.get_content_type())
					#print(ext)
					if not ext:
						ext = '.bin'
					filename = f'texto-{counter:03d}{ext}'
				else:
					if filename.endswith(".jpg") or filename.endswith(".mp4"):
						self._save_media(image = part.get_payload(decode=True),event_json = event_json,exten = filename[-4:])
				counter += 1
			self._save_event(event_json)
			return
		except Exception as Argument:
			save_log(Argument)
	def _save_media(self,image,event_json,exten):
		try:
			fechayhora=str(event_json["hora"])
			tiempo = fechayhora.replace(":","-")[:-7]
			path_wrong = image_folder + str(event_json["device_id"]) + "_" + tiempo + exten
			path = path_wrong.replace(" ","-")
			open(path, 'wb').write(image)
			imagen = str(event_json["device_id"]) + "_" + tiempo + exten
			event_json["imagepath"] = imagen.replace(" ","-")
		except Exception as Argument:
			os.system("sudo systemctl restart datacam_smtp.service")
			save_log(Argument)
	def _save_event(self,event_json):
		try:
			evento = Events()
			evento.hora = event_json['hora']
			evento.device_id = event_json['device_id']
			print(event_json['device_id'])
			evento.attach_path = event_json['imagepath']
			evento.image_length = event_json['length']
			evento.repetidas = event_json['clon']
			evento.spameos = event_json['spam']
			session.add(evento)
			session.commit()
			session.flush()
			time.sleep(1)
			url = "http://127.0.0.1:5000/event_notification/"+ str(evento.id)+"/" + event_json['imagepath']
			try:
				respuesta = requests.get(url)
			except:
				print("error conectando con app.py")
				save_log(Argument)
			No_of_files = len(os.listdir(image_folder))
			#print(No_of_files)
			if(No_of_files > 20):
				try:	
					os.chdir(image_folder)
					all_files = os.listdir()
					for f in all_files:
						os.remove(f)
				except:
					print("Fallo el proceso de vaciado de la carpeta" + image_folder + ". " +str(No_of_files) + "Archivos restantes" )
					save_log(Argument)
			session.close()
		except Exception as Argument:
			save_log(Argument)
			os.system("sudo systemctl restart datacam_smtp.service")
image_folder = ""
server_ip = ""
server_port = ""
path = ""

     ## LEYENDO LAS SETTINGS ###
parser = ConfigParser()
parser.read("configs/config_smtp.ini")
db_port = parser.get("DB Server Setting","DB_PORT")
db_ip = parser.get("DB Server Setting","DB_IP")
db_name = parser.get("DB Server Setting","DB_NAME")
db_username = parser.get("DB Server Setting","DB_UserName")
db_user_pw = parser.get("DB Server Setting","DB_PW")
server_ip  = parser.get("Server Setting","IP")
server_port = parser.get("Server Setting","PORT")
image_folder = parser.get("Image Path Setting","path")
        #sys.stdout.write('This is stdout text\n')
        #print(sys.argv)
if len(sys.argv) > 3 :
    server_ip  = sys.argv[1]
    server_port = sys.argv[2]
    db_port = sys.argv[4]
    db_ip = sys.argv[5]
    db_name = sys.argv[6]
    db_username = sys.argv[7]
    db_user_pw = sys.argv[8]
    image_folder = sys.argv[3]
    ### CREANDO EL ACHIVO DE GUADADO ###
    config = ConfigParser()
    config['SMTP Server Settings'] = {'IP': server_ip,
                      'Port': server_port,
                        }
    config['DB Server Settings'] = {'DB_NAME': db_name,'DB_UserName': db_username,'DB_PW': db_user_pw,'DB_PORT': db_port,'BD_IP': db_ip}

    config['Image Path Settings'] = {'path': path}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
try:
	db_connect = create_engine('mysql+pymysql://'+db_username+':'+db_user_pw+'@'+db_ip+':'+db_port+'/'+db_name)
	Session = sessionmaker(db_connect)
	session = Session()
except:
	print("Error Conectando con la Base de datos")
	
print("##### Systema de Recepcion de mails ##### \n IP Actual: "+ server_ip +"\n Puerto Actual: "+ server_port + "\n Directorio Actual: "+ path +"\n Nombre de La BD: "+ db_name +"\n IP de la DB: "+ db_ip +"\n Puerto de la DB: "+ db_port +"\n Usuario de la DB: "+ db_username +"\n si desea hace un cambio ingrese los demas valores en el mismo orden\n")

server = CustomSMTPServer((server_ip, int(server_port)), None)
asyncore.loop()
