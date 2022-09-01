drop database datacam;
create database datacam;
use datacam;

CREATE TABLE usuarios(
id int  not null auto_increment,
nombre varchar (40) not null,
telefono varchar(30) unique key,
id_chat bigint unique,
mail varchar(50) unique key,
avanzado bool,
empresa_id int,
primary key (id),
foreign key (empresa_id) references empresas(id)
)ENGINE = MyISAM;

CREATE TABLE camaras (
FQHN VARCHAR(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
id int auto_increment,
ubicacion varchar(50),
nombre varchar(50),
tarpit int,
modelo_id int,
primary key (id),
foreign key(modelo_id) REFERENCES modelo(id)
)ENGINE = MyISAM;

CREATE TABLE eventos (
hora timestamp,
id int not null auto_increment,
device_id varchar(50) not null, 
attach_path varchar(200) not null,
message varchar(100),
telegram_result varchar(20) DEFAULT NULL,
telegram_sent TIMESTAMP NULL DEFAULT NULL,
discarded int,
repeated int,
image_size int,
foreign key(device_id) references camaras(id_camara),
primary key(id)
)ENGINE = MyISAM;
 
 CREATE TABLE camaras_usuarios (
 camara_id INT NOT NULL,
 usuario_id INT NOT NULL,
 FOREIGN KEY(camara_id) REFERENCES camara(id),
 FOREIGN KEY (usuario_id) REFERENCES usuario(id))ENGINE = MyISAM; 
 
 CREATE TABLE modelo(
 id int auto_increment,
 nombre varchar(50),
 marca_id int, primary key(id),
 foreign key(marca_id) REFERENCES marca(id))ENGINE = MyISAM;

CREATE TABLE bots (
id int auto_increment,
nombre varchar(50),
token varchar(100),
src_ip Varchar(50),
dst_ip varchar(50),
descripcion varchar(200),
primary key(id))ENGINE = MyISAM;

create table empresas (
id int, codigo varchar(30) unique key,
 nombre varchar(100),
 bot_id int,
 foreign key(bot_id) REFERENCES bots(id),
 primary key (id))ENGINE = MyISAM;
 
 CREATE TABLE marca(
 id int auto_increment,
 nombre varchar(50),
 primary key(id))ENGINE = MyISAM;

ALTER TABLE camaras ENGINE = MyISAM;

ALTER TABLE eventos ENGINE = MyISAM;

ALTER TABLE usuarios ENGINE = MyISAM;

#ALTER TABLE camaras drop primary key;

#ALTER TABLE camaras ADD id INT AUTO_INCREMENT PRIMARY KEY;

#ALTER TABLE camaras ADD constraint UNIQUE (id_camara);

#CREATE TABLE camaras_usuarios (camara_id INT NOT NULL, usuario_id INT NOT NULL);

#ALTER TABLE camaras_usuarios ADD CONSTRAINT UC_cam_user UNIQUE (camara_id,usuario_id);

#ALTER TABLE camaras drop foreign key camaras_ibfk_1;

#ALTER TABLE eventos drop foreign key eventos_ibfk_1;

#ALTER TABLE camaras drop primary key;

#ALTER TABLE camaras DROP COLUMN id_usuario;

#ALTER TABLE camaras ADD id INT AUTO_INCREMENT PRIMARY KEY;

#ALTER TABLE camaras ADD constraint UNIQUE (id_camara);

#CREATE TABLE camaras_usuarios (camara_id INT NOT NULL, usuario_id INT NOT NULL,FOREIGN KEY(camara_id) REFERENCES camara(id), FOREIGN KEY (usuario_id) REFERENCES usuario(id)) ENGINE = MyISAM; 

#ALTER TABLE camaras_usuarios ADD CONSTRAINT UC_cam_user UNIQUE (camara_id,usuario_id);  

#ALTER TABLE usuarios ADD CONSTRAINT unique_id_chat UNIQUE (id_chat);

#ALTER TABLE usuarios MODIFY COLUMN telefono varchar(20);

#ALTER TABLE usuarios add mail varchar(50) unique key;

#ALTER TABLE usuarios ADD constraint UNIQUE (telefono);

#ALTER TABLE eventos ADD CONSTRAINT eventos_ibfk_1 foreign key (device_id) REFERENCES camaras(id_camara);

#create table empresas (id int, codigo varchar(30) unique key, nombre varchar(100), primary key (id))ENGINE = MyISAM;

#ALTER TABLE usuarios ADD empresa_id int;

#ALTER TABLE usuarios add constraint user_emp_fk1 foreign key (empresa_id) references empresas(id);

#CREATE TABLE marca(id int auto_increment, nombre varchar(50), primary key(id));

#CREATE TABLE modelo(id int auto_increment, nombre varchar(50),marca_id int, primary key(id), foreign key(marca_id) REFERENCES marca(id));

#ALTER TABLE camaras add column modelo_id int;
 
#ALTER TABLE camaras add constraint model_fk foreign key(modelo_id) REFERENCES modelo(id);

#CREATE TABLE bots (id int auto_increment,nombre varchar(50),token varchar(100),src_ip Varchar(50),dst_ip varchar(50),descripcion varchar(200), primary key(id));

#ALTER TABLE empresas add column bot_id int;

#ALTER TABLE empresas add constraint bot_fk foreign key(bot_id) REFERENCES bots(id);

#ALTER TABLE camaras CHANGE `id_camara` `FQHN` VARCHAR(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL;
 
#ALTER TABLE camaras add nombre varchar(50);

#ALTER TABLE Camaras add ubicacion varchar(50);
 
#ALTER TABLE empresas add constraint bot_fk foreign key(bot_id) REFERENCES bots(id);

#ALTER TABLE camaras CHANGE `id_camara` `FQHN` VARCHAR(50) CHARACTER SET latin1 COLLATE 

#latin1_swedish_ci NOT NULL;
 
#ALTER TABLE camaras add nombre varchar(50);

#ALTER TABLE Camaras add ubicacion varchar(50);

#ALTER TABLE eventos ADD telegram_sent TIMESTAMP NULL DEFAULT NULL;

#ALTER TABLE eventos add telegram_result varchar(20) DEFAULT NULL;

