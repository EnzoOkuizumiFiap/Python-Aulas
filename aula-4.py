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

##Exercício 10 - Calcular distância de um ponto até a origem.
'''
Calcular a distância de um ponto até a origem (coordenada (0, 0) do plano). Seu programa irá:

Ler as coordenadas x e y de um ponto (leia uma de cada vez, isto é, use inputs separados para o x e o y);

Calcular a distância de (x, y) até (0, 0), também chamado de "magnitude" desse ponto;

Mostrar a distância.

Lembre que essa distância é calculada como sendo a raiz quadradada de (x² + y²)

BÔNUS (a): calcular distância entre dois pontos distintos

BÔNUS (b): calcular distância entre dois pontos em 3D (isto é, pontos com coordenadas (x, y, z))
'''

X = int(input("Coordenada X:"))
Y = int(input("Coordenada Y:"))


