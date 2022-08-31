drop database sistema_camaras;
create database sistema_camaras;

use sistema_camaras;

CREATE TABLE usuarios(
id int  not null auto_increment,
nombre varchar (40) not null,
telefono int,
id_chat int,
primary key (id));

create table camaras (
id_camara varchar(50) not null,
id_usuario int not null,
primary key (id_camara),
foreign key (id_usuario) references usuarios(id));

create table eventos (
hora timestamp,
id int not null auto_increment,
device_id varchar(50) not null, 
attach_path varchar(200) not null,
message varchar(100),
foreign key(device_id) references camaras(id_camara),
primary key(id));

