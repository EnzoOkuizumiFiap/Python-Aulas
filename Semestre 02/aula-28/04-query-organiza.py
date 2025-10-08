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

def faz_queries(cursor, conexao):
    tabela = 'DDD_FILME' # troque por alguma outra que você tenha no seu usuário Oracle da FIAP
    query = f'SELECT * FROM {tabela}'
    
    cursor.execute(query)

    print(f'Todos os dados presentes na tabela {tabela}:')

    # mostra todos os resultados da query:
    for linha in cursor:
        # cada linha de resultado é uma tupla
        print(linha)

def main():
    print('Insira suas credenciais no BD Oracle da FIAP.\n')
    usuario = input('username: ')
    senha = getpass('senha: ')  # é como input, mas esconde o que estou digitando

    conexao = abre_conexao(usuario, senha)
    print('Programa abriu conexão com o Banco de Dados.\n')

    cursor = conexao.cursor()
    
    faz_queries(cursor, conexao)

    cursor.close()
    conexao.close()
    print('\nPrograma fechou a conexão e está encerrando.')

if __name__ == '__main__':
    main()