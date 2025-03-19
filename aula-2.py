n = 5
print("Tabuada do ", n)

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")



#Diferentes tipos de dados em python

a = 5       #Número inteiro: Int
pi = 3.14   #Número com parte decimal: Float

nome = "Enzo" #Texto ou String: Str (Cadeia ou sequência de caracteres)

Chovendo = False #Tipo "Bool" (booleano) Verdadeiro/Falso
Sol = True 

# O tipo booleano admite apenas dois valores distintos:
#True (verdadeiro) e False (falso)

#Alguns outros tipo de dados que vamos ver: Lista, None, Tupla, Dicionário
#Para o separador ficar vazio (ou seja, sem nada) em vez de ser espaço
print("coisa1", "coisa2", "coisa3", "\n", sep='')



#Entrada de dados é o programa RECEBER  valores do "mundo externo"
#Exemplo 1: Input

print("Qual o seu nome?")
nome = input()

print("Prazer em te conhecer", nome)



#Mais avançado

print('Oi, qual o seu nome? Digite abaixo por favor.')
nome = input()

print('Em qual cidade você nasceu?')
cidade = input()

print('Qual sua idade?')
idade = input()

print('Obrigado pelas informações!')
print('Você é', nome, 'natural da cidade de', cidade)
print('Atualmente você tem', idade, 'anos')



#Nome + espaço + Sobrenome

print("Qual seu nome?")
nome = input()

print("Qual seu sobrenome?")
sobrenome = input()

nome_completo = nome + ' ' + sobrenome
print("Seu nome completo é", nome_completo)



#Cuidado ao somar valores

#Pegando INPUT e tratando como números inteiros
# (Por padrão "input" gera TEXTO)
print("Digite os dois valores")
#vv No caso a resolução já está correta -> int(input())
valor = int(input())
valor2 = int(input())

print("A soma é", valor + valor2)

