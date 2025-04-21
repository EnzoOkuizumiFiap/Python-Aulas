#Ex 02 - Se você já fez isso, próximo exercício: Modificar o programa da tabuada para que mostre todas as tabuadas desde 1 até 10. (Você vai acabar fazendo um programa com while dentro do while)

# Inicializa o contador externo para as tabuadas
table = 1

# Loop while externo para percorrer as tabuadas de 1 até 10
while table <= 10:
    print(f"\nTabuada do {table}:")
    print("-" * 15)
    
    # Inicializa o contador interno para os multiplicadores
    multiplier = 1
    
    # Loop while interno para calcular e mostrar cada multiplicação
    while multiplier <= 10:
        result = table * multiplier
        print(f"{table} x {multiplier:2} = {result:2}")
        multiplier += 1
    
    table += 1
