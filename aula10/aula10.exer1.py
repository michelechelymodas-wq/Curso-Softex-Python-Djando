vendas = [("teclado", 50, 2), ("mouse", 25.50, 4), ("monitor", 300, 1), ("fone", 45, 1), ("webcam", 75.20, 2)]

vendas_filtradas = []
produtos_unicos = set()
for produtos, valor, quantidade in vendas:
    valor_total = valor* quantidade
