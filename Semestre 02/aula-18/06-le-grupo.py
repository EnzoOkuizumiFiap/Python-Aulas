import json

NOME_ARQUIVO = './semestre 02/aula-18/grupo_v2.json'

'''
Exercícios:

1. Preencher grupo_v2.json com dados do SEU GRUPO

2. Modificar função mostra_dados() para mostrar mais informações sobre o grupo e integrantes.
'''

def carrega_grupo():
    try:
        with open(NOME_ARQUIVO) as arquivo:
            grupo = json.load(arquivo)

    except:
        grupo = {}
    
    return grupo

def mostra_dados(grupo):
    if grupo == {}:
        print('Dados inexistentes.')
        print('Cadastre o grupo no arquivo', NOME_ARQUIVO)
    else:
        # é só um exemplo!
        # modifique para mostrar mais campos do JSON
        print(f'\nNome: {grupo['nome']}')
        print(f'Curso: {grupo['curso']}')
        print(f'Semestre: {grupo['semestre']}')
        print(f'Professor: {grupo['professor']}')
        print(f'matéria: {grupo['materia']}')

        print(f'\nIntegrantes do {grupo['nome']}:\n')
        integrantes = grupo['integrantes']

        for pessoa in integrantes:
            print(f'Nome: {pessoa['nome']}')
            print(f'RM: {pessoa['ra']}')
            print(f'turno: {pessoa['turno']}')
            print(f'Média: {pessoa['media']}')
            print('-------------------------------')

def main():
    grupo = carrega_grupo()
    if grupo == {}:
        print('Dados não encontrados')
    else:
        print('Dados lidos com sucesso')
    
    mostra_dados(grupo)

main()