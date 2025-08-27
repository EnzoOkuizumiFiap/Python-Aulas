def filtra_baixas(temperaturas, temp_limite):
    resultado = []
    for temperatura in temperaturas:
        if temperatura < temp_limite:
            resultado.append(temperatura)
    return resultado

def main():
    temperaturas = [20.1, 19.2, 16.3, 23.4, 25.8]
    temps_baixas = filtra_baixas(temperaturas, 20.0)
    print(temps_baixas)

main()
