class circulo:
    def __init__(self, raio:int):
        self.raio = raio

    @property
    def raio(self) -> int:
        return self._raio
    
    @raio.setter
    def raio(self,novo_raio:int) ->None:
        if novo_raio >0 and isinstance(novo_raio, int):
            self._raio = novo_raio
        else:
            print("valor invalido")
    def calcular_area(self) -> float:
        area = pi * self.raio **2
        return (area)
    
roda = circulo(2)
print(roda.raio)
roda.raio = -3
roda.calcular_area()

           