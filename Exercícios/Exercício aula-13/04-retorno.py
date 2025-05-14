#Função que recebe um raio de círculo e retorna (dá como resultado) a área do círculo com esse raio

def area_circulo(raio):
    pi = 3.1415926536
    area = pi*(raio**2)
    return area

area1 = area_circulo(10)
area2 = area_circulo(3.5)

print('Área 1 =', area1)
print('Área 2 =', area2)