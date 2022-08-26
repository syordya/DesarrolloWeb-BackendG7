create database concierto;
use concierto;
insert into participantes (id, nombre, apellido, telefono, password, zona,comentario,correo) values 
						 (default,'lily','paucar','963992129', '123', 'super_vip','holaa','lilipaucar03@gmail.com');
START TRANSACTION;
INSERT INTO participantes (id, nombre, apellido, telefono, password, zona, comentario, correo) VALUES
                        (DEFAULT, 'LUIS', 'A', '974207075', 'mimammemima','VIP', NULL, 'la@gmail.com');

INSERT INTO participantes (id, nombre, apellido, telefono, password, zona, comentario, correo) VALUES
                        (DEFAULT, 'ROBERTO', 'B', '974207075', 'mimammemima','VIP', NULL, 'rb@gmail.com');

INSERT INTO participantes (id, nombre, apellido, telefono, password, zona, comentario, correo) VALUES
                        (DEFAULT, 'ROXANA', 'C', '974207075', 'mimammemima','VIP', NULL, 'rc@gmail.com');

SELECT * FROM participantes;

UPDATE participantes set nombre = 'MARTHA' where id = 4;

SELECT * FROM participantes;

DELETE FROM participantes where ID = 100;

ROLLBACK;
SELECT * FROM participantes;