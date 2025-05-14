#Quando temos vários parâmetros, eles são separados por vírgulas
def soma(x, y):
    return x + y

#Na chamada, precisamos fornecer todos os parâmetros (separando por vírgula)
#A chamada na linha abaixo executa corpo da função, inicializando x com valor ___ e y com valor ___
print("Soma entre 2 e 3 =", soma(2, 3))

#Exercício maior valor
def maior_valor(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2

print("O maior valor é", maior_valor(20, 30))

#Explicação - Função maior recebe dois valores (x e y) retorna o maior dentre eles

#Função maior recebe dois valores (x e y) e retorna o maior dentre eles
def maior(x, y):
    if x > y:
        resultado = x
    else:
        resultado = y
    return resultado

#Função menor recebe dois valores (x e y) e retorna o menor dentre eles podia escrever do mesmo jeito da função maior, mas quero exemplificar o fato de que uma função pode ter mais do que um comando "return"
def menor(x, y):
    if x < y:
        return x
    else:
        return y
    
valor1 = 4
valor2 = 9
print(f'{valor1} + {valor2} = {soma(valor1, valor2)}')
print(f'maximo entre {valor1} e {valor2} = {maior(valor1, valor2)}')
print(f'minimo entre {valor1} e {valor2} = {menor(valor1, valor2)}')