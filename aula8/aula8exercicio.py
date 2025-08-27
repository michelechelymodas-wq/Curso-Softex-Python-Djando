numero  =input("digite de telefone com 11 digitos: ")
if not numero.isdigit() or len(numero) != 11:
              print("Erro deve conter 11 digitos numericos. ")
elif any(numero[i] == numero [i+1] == numero [i+2] for i in range(len(numero)-2)):              
     print("Erro: possui 3 ou mais digitos iguais consecutivos. ")
else:
     print(f"({numero[:2]}) {numero[2:7]}- {numero[7:]}")