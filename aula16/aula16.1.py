class animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def som(self):
        print(" 'auau!' -metodo da super")

class cachorro(animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

cao = cachorro("rex", 4, "vira-lata")
print(cao.nome)
print(cao.idade)
print(cao.raca)
cao.som()
        