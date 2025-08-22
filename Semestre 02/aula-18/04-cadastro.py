def le_paciente_por_input():
    paciente = {}
    paciente['nome'] = input('Nome do paciente? ')
    paciente['idade'] = int(input('Idade? '))
    paciente['queixa'] = input('Qual a queixa? ')
    return paciente

def mostra(paciente):
    if paciente == {}:
        print('Paciente ainda sem dados! Use a opção de cadastro.')
    else:
        print(f'Nome: {paciente['nome']}')
        print(f'Idade: {paciente['idade']}')
        print(f'Queixa: {paciente['queixa']}')

def mostra_opcoes_menu():
    print('-----------------------------')
    print('0. Sair do programa')
    print('1. Mostrar dados paciente')
    print('2. Cadastrar o paciente')

def main():
    em_execucao = True
    paciente = {}
    while em_execucao:
        mostra_opcoes_menu()
        opcao_escolhida = int(input())
        if opcao_escolhida == 0:
            em_execucao = False
        elif opcao_escolhida == 1:
            mostra(paciente)
        elif opcao_escolhida == 2:
            paciente = le_paciente_por_input()
        else:
            print('Opção inválida. Tente novamente.')

    print('---')
    print('Programa encerrando...')

main()