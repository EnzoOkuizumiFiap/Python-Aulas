#Pergunte a temperatura em Fahrenheit. Imprima "está calor" se a temperatura equivale a mais de 25 graus Celsius.

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9

if celsius > 25:
    print("Está calor.")
else:
    print("Não está calor.")