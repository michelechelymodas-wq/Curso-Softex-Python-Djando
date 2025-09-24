class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        print(f'meu nome é {self.nome} e tenho {self.idade} anos')      

    #def modo_apresentacao(pessoa):
        #pessoa.modo_apresentacao()


class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso



    def apresentacao(self):
        print(f'meu nome é {self.nome} e tenho {self.idade} anos e curso {self.curso}') 

pessoa = Pessoa("Ana", 40,)
estudante = Estudante("Joao", 33, "ingles")
lista_objetos:list[Pessoa]= [pessoa, estudante]

for objeto in lista_objetos:
    objeto.apresentacao()

        
    

        