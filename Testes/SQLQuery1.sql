CREATE DATABASE rtsystems;

USE rtsystems;

CREATE TABLE tabeventos(cadID INT PRIMARY KEY IDENTITY NOT NULL, cadNome VARCHAR(80) NOT NULL, cadDescricao VARCHAR(150) NOT NULL, cadPagamento FLOAT NOT NULL, cadNumVagas INT NOT NULL);

INSERT INTO tabeventos(cadNome, cadDescricao, cadNumVagas, cadPagamento) 
VALUES('ASP Balada 4', 'Balada localizada em Cotia, ao lado da Tabacaria Moraes', 10, 170);

SELECT * FROM tabeventos;

TRUNCATE TABLE tabeventos;

DELETE FROM tabeventos WHERE cadID=3;