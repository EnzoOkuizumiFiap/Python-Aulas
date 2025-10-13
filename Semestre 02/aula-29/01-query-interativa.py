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

'''
Exercício:

Adaptar a função abaixo para realizar alguma query em uma tabela que você tenha.

    1. Vai perguntar para o usuário algum dado para buscar
    2. Realiza a query usando o dado recebido por input

'''

def faz_queries(cursor, conexao):
    tabela = 'DDD_FILME'

    while True:
        selecione = int(input("\nDigite algumas das opções abaixo:\n1 - Listar todos \n2 - Buscar Filme \n0 - Sair\nInsira:"))

        if selecione == 1: 
            query = f'SELECT * FROM {tabela}'
            cursor.execute(query)
            
            print(f'\nTodos os dados presentes na tabela {tabela}:')
            
            for linha in cursor:
                print(linha)

        elif selecione == 2: 
            codigo_para_procurar = int(input('Qual Filme você quer procurar na tabela? Digite o ID: '))
            query = f'SELECT * FROM {tabela} WHERE CODIGO = :codigo'
            cursor.execute(query, {'codigo': codigo_para_procurar})

            resultados = cursor.fetchall()

            if resultados:
                for linha in resultados:
                    print(linha)
            else:
                print(f"Nenhum filme encontrado com o ID {codigo_para_procurar}.")


        elif selecione == 0:
            print("Encerrando busca...")
            break

        else:
            print("Opção inválida. Tente novamente.")


def main():
    print('Insira suas credenciais no BD Oracle da FIAP.')
    usuario = input('username: ')
    senha = getpass('senha: ')

    try:
        conexao = abre_conexao(usuario, senha)
    except oracledb.DatabaseError as e:
        print(f'Erro ao conectar: {e}')
        return

    print('Programa abriu conexão com o Banco de Dados.')

    cursor = conexao.cursor()
    
    faz_queries(cursor, conexao)

    cursor.close()
    conexao.close()
    print('Programa fechou a conexão e está encerrando.')

if __name__ == '__main__':
    main()