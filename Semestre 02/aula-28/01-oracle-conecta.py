import oracledb
from getpass import getpass #Função getpass pega senha sem mostrar no terminal

def main():
    print('Insira suas credenciais no BD Oracle da FIAP:')
    usuario = input("username:")
    senha = getpass("password:") #É como input, mas esconde o que eu estou digitando

    try:
        conexao = oracledb.connect(
            user = usuario,
            password = senha,
            dsn = 'oracle.fiap.com.br:1521/ORCL'
        )
        print("Consegui abrir conexão com o BD")
        conexao.close()
    except:
        print("Não foi possível abrir conexão com o BD")

if __name__ == '__main__':
    main()

