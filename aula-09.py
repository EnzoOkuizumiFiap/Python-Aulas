'''
O loop `while` em Python é usado para executar um bloco de código repetidamente enquanto uma condição específica for verdadeira.

while condicao:
    # Bloco de código a ser executado
    # (geralmente inclui algo que eventualmente tornará a condição falsa)

- A `condicao` é avaliada antes de cada iteração.
- Se a `condicao` for `True`, o bloco de código dentro do `while` é executado.
- Se a `condicao` for `False`, o loop termina e a execução continua após o bloco `while`.
- É importante garantir que a condição eventualmente se torne `False` para evitar loops infinitos, a menos que um loop infinito seja intencional e controlado (por exemplo, com `break`).
'''

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


#Exemplo 05 - Repetição com valores inicial e final definidos pelo usuário
print('Qual o valor inicial da repetição?')
inicio = int(input())
print('Qual o valor final da repetição?')
final = int(input())

i = inicio
while i < final:
    print(i)
    i = i + 1

print('while terminou porque i está com valor', i)