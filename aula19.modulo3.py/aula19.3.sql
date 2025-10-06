-- Active: 1759755647519@@127.0.0.1@3306
create table usuarios ( 
    id integer PRIMARY KEY ,
    primeiro_nome text not null, 
    sobrenome text not null, 
    email text not null, 
    senha  INTEGER
    );

INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES('João', 'Rangel', 'rangel.rangel@gmail.com', 123456);
INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES('Maria','Santos', 'santos.santos@gmail,com', 654321);
INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES('Pedro', 'Silva', 'silva.silva@gmail.com', 112233);
INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES('Ana', 'Sousa', 'sousa.soua@gmail.com', 445566);
INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES('Silvia', 'Coimbra', 'coimbra.coimbra@gmail.com', 778899);

SELECT * FROM usuarios;
DELETE FROM usuarios WHERE id = 4 or id = 5 or id = 6 or id = 7 or id = 2;