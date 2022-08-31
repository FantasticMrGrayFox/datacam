
ALTER TABLE empresas add constraint bot_fk foreign key(bot_id) REFERENCES bots(id);

use sistema_camaras;

ALTER TABLE camaras CHANGE `id_camara` `FQHN` VARCHAR(50) CHARACTER SET latin1 COLLATE 

latin1_swedish_ci NOT NULL;
 
ALTER TABLE camaras add nombre varchar(50);

ALTER TABLE Camaras add ubicacion varchar(50);
 
ALTER TABLE usuarios add avanzado int;

ALTER TABLE camaras add tarpit int;
