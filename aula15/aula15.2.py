class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

  
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if type(valor) is str and valor + "" :
            self._nome = valor
        else:
            print("nome invalido")
    @property
    def idade(self):
        return self._idade            

    @idade.setter