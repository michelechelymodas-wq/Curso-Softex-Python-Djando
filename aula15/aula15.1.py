class produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

        def get_preco(self):
            return self.__preco
        
        def set_preco(self, valor):
            if valor >=0:
                self.__preco = valor
            else:
                print("valor incorreto!")
        def _verifica_valor(self, valor):
            return valor >=0


caneta = produto("caneta azul", 2,50)
print(caneta.set_preco(-10))
print(caneta.get_preco())
