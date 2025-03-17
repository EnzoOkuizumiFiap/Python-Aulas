from datetime import datetime
'''
O que vimos até aqui?

* Print
* Operações númericas
* Criar Variáveis
* Input (Entrada de dados)

'''

#Exercício 1 - Faça aparecer uma mensagem de boas-vindas
bem_vindo = "bem-vindo"

print("Olá, seja " + bem_vindo + " ao meu programa! Qual o seu nome?")
nome = input()
print("Boas-vindas,", nome)


#Exercício 2 - Pergunte ao usuário por 2 números (x e Y)

#A - Mostre a soma X + Y
print("\nDigite os número que deseja somar:")

x = int(input("Qual o 1° Número? "))
y = int(input("Qual o 2° Número? "))

print(f"{x} + {y} =", x + y)

#B - Mostre mais três operações à sua escolha

print("\nOutras operações: ")
print(f"Multiplicação:", x * y, "\nDivisão:", x / y, "\nPotenciação:", x ** y)
print("\n")


#Exercício 3 - Conversão de anos em meses e dias.

Ano = int(input("Digite a sua idade:"))
Ano_para_meses = 12 * Ano
Ano_para_dias = 365 * Ano

print(f"O ano {Ano} em meses seria de {Ano_para_meses} meses")
print(f"O ano {Ano} em dias é de {Ano_para_dias} dias")
print("\n")



#Exercício 4 - Mostrar o tamanho de um texo.

nome = input("Digite o seu nome:")
tamanho = len(nome)

print(f"O número de letra fornecido pelo usuário é de {tamanho}")
print("\n")


#Exercício 5 - Conversão de temperatura

Fahrenheit = int(input("Qual a temperatura do local em Fahrenheit?"))
Fahrenheit_para_celsius = (Fahrenheit - 32) * 5 / 9
print("O valor em Celsius é", Fahrenheit_para_celsius)

Celsius = int(input("Qual a temperatura do local em Celsius?"))
Celsius_para_fahrenheit = (Celsius * 9 / 5) + 32
print("O valor em Fahrenheit é", Celsius_para_fahrenheit)
print("\n")


#Exercício 6 - Cálculo de área e valor

Comprimento = float(input("Qual o comprimento do seu terreno?"))
Largura = float(input("Qual a largura do seu terreno?"))
Area_total = Comprimento * Largura

print("A área total do seu terreno é", Area_total)

Preco_terreno = float(input("Qual o valor do seu terreno?"))
Preco_metro = Preco_terreno / Area_total

print("O valor do seu terreno por metro quadrado é", Preco_metro)

#Exercício 7 - Bônus
ano_atual = datetime.now().year

usuario_ano = int(input("Qual o ano em que você nasceu?"))
Idade = ano_atual - usuario_ano 
print("A sua idade é", Idade, "anos")

if Idade < 18:
    print("Você é menor de idade, isso requer uma autorização para usar o sistema")
else:
    print("Acesso permitido!")