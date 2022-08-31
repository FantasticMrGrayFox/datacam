use sistema_camaras;
ALTER TABLE camaras drop primary key;

ALTER TABLE camaras ADD id INT AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE camaras ADD constraint UNIQUE (id_camara);

CREATE TABLE camaras_usuarios (camara_id INT NOT NULL, usuario_id INT NOT NULL);
ALTER TABLE camaras_usuarios ADD CONSTRAINT UC_cam_user UNIQUE (camara_id,usuario_id);
