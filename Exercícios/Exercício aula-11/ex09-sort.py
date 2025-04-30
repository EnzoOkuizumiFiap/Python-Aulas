valores = [4, 1, 2, 6, 3]

#O Método sort() deixa a lista em ordem crescente
#É um processo que chamamos de ORDENAR a lista
valores.sort()

print(valores)

'''
Observações importantes:

1 - O sort() é feito em "uma linha de código", mas internamente é um processo complexo e cujo tempo depende do tamanho da lista (Quanto maior o tamanho da lista, maior o tempo que esse processor vai demorar)

2 - sort() só funciona se todos os itens da lista são comparáveis entre si.
    *Se forem todos os itens do mesmo tipo, ok!
    *Se misturar int com float tudo bem, são comparáveis
    *Se misturar com string não funciona

'''

nomes = ['Paula', 'José', 'Bruna', 'Thiago']
nomes.sort()
print(nomes)

#Quando a lista é String, a ordenação é em ORDEM LEXICOGRÁFICA, que parecida com a ordem alfabética, mas consegue lidar com caracteres especiais. Além disso, trata miaúsculas e minúsculas de maneira diferente

palavras = ['Brasil', 'Alemanha', 'abacaxi']
palavras.sort()
print(palavras) #Inicial minúscula vem depois das iniciais maiúsculas.

print("\n-----------------------\n")

'''
Exercício: Modifique o programa da lista de compras para mostrar, ao final, as compras em ordem alfabética.
'''

compras = []

while True:
    item = input("Digite um item:")
    compras.append(item)

    print("Deseja adicionar mais um item? (s/n)")
    resposta = input().lower()

    if resposta != 's':
        break

print("\nLista criada:")
print(compras)

compras.sort()
print("Lista em ordem alfabética:")
print(compras)