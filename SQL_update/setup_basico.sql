use datacam;
INSERT INTO camaras (FQHN,ubicacion) VALUES ("DONVEGA.CAM36","Baño");
INSERT INTO bots (id,nombre,token,descripcion) VALUES (1,"test_bot","1412544928:AAERoGWd3jwaLt9RpduLScw4ToyNIdCPkVE","Bot de pruebas");
INSERT INTO empresas (id,codigo,nombre,bot_id) VALUES (1,1,"Hassan S.A",1);
INSERT INTO usuarios (nombre,id_chat,telefono,mail,avanzado,empresa_id) VALUES ("Hassan",1381883495,1123,"Hm64@gmail.com",true,1);
INSERT INTO camaras_usuarios (camara_id,usuario_id) VALUES (1,1);


