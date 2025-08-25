posicao = 0
posicao_avancar = 1
posicao_recuar = 2
posicao_status = 3
posicao_desligar = 4


while True:
    escolha = (input("sou o robo joy, estou parado. escolha o comando para me usar:1 avancar. 2 recuar. 3 status. 4 desligar."))
    if escolha == '1':
        posicao += 1
    elif escolha == '2':
         posicao -= 1
    elif escolha == '3':
        print(posicao)
    elif escolha == '4':
        break
    else:
        print("erro!")

        
              
              
                    



