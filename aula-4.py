import math
#Exercício 08 - Calcular área de um círculo: Peça ao usuário por input o raio de um círculo. Calcule e mostre sua área.
PI = 3.14 #Valor Constante

raio = float(input("Diga o raio do círculo: ")) 

calculo_area_circulo = PI * raio ** 2

print("A área do círculo é de", calculo_area_circulo)



#Exercício 09 - Vamos usar esse exercício para aprender algumas operações de string. Peça um texto por input.

#(a) Mostre esse texto em MAIÚSCULAS (método upper());
texto = "abobrinha"

texto_maiusculo = texto.upper()
print("Texto em maiúsculo: ", texto_maiusculo)

#(b) Mostre esse texto trocando a letra 'a' por 'i' (método replace());
texto_trocado = texto.replace('a', 'i')
print("Texto com 'a' trocado por 'i':", texto_trocado)

#(c) Mostre o número de ocorrências da letra 'e'.

ocorrencias_e = texto.count('e')
print("Número de ocorrências da letra 'e':", ocorrencias_e)

print("\n")

'''
Calcular a distância de um ponto até a origem (coordenada (0, 0) do plano). Seu programa irá:

Ler as coordenadas x e y de um ponto (leia uma de cada vez, isto é, use inputs separados para o x e o y);

Calcular a distância de (x, y) até (0, 0), também chamado de "magnitude" desse ponto;

Mostrar a distância.

Lembre que essa distância é calculada como sendo a raiz quadradada de (x² + y²)

BÔNUS (a): calcular distância entre dois pontos distintos

BÔNUS (b): calcular distância entre dois pontos em 3D (isto é, pontos com coordenadas (x, y, z))
'''

##Exercício 10 - Calcular distância de um ponto até a origem.

# Ler as coordenadas x e y de um ponto
print("Calculando a distância de um ponto até a origem\n")

x = float(input("Diga a coordenada X:"))
y = float(input("Diga a coordenada Y:"))

#sqrt é √ (raiz) / (Potenciação > Soma) > Raiz
distancia = math.sqrt(x**2 + y**2)

print(f"Distância: {distancia:.2f}")



#Leitura dos valores para calcular a distância entre dois pontos no plano 2D
print("\nCalculando a distância entre 2 pontos no plano Cartesiano (2D)\n")
x_1 = float(input("Diga a coordenada do X_1:"))
y_1 = float(input("Diga a coordenada do Y_1:"))

x_2 = float(input("Diga a coordenada do X_2:"))
y_2 = float(input("Diga a coordenada do Y_2:"))

distancia_2d = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

print(f"A distância entre os dois pontos é de {distancia_2d}")



#Calculando a distância entre dois pontos no espaço 3D
print("\nCalculando a distância entre dois pontos no espaço Tridimensional")

print("\nDiga as coordenadas do seu PRIMEIRO PONTO")
x_01 = float(input("Diga a coordenada X_01: "))
y_01 = float(input("Diga a coordenada Y_01: "))
z_01 = float(input("Diga a coordenada Y_01: "))

print("\nDiga as coordenadas do seu SEGUNDO PONTO")
x_02 = float(input("Diga a coordenada X_02: "))
y_02 = float(input("Diga a coordenada Y_02: "))
z_02 = float(input("Diga a coordenada Z_02: "))

distancia_3d = math.sqrt((x_02 - x_01) ** 2 + (y_02 - y_01) ** 2 + (z_02 - z_01) ** 2)

print(f"A distância entre os pontos no plano 3D é {distancia_3d:.2f}")