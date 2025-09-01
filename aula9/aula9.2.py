lista1 = ["vermelho", "azul", "verde", "amarelo"]
lista2 = ["verde", "roxo", "azul", "preto"]
lista_em_comum = []

for item  in lista1:
    if item in lista2:
        lista_em_comum.append(item)


print(lista_em_comum)
