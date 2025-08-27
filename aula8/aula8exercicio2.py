

frase =  input("digite uma frase: ").lower()
frase_codificada = frase.replace("a", "1").replace("e", "2").replace("i", "3").replace("o", "4").replace("u", "5")
print("frase_codificada:", frase_codificada)
frase_descodificada = frase.replace("1", "a").replace("2", "e").replace("3", "i").replace("4", "o").replace("5", "u")
print("frase_descodificada:", frase_descodificada)

