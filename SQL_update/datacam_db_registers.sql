use datacam;
INSERT INTO bots() VALUES ();
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("VAJEN.CAM31",1,"INGRESO FINCA",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("VAJEN.CAM32",2,"POZO 1",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("VAJEN.CAM33",3,"CAMPO",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("VAJEN.CAM41",4,"GALPON INGRESO",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("VAJEN.CAM42",5,"GALPON INTERIOR",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("VAJEN.CAM43",6,"POZO 2",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("MAGON.CAM31",7,"FINCA INGRESO",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("MAGON.CAM33",8,"CAMPO",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("MAGON.CAM34",9,"GALPON INGRESO",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("MAGON.CAM35",10,"GALPON INTERIOR",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("KEK-C1.CAM31",11,"CAMPO 1 (Ingreso)",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("KEK-C1.CAM32",12,"CAMPO 1 (Taller)",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("KEK-C2.CAM41",13,"CAMPO 2 (Frente)",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("KEK-C2.CAM42",14,"CAMPO 2 (Taller y Maquinaria)",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("KEK-C3.CAM51",15,"CAMPO 3 (Ingreso y Galpón)",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("KEK-C3.CAM52",16,"CAMPO 3 (Pozo)",0);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("ENRICI.CAM31",17,NULL,NULL);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("DONVEGA.CAM36",18,NULL,NULL);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("DMARIA.CAM41",19,"VENTAS",40);
INSERT INTO camaras (FQHN,id,nombre,tarpit) VALUES ("DMARIA.CAM42",20,"DEPOSITO",60);

INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (1,"Josè Hugo Escobar","+5491163921447",1430461294,"josehugoescobar@hotmail.com",1,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (2,"Vìctor Hugo Escobar","+5491154270246",NULL,"victorhugoescobar@outlook.com",1,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (3,"Juan Gregorio Martinez","+5491136926125",1499672606,"juanmartinez@valledejaen.com.ar",1,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (4,"Mario Hernàn Gonzalez","+5493825666493",NULL,"maritogonzalez@hotmail.com",2,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (5,"Esteban Eduardo Enrici","+5493825676702",1317817148,"fincatierradelsol@gmail.com",3,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (6,"Lucas Martin Fonzalida","+5491162814950",263281684,"lfonzalida@lambda.net.ar",4,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (7,"Matias Arriola Silva","+5493512894866",NULL,"marriola@lambda.net.ar",4,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (8,"Adolfo Emanuel Cuevas","+5493825408050",NULL,"acuevas@lambda.net.ar",4,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (9,"Magui Herrera","+5493804350280",1470156160,"maguiherrera89@gmail.com",2,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (10,"grupo_test","123",-424592890,"test@lambda.net.ar",4,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (11,"Valle de Jaen S.A.S.","VAJAEN",-1001210736981,"",1,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (12,"Grupo DMARIA","DMARIA",-1001134686904,NULL,5,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (13,"Grupo KEK Producers","KEK-C3",-534754670,NULL,3,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (14,"Grupo KEK Producers","KEK-C2",-514472695,NULL,3,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (15,"Grupo KEK Producers","KEK-C1",-585312365,NULL,3,False);
INSERT INTO usuarios (id,nombre,telefono,id_chat,mail,empresa_id,avanzado) VALUES (16,"Grupo KEK LAMBDA","LAMBDA",-598031327,NULL,4,False);


INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (1,11);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (2,11);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (3,11);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (4,11);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (4,16);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (5,11);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (6,10);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (6,11);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (7,9);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (8,9);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (8,16);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (9,9);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (10,9);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (10,16);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (11,15);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (12,15);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (13,14);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (14,14);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (15,13);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (15,16);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (16,13);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (19,10);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (19,12);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (20,10);

INSERT INTO empresas (id,codigo,nombre,bot_id) VALUES (1,"VAJEN","Valle de Jaen S.A.",1);
INSERT INTO empresas (id,codigo,nombre,bot_id) VALUES (2,"MAGON","Mario Hernàn Gonzalez",1);
INSERT INTO empresas (id,codigo,nombre,bot_id) VALUES (3,"KEK","KEK Producers S.R.L.",1);
INSERT INTO empresas (id,codigo,nombre,bot_id) VALUES (4,"LAMBDA","Lambda S.A.",1);
INSERT INTO empresas (id,codigo,nombre,bot_id) VALUES (5,"DMARIA","D'Marìa Helados de Carmela De Marìa",1);

INSERT INTO marca (id,nombre) VALUES (1,"Vivotek");
INSERT INTO marca (id,nombre) VALUES (2,"HikVision");
INSERT INTO marca (id,nombre) VALUES (3,"Dahua");
INSERT INTO marca (id,nombre) VALUES (4,"Axis");
INSERT INTO marca (id,nombre) VALUES (5,"Bosh");

INSERT INTO modelo (id,nombre,marca_id) VALUES (1,"Generico",1);
INSERT INTO modelo (id,nombre,marca_id) VALUES (2,"Generico",2);
INSERT INTO modelo (id,nombre,marca_id) VALUES (3,"Generico",3);
INSERT INTO modelo (id,nombre,marca_id) VALUES (4,"Generico",4);
INSERT INTO modelo (id,nombre,marca_id) VALUES (5,"Generico",5);


