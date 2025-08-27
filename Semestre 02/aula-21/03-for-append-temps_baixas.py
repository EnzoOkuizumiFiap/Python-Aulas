def main():
    temperaturas = [ 20.0, 19.2, 16.3, 23.4, 25.8]
    temps_baixas = []
    
    # Exercício 1: implemente a lógica para filtrar temperaturas abaixo de 20 graus
    
    for temperatura in temperaturas: #Percorre cada temperatura na lista temperaturas
        if temperatura < 20.0: #Se a temperatura for menor que 20.0
            temps_baixas.append(temperatura) #append -> acrescentar, acrescenta um elemento na lista

    print(temps_baixas) # Mostrar temperaturas abaixo de 20.0

main()