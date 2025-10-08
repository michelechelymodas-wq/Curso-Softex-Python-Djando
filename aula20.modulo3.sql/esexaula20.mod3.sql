create table autores ( 
    id integer PRIMARY KEY ,
    autor_nome text not null, 
    nacionalidade text not null
    );
DROP TABLE autores;
 create table livros ( 
    id_livros integer PRIMARY KEY ,
    titulo text not null, 
    ano_publicado text not null, 
    id_autor text not null
    );   
DROP TABLE livros;
INSERT INTO autores(autor_nome, nacionalidade) VALUES('Thomaz Joy', 'Americano'), ('Bruno Monteiro', 'Brasileira');
SELECT * FROM autores;
INSERT INTO livros(titulo, ano_publicado, id_autor) VALUES('Jesus Copy', 2002, 1),('Obedecer é melhor que sacrificar', 2010,2);
SELECT * FROM livros;
