import oracledb
from getpass import getpass

SERVIDOR = 'oracle.fiap.com.br'
PORTA = 1521
SERVICO = 'ORCL'

def abre_conexao(usuario, senha):
    conexao = oracledb.connect(
        user = usuario,
        password = senha,
        dsn = f'{SERVIDOR}:{PORTA}/{SERVICO}'
    )
    return conexao

if __name__ == '__main__':
    print('Insira suas credenciais no BD Oracle da FIAP.')
    usuario = input('username: ')
    senha = getpass('senha: ')  # é como input, mas esconde o que estou digitando

    conexao = abre_conexao(usuario, senha)
    print('Programa abriu conexão com o Banco de Dados.')

    cursor = conexao.cursor()

    em_execução = True
    while em_execução:
        print('\nEscolha uma opção:')
        print('0 - Encerrar programa')
        print('1 - Mostrar todos os dados da tabela')
        print('2 - Nome específico da tabela')

        try:
            opcao = int(input())
        except:
            opcao = 0 # se der erro trato como opção de sair
        
        if opcao == 0:
            em_execução = False

        elif opcao == 1:
            cursor.execute('SELECT * FROM ESTUDANTES')

            # fetchall() retorna resultados da última query
            resultados = cursor.fetchall()
            for res in resultados:
                print(res)
        elif opcao == 2:
            nome_para_procurar = input('Qual Nome você quer procurar? Digite o NOME: ')

            query = f'SELECT * FROM ESTUDANTES WHERE NOME = :nome'
            cursor.execute(query, {'nome': nome_para_procurar})

            resultados = cursor.fetchall()

            print('resultado:', resultados)
    
    print('Programa está encerrando...')
    cursor.close()
    conexao.close()
    print('Programa encerrado.')