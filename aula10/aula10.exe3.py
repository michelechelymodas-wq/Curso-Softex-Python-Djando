acesso = [('Pedro', 'sucesso'), ('Ana', 'falha'), ('Maria', 'sucesso'), ('pedro', 'falha'), ('Ana', 'falha')]
usuario_sucesso = set()
usuario_falha = set()
for usuario, status in acesso:
    if status == 'sucesso':
        usuario_sucesso.add(usuario)
    elif status == 'falha':
        usuario_falha.add(usuario)
somente_falha = usuario_falha.difference(usuario_sucesso)
       
print('usuario com um login bem-sucedido:')
print(usuario_sucesso)
print('\nusuario que tiveram somente logins com falha:')
print(somente_falha)




