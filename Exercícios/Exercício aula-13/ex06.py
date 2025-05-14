from math import pi

def area_circulo(raio):
    #Variável pi importada do módulo math
    area = pi * (raio ** 2)
    return area

print('O valor de pi é', pi)

raios = [0.5, 3, 1, 5.4, 0.9, 8.0, 12.3, 2.7]

print("A lista completa de raios é", *raios)
print("Os raios que dão área maior que 20 são:")

conta = 0

for raio in raios:
    area = area_circulo(raio)
    if area > 20:
        print(raio)
        conta += 1


'''
Modifique o programa acima para printar: Ao inicio, qual o tamanho total da lista de raios, ao final quantos resultaram em área maior que 20
'''

print("O tamanho total da lista é", len(raios))
print("O tamanho da lista que resultaram em área maior que 20 é", conta)

