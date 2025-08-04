em_execucao = True

while em_execucao:
    print('Escolha uma opção:')
    print('A - Imprimir Mensagem')
    print('B - Encerrar Programa')

    opcao = input()
    if opcao == 'A':
        print('Bom dia')
    else:
        em_execucao = False

print('Encerrando...')

# Exercício: modifique o programa acima para fazer uma calculadora interativa