import json

def mostra_dados(estudante):
    print(f'Nome: {estudante["nome"]}')
    print(f'RA: {estudante["ra"]}')
    print(f'Curso: {estudante["curso"]}')

def main():
    with open('./semestre 2/aula-18/estudante.json') as arquivo:
        estudante = json.load(arquivo)
    
    print('Dados lidos com sucesso!')
    mostra_dados(estudante)

main()
