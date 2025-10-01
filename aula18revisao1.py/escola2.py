'''Etapa 2: O Estudante Especializado (no arquivo estudante.py) 

Um estudante é uma pessoa, mas tem algumas características extras. Ele tem uma matrícula 
e tira notas. 
Seu trabalho aqui: 
● Crie uma classe chamada Estudante que herda (pega emprestado) todas as 
características da classe Pessoa. 
● Adicione um atributo de matrícula a esta classe. 
● Para guardar as notas, use um dicionário, onde a "chave" é o nome da matéria (como 
'Matemática') e o "valor" é uma lista de notas (ex: [9.0, 8.5]). 
● Crie um método "setter" para adicionar notas a uma matéria específica. Um "setter" é 
uma forma de definir ou alterar uma informação dentro do objeto.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Estudante(Pessoa):
     def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.matricula = matricula
        self.notas = {}
        def adicionar_nota(self, materia, nota):
            if materia not in self.notas:
                self.notas[materia]=[]
        self.notas[materia].append(materia)
               

        
