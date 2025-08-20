pao_frances = "frances"
pao_doce = "doce"
pao_forma = "forma"

pao_frances = 1.00
pao_doce = 5.00
pao_forma = 5.99

atendente = 'Ana'

quant_frances= 20
quant_doce = 18
quant_forma = 30

bairro_barroco = "barroco"
bairro_sao_jose = "sao jose"

frete_barroco = 5.00
frete_sao_jose = 8.00


cod_vendas = 112233

while True:
    print(f"--Bem vindo a Padaria Dugil, sou atedente {atendente}")
    escolha = input(f"temos os paes: {pao_doce, pao_frances, pao_forma}.")
    if escolha == pao_frances:
        quant = int(input('qual a quant?'))
        if quant <= quant_frances:
            quant_frances -= quant
            pedido_de_paes = quant
            valor_compra = quant * pao_frances
            print(f"seu perido ficou em R$ {valor_compra}.")
        else:
            print(f"infelizmente so tenho {quant_frances} o momento!")
            break
        forma_retirada = input('e para 1: retirada ou 2: entrega?').lower()
        if forma_retirada == "2":
            bairro_entrega = input(f"qual o bairro? (1:{bairro_barroco}, 2:{bairro_sao_jose})")
            if bairro_entrega == "1":
                valor_frete = frete_barroco
                print(f"valor do frete R$ {valor_frete}")
            elif bairro_entrega == "2":
                valor_frete = frete_sao_jose
                print(f"valor do frete R$ {valor_frete}")
            else:
                

        
    

        




        