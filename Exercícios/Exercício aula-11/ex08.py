compras = []

print('Quantos itens você deseja colocar na lista de compras?')

numero_itens = int(input())

itens_inseridos = 0
while itens_inseridos < numero_itens:
    print("Digite um item:")
    item = input()
    compras.append(item)
    itens_inseridos += 1

print("Lista criada:")
print(compras)

print("\n-----------------------\n")


'''
Exercício: Modifique o programa acima para que o usuário, em vez de escolher no início a quantidade de itens, receba a cada passo a opção de adicionar mais um item ou encerrar o programa
'''

compras = []

while True:
    item = input("Digite um item:")
    compras.append(item)

    print("Deseja adicionar mais um item? (s/n)")
    resposta = input().lower()

    if resposta != 's':
        break

print("Lista criada:")
print(compras)

