'''
Resolução daquele exercício de Entregar

3. Escreva uma função chamada `valor_medio`, que recebe como parâmetro 
uma lista de números e retorna a média de sus valores.
'''


def valor_medio(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    
    media = soma /len(lista)

    return media


def valor_medio_alt(lista):
    media = 0
    for elemento in lista:
        media = media + elemento/len(lista)

    return media


