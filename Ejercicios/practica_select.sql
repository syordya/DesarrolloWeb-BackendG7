-- Crear una tabla llamada vacunas en la cual tengamos las siguientes columnas:
-- el id que sera numerico y sera auto incrementable y primary key
-- nombre de la vacuna que sera hasta 100 characters 
-- procedencia que sera hasta 20 characters
-- lote que sera de 6 caracteres

CREATE DATABASE vacunaciones;

CREATE TABLE Vacunas(
    id INT AUTO_INCREMENT  PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    origen VARCHAR(20) NOT NULL,
    lote CHAR(6)
);

INSERT INTO vacunas(id, nombre, origen, lote) VALUES
(DEFAULT,'SPUTNIK','RUSIA','7a6bcd'),
(DEFAULT,'JHONSON & JHOSON',"USA","bbfiufiuXD"),
(DEFAULT,'ASTRAZENECA','CHINA','m5n3wert'),
(DEFAULT,'CHONOPARHM','CHINA','wantanXD345');