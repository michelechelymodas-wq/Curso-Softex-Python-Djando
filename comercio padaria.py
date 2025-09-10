'''comercio padaria
1- o programa tem que rodar em loop infinito ate ser parado
2- cliente pedir um tipo de pão (frances, doce, forma, australiano)
3- cada pao tera uma quantidade 
4- valor do pao 
5- pedir forma de pagamento (dinheiro, cartao)
6- forma de entrega 
7- dados do cliente (se for entrega)
8-valor do frete por bairro
9- nome da atendente
10- codigo da entrega'''


def dados() -> dict:
    '''carregar e retornar os dados de produtos, frete e funcionarios'''
    return{
        "atendente": "Maria", 
        "pães": { "frances": {"nome": "pao frances", "valor": 0.50, "quantidade": 15},
                 "doce": {"nome": "pao doce", "valor": 5.00, "quantidade": 20},
                 "forma": {"nome": "pao de forma", "valor": 5.99, "quantidade": 18}, 
                 "bairros":
                 "barroco":{"nome": "barroco", "frete": 5.00},
                 "sao jose": {"nome": "sao jose", "frete": 15.00},
                 "codigo_vendas_base": 95875,}

def obter_dados_cliente() -> dict:
'''solicitar e retornar os dados do clientes'''

