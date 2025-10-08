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
    print('Insira suas credenciais no BD Oracle da FIAP:')
    usuario = input("username:")
    senha = getpass("password:")

    conexao = abre_conexao(usuario, senha)

    print("Programa abriu conexão com Banco de dados.")
    conexao.close()
    print("Programa fechou a conexão e está encerrando.")

if __name__ == '__main__':
    main()

