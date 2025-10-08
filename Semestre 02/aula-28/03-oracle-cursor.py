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

def main():
    print('Insira suas credenciais no BD Oracle da FIAP... Aguarde\n')
    usuario = input("user:")
    senha = getpass("password:")

    conexao = abre_conexao(usuario, senha)

    tabela = 'DDD_FILME'
    query = f'SELECT * FROM {tabela}'

    cursor = conexao.cursor()
    cursor.execute(query)

    #Mostra todos os resultados da query:
    for linha in cursor:
        #Cada linha de resultado é uma tupla
        print(linha)

    cursor.close()
    conexao.close()
    print("\nPrograma fechou a conexão e está encerrando.")

if __name__ == '__main__':
    main()
