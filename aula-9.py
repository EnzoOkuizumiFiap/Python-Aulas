#Usando o While...

#Exemplo 01 - Idade
print('Qual sua idade?')
idade = int(input())
while idade < 18:
    print('Você tem', idade, 'anos e portanto é menor de idade')
    idade = idade + 1  # "aniversário": aumentamos a idade em 1 a cada loop
print('O programa terminou.')


#Exemplo 02 - Tabuada do 7 
#Abstração: Transformo as contas concretas 7x2, 7x3... Em uma conta genérica: 7 x N, com N mudando de valor
N = 1
while N <= 10:
    print(N*7)
    N = N + 1


#Exemplo 03 - Tabuada Genérica
#Padrão de código comum é chamar essa variável "auxiliar" que passa por diversos valores (nesse caso, 1 a 10) de "i"
i = 1
numero = int(input("\nDigite um número: "))
while i <= 10:
    print(numero*i)
    i += 1

#Exemplo 04 - Menu / Duas opções: Soma e encerrar programa
em_execucao = True

while em_execucao:
    print('Escolha uma opção:')
    print('A - Somar dois números')
    print('B - Encerrar programa')

    opcao = input()
    if opcao == 'A':
        print('Digite o primeiro valor para a soma:')
        x = float(input())
        print('Digite o segundo valor para a soma:')
        y = float(input())

        print('Resultado da soma:', x + y)
    else:
        em_execucao = False
print('Encerrando...')
