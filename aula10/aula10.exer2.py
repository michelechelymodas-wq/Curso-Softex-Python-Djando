estoque_fisica = [('camisa', 101), ('calça', 102), ('boné', 103), ('tenis', 104)]
estoque_online = [('bone', 103), ('camisa polo', 105), ('calça', 102), ('chinelo', 106)]

loja_fisica = set(estoque_fisica)
loja_online = set(estoque_online)

 


estoque_fisica = loja_fisica.difference(loja_online)
estoque_online = loja_online.difference(loja_fisica)
em_ambas = loja_fisica.intersection(loja_online)
print('produtos disponiveis loja e online':)
print ('produtos disponiveis loja':)
print('produtos disponiveis online':)