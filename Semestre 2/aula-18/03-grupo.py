import json

def mostra_dados(estudante):
    print(f'Nome: {estudante["nome"]}')
    print(f'RA: {estudante["ra"]}')
    print(f'Curso: {estudante["curso"]}')

def main():
    with open('./semestre 2/aula-18/grupo.json') as arquivo:
        grupo = json.load(arquivo)
    
    print('Dados lidos com sucesso!')
    #print(grupo)
    for estudante in grupo:
        print("Vamos mostrar os dados do grupo:")
        print('---')
        mostra_dados(estudante)

main()
