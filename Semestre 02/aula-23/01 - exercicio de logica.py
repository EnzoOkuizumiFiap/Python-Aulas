'''
-----------------------------------------------------------------------
IMPORTANTE: usar for/while e não as coisas prontas do Python.
-----------------------------------------------------------------------
Exercícios:

1. Escreva uma função chamada contem, que recebe como parâmetros uma lista
e um elemento alvo.
Retorna True, se o alvo existe na lista, e False caso contrário.

2. Escreva uma função chamada minimo, que recebe como parâmetro uma lista.
Retorna o menor elemento existente na lista.

Exemplo: minimo([5, 1, 0, 7, -3, 6, 2]) --> retorna -3
'''

def contem(lista, alvo):
    for elemento in lista:
        if elemento == alvo:
            return True
    #Se saí do For sem retornar True, é porque o alvo não ocorre na lista
    return False

def minimo(lista):
    menor_até_agora = lista[0]
    for elemento in lista:
        if elemento < menor_até_agora:
            menor_até_agora = elemento
    #Retorna o menor valor
    return menor_até_agora

listaDeNumeros = [5, 1, 0, 7, -3, 6, 2]

print(contem(listaDeNumeros, 7))    # Deve mostrar: True
print(contem(listaDeNumeros, 10))   # Deve mostrar: False

print(minimo(listaDeNumeros))       # Deve mostrar: -3
