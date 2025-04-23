'''
Conceito de passo: Em quanto eu modifico o valor da variável na etapa de atualização.

(Só faz sentido quando a atualização tem uniformidade, ou seja, altera a variével sempre da mesma maneira.)
'''

inicio = 5
fim = 12

print("passo 1:")
i = inicio 
while i < fim:
    print(i)
    i += 1

print("\npasso 3:")
i = inicio
while i < fim:
    print(i)
    i += 3

#Passo também pode ser negativo:
inicio = 10
fim = 0 

print("\nPasso -1:")
i = inicio
while i > fim:
    print(i)
    i -= 1

print("\nPasso -2:")
i = inicio
while i > fim:
    print(i)
    i -= 2
