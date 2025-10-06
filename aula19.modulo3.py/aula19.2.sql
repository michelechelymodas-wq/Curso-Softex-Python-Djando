#criando gaveta
create table alunos ( id integer PRIMARY KEY AUTOINCREMENT, nome text not null, idade integer);

INSERT INTO alunos (nome, idade) VALUES('João', 20);
INSERT INTO alunos (nome, idade) VALUES('Maria', 22);

SELECT * FROM alunos;

SELECT * FROM alunos WHERE idade = 20;
SELECT * FROM alunos WHERE id = 2;

UPDATE alunos SET idade = 21 WHERE nome = 'João';

DELETE FROM alunos
