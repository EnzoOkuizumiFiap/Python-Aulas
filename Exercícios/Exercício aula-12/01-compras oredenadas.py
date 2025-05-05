compras = []

em_execucao = True
while em_execucao:
    print("Inserir elemento nas listas de compras?")
    print("0 - Não, quero encerrar o programa")
    print("1 - Sim, quero inserir um item")

    opcao = int(input())

    if opcao == 0:
        em_execucao = False
    elif opcao == 1:
        item = input("Escreva o nome do item:")
        compras.append(item)
    else:
        print("Opção Inválida.")
    

print("Encerrando o programa. Lista de compras gerada:")
# Asterisco deixa a saída mais limpa (Sem sintaxe de lista)
#sort() ordena a lista para mostrar em ordem alfabética
print(*compras.sort())
