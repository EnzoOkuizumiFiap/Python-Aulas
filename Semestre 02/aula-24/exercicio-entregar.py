def contem(lista, alvo):
    for elemento in lista:
        if elemento == alvo:
            return True
    # se saí do for sem retornar True, é porque o alvo não ocorre na lista
    return False

def minimo(lista):
    menor_até_agora = lista[0] # com qual valor eu inicializo essa variável?
    for elemento in lista:
        if elemento < menor_até_agora:
            menor_até_agora = elemento
    
    return menor_até_agora

def minimo_com_sorted(lista):
    # Ordena a lista e retorna o primeiro elemento (menor)
    lista_ordenada = sorted(lista)
    return lista_ordenada[0]


#Exercício 3
def valor_medio(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    
    return soma / len(lista)



listaDeNumeros = [5, 1, 0, 7, -3, 6, 2]

print(contem(listaDeNumeros, 7))    # Deve mostrar: True
print(contem(listaDeNumeros, 10))   # Deve mostrar: False
print(minimo(listaDeNumeros))       # Deve mostrar: -3 
print(minimo_com_sorted(listaDeNumeros)) # Deve mostrar: -3

print(valor_medio(listaDeNumeros))
