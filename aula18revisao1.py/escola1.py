'''Construindo uma Mini-Escola 
Imagine que você precisa criar um pequeno sistema para organizar informações de uma 
escola. A ideia é que o computador saiba quem são as pessoas, quem são os estudantes,e o 
que eles estão aprendendo. 
Etapa 1: A Pessoa (no arquivo pessoa.py) 
Toda escola tem pessoas. Um estudante é uma pessoa, um professor é uma pessoa. Vamos 
criar um "molde" básico para qualquer pessoa. 
Seu trabalho aqui: 
● Crie uma classe (o nosso molde) chamada Pessoa. 
● Essa classe deve ter um nome e uma idade. 
● Para garantir que as informações sejam acessadas e modificadas de forma organizada, 
implemente um método "getter" para o nome. Um "getter" é uma forma de obter a 
informação de um objeto. 
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_nome(self):
        return self.get_nome
    def get_idade(self):
        return self.get_idade
        print("nome, idade")


#from pessoa import Pessoa

#p1= pessoa("Maria", 19)
#p2 = pessoa("Joao", 20)
#print(p1.get_nome(), '-', p1.get_idade(), 'anos')
#print(p2.get_nome(),'-', p2.get_idade(), 'anos')