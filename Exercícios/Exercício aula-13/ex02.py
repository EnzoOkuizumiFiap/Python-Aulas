def maior(valor1, valor2, valor3):
    if valor1 >= valor2 and valor1 >= valor3:
        return valor1
    elif valor2 >= valor1 and valor2 >= valor3:
        return valor2
    else:
        return valor3

print("Forneça o primeiro valor:")
x = int(input())

print("Forneça o segundo valor:")
y = int(input())

print("Forneça o terceiro valor:")
z = int(input())

resultado = maior(x, y, z)
print("O maior dentre esses é o valor", resultado)
