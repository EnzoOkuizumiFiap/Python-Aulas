def media(valores):
    #recebe uma lista de valores e retorna a média entre eles
    soma = sum(valores)
    numero_itens = len(valores)

    return soma / numero_itens

print(media([6, 8]))    # printa 7
print(media([100, 200]))#Printa 150

temperaturas = [15.7, 16.4, 18.0, 19.8, 22.5, 21.0, 20.6]
print("Temperaturas:", temperaturas)
print("A média de temperaturas é", media(temperaturas))
