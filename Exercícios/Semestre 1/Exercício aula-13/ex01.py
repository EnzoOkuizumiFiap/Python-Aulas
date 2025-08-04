def menor(valor1, valor2):
    if valor1 < valor2:
        return valor1
    else:
        return valor2
    
print("Forneça o primeiro valor:")
x = int(input())

print("Forneça o segundo valor:")
y = int(input())

resultado = menor(x, y)
print("O menor dentre eses é o valor", resultado)
