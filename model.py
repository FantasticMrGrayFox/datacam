from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from flask import Flask

#Base = declarative_base()
#app = Flask(__name__)
#api = Api(app)
#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@127.0.0.1:3306/Sistema_Camaras'
db = SQLAlchemy()

cams_users = db.Table('camaras_usuarios',
    Column("usuario_id", Integer, ForeignKey('usuarios.id')),
    Column("camara_id", Integer, ForeignKey('camaras.id')),
)

class User(db.Model):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key = True, autoincrement = True)
    username = Column('nombre', String)
    id_chat = Column("id_chat", Integer)
    telefono = Column('telefono', String)
    email = Column("mail", String(20))
    avanzado = Column("avanzado", db.Boolean)
    id_empresa = Column("empresa_id", Integer, db.ForeignKey('empresas.id'))
    #empresa = db.relationship("Empresas", backref = "user")
    relacion = db.relationship("Cams", secondary= cams_users, backref = "usuarios")

class Cams(db.Model):
    __tablename__ = "camaras"
    id = Column("id", Integer, primary_key = True, autoincrement = True)
    FQHN = Column("FQHN", String(50))
    ubicacion = Column("ubicacion", String(50))
    nombre = Column("nombre", String(50))
    tarpit = Column("tarpit", Integer)
    eventos_de_camara = db.relationship("Events", backref = "device")
    relacion = db.relationship("User", secondary= cams_users, backref = "camaras")

class Events(db.Model):
    __tablename__ = "eventos"
    id = Column("id",Integer, primary_key = True, autoincrement = True)
    hora = Column("hora",DateTime)
    device_id = Column("device_id",String(50), db.ForeignKey('camaras.FQHN'))
    attach_path = Column("attach_path", String(100))
    image_length = Column("image_size", String(100), default = 0)
    repetidas = Column("repeated", Integer, default = 0)
    spameos = Column("discarded", Integer, default = 0)
    hora_confirmacion = Column("telegram_sent", DateTime, default = 0)
    respuesta = Column("telegram_result", String(10), default = 0)
    
    #message = Column("message",String(100))

class Empresas(db.Model):
    __tablename__="empresas"
    id = Column("id",Integer, primary_key = True, autoincrement = True)
    codigo = Column("codigo", String(50))
    nombre = Column("nombre", String(50))
    bot_id = Column("bot_id", Integer, db.ForeignKey('bots.id'))
    usuario_miembro = db.relationship("User",backref = "empresa")

class Bots(db.Model):
    __tablename__="bots"
    id = Column("id",Integer, primary_key = True, autoincrement = True)
    nombre = Column("nombre", String(50))
    token = Column("token", String(100))
    src_ip = Column("src_ip", String(50))
    dst_ip = Column("dst_ip", String(50))
    descripcion = Column("descripcion", String(100))
    bot = db.relationship("Empresas",backref = "bot")


#engine = create_engine('sqlite:///:memmory:', echo=True)
#engine = create_engine('sqlite:///C:\\TRABAJO\\proyectos\\camsistem_sqlalchemy\\basededatos.db', echo=True)
#Base.metadata.create_all(engine)

#Session = sessionmaker(engine)
#session = Session()

#user = User()
#user.id = 9
#user.telefono = 11455663677
#user.username ="carlos"

#cams = Cams()
#cams.id_camara = 2
#cams.id_usuario = 4

#session.add(user,cams)
#session.commit()

# camara = session.query(Cams).all()
# users = session.query(User).all()
# print("aca arranca el for")
#for user in users:
    
    #print("User whit username=%s and id=%d and telefono=%d" % (usersusername, user.id, user.telefono))

#print("aca arrancaria el 2do for")

#for cams in camara:
    #print("Camaras whit id_camara=%d and id_usuario=%d" % (cams.id_camara, id_usuario))  

#session.commit()

#session.close()
