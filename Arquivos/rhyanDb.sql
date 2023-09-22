CREATE DATABASE rhyanDb;

USE rhyanDb;

#Criação de Tabelas
CREATE TABLE tabUsers(
usrId INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
usrNome VARCHAR(80) NOT NULL, 
usrEmail VARCHAR(80) NOT NULL,
usrSenha VARCHAR(80) NOT NULL,
usrStatus INT NOT NULL,
usrAdm INT NOT NULL
);


#Vizualização de dados
SELECT * FROM tabUsers;


#CRUD
INSERT INTO tabUsers VALUES(null, "Rhyan Lucca Borges", "brhyanlucca@gamil.com", "rhyanlucca", 1, 1);
INSERT INTO tabUsers VALUES(null, "Rhyan Lucca Borges Galdino", "brhyanlucca@gmail.com", "rhyanlucca", 1, 1);
INSERT INTO tabUsers VALUES(null, "Isabella Martins de Sousa", "isabellamartins@gmail.com", "rhyanlucca", 1, 0);
INSERT INTO tabUsers VALUES(null, "Isabella Martins", "isabellamartins@gmail.com", "rhyanlucca", 1, 1);