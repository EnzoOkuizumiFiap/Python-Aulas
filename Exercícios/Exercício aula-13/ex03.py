'''
função que recebe uma lista e retorna o último item dela
'''

def ultimo(lista):
    #Em uma lista de 3 elementos, o último é o índice 2
    #Em uma lista de 10 elementos, o último é o índice 9
    #Último índice é sempre o tamanho da lista menos -1
    ultimo_valor = lista[len(lista)-1]
    return ultimo_valor

exemplo = [5, 1, 4, 6, 7, 9, 0, 2]
print(ultimo(exemplo))