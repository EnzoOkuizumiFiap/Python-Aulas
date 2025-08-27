# Exercício: modifique sua resposta do Exercício 1 para que a lógica que filtra as temperaturas baixas esteja em uma função separada 

def filtra_baixas(temperaturas):
    resultado = []
    for temperatura in temperaturas:
        if temperatura < 20.0:
            resultado.append(temperatura)
    return resultado

def main():
    temperaturas = [ 20.0, 19.2, 16.3, 23.4, 25.8]
    temps_baixas = filtra_baixas(temperaturas)

    print(temps_baixas) #Mostrar temperaturas abaixo de 20.0

main()