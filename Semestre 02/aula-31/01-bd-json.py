'''
Esse programa supõe a existência de uma tabela Estudantes criada assim:

CREATE TABLE ESTUDANTES (
    id NUMBER PRIMARY KEY,
    rm VARCHAR(10),
    nome VARCHAR(100),
    curso VARCHAR(100),
    turma VARCHAR(20)
)
'''

import oracledb
from getpass import getpass
import json

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





def mostra_resultados_query(cursor):
    #fetchall retorna resultados da última query na forma de lista
    resultados = cursor.fetchall()

    print("\n--------------------------")

    #Se a última query não teve resultado, printa mensagem especial
    if resultados == []:
        print("\nNão foram encontrados dados correspondentes a essa busca")
    else:
        for res in resultados:
            print(res)
    print("--------------------------")




def mostra_todos_dados(cursor):
    #Em vez de SELECT *, escrevo as colunas na ordem que quero que venham
    cursor.execute('SELECT id, rm, nome, curso, turma FROM ESTUDANTES')

    resultados = cursor.fetchall()
    resultados_convertidos = [] #Monta resultados na forma de lista de dicionários

    for resultado in resultados:
        print(resultado)

        dicionario = {
            'id' : resultado[0],
            'rm' : resultado[1],
            'nome' : resultado[2],
            'curso' : resultado[3],
            'turma' : resultado[4]
        }
        resultados_convertidos.append(dicionario)

    print("\n")
    resposta = input("Exportar resultados para JSON?? (S/N)")
    
    if resposta == 'S':
        with open('resultado_query.json', 'w') as arquivo:
            json.dump(resultados_convertidos, arquivo, indent=4)

    #mostra_resultados_query(cursor)





def mostra_resultados_busca(cursor, estudante, opcao_nome):
    if (opcao_nome == 1):
        query = 'SELECT * FROM ESTUDANTES WHERE nome = :nome'
        cursor.execute(query, {'nome' : estudante})

    elif (opcao_nome == 2):
        query = 'SELECT * FROM ESTUDANTES WHERE rm = :rm'
        cursor.execute(query, {'rm' : estudante})

    
    resultados = cursor.fetchall()
    resultados_convertidos = [] #Monta resultados na forma de lista de dicionários

    for resultado in resultados:
        print(resultado)

        dicionario = {
            'id' : resultado[0],
            'rm' : resultado[1],
            'nome' : resultado[2],
            'curso' : resultado[3],
            'turma' : resultado[4]
        }
        resultados_convertidos.append(dicionario)

    print("\n")
    resposta = input("Exportar resultados para JSON?? (S/N)")
    
    if resposta == 'S':
        with open('resultado_query_nome.json', 'w') as arquivo:
            json.dump(resultados_convertidos, arquivo, indent=4)
         
    #mostra_resultados_query(cursor)





def insere_novo_dado(conexao, cursor):
    print('\nInsira as informações para inserção no BD:')
    dicionario_dados = {
        'id' : int(input('ID: ')),
        'rm' : input('RM: '),
        'nome' : input('nome: '),
        'curso' : input('curso: '),
        'turma' : input('turma: ')
    }
    
    query = '''
    INSERT INTO ESTUDANTES (id, rm, nome, curso, turma)
    VALUES (:id, :rm, :nome, :curso, :turma)
    '''
    
    cursor.execute(query, dicionario_dados)
    conexao.commit() # necessário após fazer modificações na tabela
    



def remover_estudante(cursor, id_remover, conexao):
    print(f'Removendo estudante {id_remover}')

    query = 'delete from estudantes where id = :id'
    cursor.execute(query, {'id' : id_remover})

    #rowcount conta o número de linhas afetadas na última query
    linhas_afetadas = cursor.rowcount

    if linhas_afetadas == 0:
        print('Não foi removido nenhum dado. ID INEXISTENTE')
        
    else:
        print("\nRemovido com sucesso")
        conexao.commit()

#Retorna True, se a tabela existe no banco de dados; Retorna False caso contrário
def existe_tabela(cursor, nome_tabela):
    query = 'select table_name from user_tables where table_name = :nome'

    cursor.execute(query, {'nome' : nome_tabela})
    resultados = cursor.fetchall()

    #Se a tabela existe, a query terá 1 resultado. Senão, terá zero resultado.
    if len(resultados) == 1:
        return True
    else:
        return False




if __name__ == '__main__':
    print('Insira suas credenciais no BD Oracle da FIAP.')
    usuario = 'rm561432' #input('username: ')
    senha = '301006' #getpass('senha: ')  # é como input, mas esconde o que estou digitando

    conexao = abre_conexao(usuario, senha)
    print('Programa abriu conexão com o Banco de Dados.')

    cursor = conexao.cursor()

    if existe_tabela(cursor, 'ESTUDANTES'):
        print("A tabela ESTUDANTES foi encontranda!")
    else:
        print("A tabela ESTUDANTES não existe... Criando")
        query_cria = '''
        CREATE TABLE ESTUDANTES (
            id NUMBER PRIMARY KEY,
            rm VARCHAR(10),
            nome VARCHAR(100),
            curso VARCHAR(100),
            turma VARCHAR(20)
        )
        '''
        cursor.execute(query_cria)

        print("Tabela criada...")



    em_execução = True
    while em_execução:
        print('\nEscolha uma opção:')
        print('1 - Mostrar todos os Estudantes')
        print('2 - Procurar nome de Estudante')
        print('3 - Inserir novo Estudante')
        print('4 - Deletando Estudante')
        print("5 - Destruir a tabela ESTUDANTES")
        print('0 - Encerrar programa')

        try:
            opcao = int(input("Digite:"))
        except:
            opcao = 0 # se der erro trato como opção de sair
        
        if opcao == 0:
            em_execução = False

        elif opcao == 1:
            mostra_todos_dados(cursor)
        
        elif opcao == 2:
            opcao_nome = int(input("\nDeseja procurar por: 1 - Nome ou 2 - RM ?? "))

            if opcao_nome == 1:
                estudante = input('Qual nome de Estudante procurar? ')
                mostra_resultados_busca(cursor, estudante, opcao_nome)
            elif opcao_nome == 2:
                estudante = input("Qual RM de Estudante procurar? ")
                mostra_resultados_busca(cursor, estudante, opcao_nome)
        
        elif opcao == 3:
            insere_novo_dado(conexao, cursor)
        elif opcao == 4:
            try: 
                id = int(input('\nDigite o ID do Estudante que deseja remover:'))
                remover_estudante(cursor, id, conexao)
            except:
                print("ID Inválido")
        elif opcao == 5:
            confirmacao = input('Certeza que quer destruir a tabela?? (S/N) ')

            if confirmacao == 'Sim':
                cursor.execute('DROP TABLE ESTUDANTES')
                conexao.commit()
                print("Tabela DESTRUÍDA")
                em_execução = False
            else: 
                print("Tabela não destruída")
    
    print('Programa está encerrando...')
    cursor.close()
    conexao.close()
    print('Programa encerrado.')