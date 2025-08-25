hamburguer = 20.00
cod_desconto = 'hm20'
saudacao = ("bem-vindo a key burguer :")

while True:
     produto =  input('vamos de quê hoje? ')
     if produto =='hamburguer':
         print("pedido confirmado ")
         break
     else:
          print("nao conta no cardapio tente novamente. ")
          
cupom = input("digite seu cupom")
if cupom == cod_desconto:
     print(f"seu pedido custou {hamburguer * 0.9}")
else:
     print(f"seu pedido custou {hamburguer}")
          





    