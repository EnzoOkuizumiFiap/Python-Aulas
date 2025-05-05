exemplo = [4, 1, 9, 2, 5, 3, 7, 10, 6, 8]

#print('Menor elemento da lista:', min(exemplo))
#print('Maior elemento da lista:', max(exemplo))

#Verifica o menor número da lista
minimo = exemplo[0]
for valor in exemplo:
    if valor < minimo:
        minimo = valor

print('Menor elemento da lista:', minimo)

#Verifica o maior número da lista
maximo = exemplo[0]
for valor in exemplo:
    if valor > maximo:
        maximo = valor

print('Maior elemento da lista:', maximo)
