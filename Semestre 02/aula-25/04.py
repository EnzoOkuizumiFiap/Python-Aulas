'''
Para efeito de comparação, vou colocar a versão "antiga"
(que não ordena a lista)
'''

#O(N) -> proporcional ao tamanho da lista
#Esse for: Custo: O(N), onde N é o tamanho da lista
#Se a lista tem N elementos, o for vai fazer N passos.

#Percorre a lista com For
def minimo_com_for(lista):
    menor_valor_ate_agora = lista[0]
    
    for elemento in lista:
        if elemento < menor_valor_ate_agora:
            menor_valor_ate_agora = elemento
        
    return menor_valor_ate_agora

#ordenando lista com sort, mas ele altera a lista original
def minimo_sort(lista):
    lista.sort() #Altera a lista, muda a 'lista' e deixa ordenada
    return lista[0]

#Ordenando a lista com sorted, mas ele gera uma nova lista, então precisamos atribuir uma variável a ele
#Em lista ordenada, o menor elemento está na posição 0
def minimo_sorted(lista):
    # A função fica simples, mas o custo da ordenação é bem mais alto do que calcular o mínimo de forma direta
    lista_ordenada = sorted(lista)
    return lista_ordenada[0]