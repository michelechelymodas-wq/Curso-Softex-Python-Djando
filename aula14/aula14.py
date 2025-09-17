class cachorro:
    def __init__(self, nome: str, cor: str) -> None:
        self.nome = nome
        self.cor = cor

    def latir(self) -> None:
        print(f"{self.nome} diz: au, au")

       
meu_cachorro = cachorro("mel", "caramelo")
    
print(meu_cachorro.nome)
print(meu_cachorro.cor)
meu_cachorro.latir()