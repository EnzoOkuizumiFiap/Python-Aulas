import json

# nome do arquivo usado para persistir os dados
NOME_ARQUIVO = './semestre 02/aula-18/paciente.json'

def le_json():
    '''
    bloco try/except

    É QUASE um if/else. Se o bloco do try causar erro,
    (por exemplo por arquivo inexistente), executamos
    bloco do except
    '''
    try:
        with open(NOME_ARQUIVO) as arquivo:
            paciente = json.load(arquivo)
    except:
        # se não consegui abrir arquivo, paciente fica vazio
        paciente = {}
    
    return paciente

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
    print('2. Cadastrar/atualizar paciente')

def main():
    paciente = le_json()
    em_execucao = True
    while em_execucao:
        mostra_opcoes_menu()
        opcao_escolhida = int(input())
        if opcao_escolhida == 0:
            em_execucao = False
        elif opcao_escolhida == 1:
            mostra(paciente)
        elif opcao_escolhida == 2:
            paciente = le_paciente_por_input()
            with open(NOME_ARQUIVO, 'w') as arquivo:
                json.dump(paciente, arquivo, indent=4)
        else:
            print('Opção inválida. Tente novamente.')

    print('---')
    print('Programa encerrando...')

main()