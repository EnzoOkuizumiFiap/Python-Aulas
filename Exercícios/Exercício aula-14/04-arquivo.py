'''
Encoding = 'utf-8' garante que usamos a codificação correta para mostrar os acentos
'''
with open('./Exercícios/Exercício aula-14/exemplo.txt', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    print('Primeira linha do arquivo:')
    print(linhas[0])

    print("Vamos printar todas as linhas agora")
    for linha in linhas:
        print(linha.strip()) #.strip() tira a quebra de linha que tem no final
