#Range pode ser especificado por valores que vêm de variáveis

print('Qual o início do intervalo?')
inicio = int(input())

print("Qual o fim do Intervalo?")
fim = int(input())

for numero in range(inicio, fim):
    print(numero)


'''
Exercício: 

Modifique o programa para que, se usuário digitar inicio maior do que fim, seja mostrado o intervalo decrescente.

Exemplo: se inicio = 5, fim = 0, print 5, 4, 3, 2, 1

Dica: Criar um variável "passo" que vai ser 1 ou -1
e aí fazemos for numero in range(inicio, fim, passo)

'''

inicio_2 = int(input("Digite o inicio do intervalo:"))
fim_2 = int(input("Digite o fim do intervalo:"))

if inicio_2 < fim_2:
    passo_2 = 1
    fim_ajustado = fim_2
else:
    passo_2 = -1
    fim_ajustado = fim_2 - 1

for numero_2 in range(inicio_2, fim_ajustado, passo_2):
    print(numero_2)