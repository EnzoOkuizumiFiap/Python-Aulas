#compras é uma variável do tipo Lista (list)

SEPARATOR = "\n-----------------------\n"

compras = ['goiaba', 'alface', 'pão']
for item in compras:
    print(item)

print(SEPARATOR)

#Em python, a lista pode ser HETEROGÊNEA, isto é, conter dados de diferentes tipo

itens = [8, 'olá', 3.14, False, 'ok']
for item in itens:
    print(item)

print(SEPARATOR)

#Acima, eu estava fazendo print item por item, mas posso pedir para printar a lista de uma vez

print(compras)

print(SEPARATOR)

#Posso usar APPEND para adicionar novos itens na lista:
compras.append('queijo')

print(compras)