#Exibindo todas as tabuadas

n = 1  # inicialização da variável do while externo

while n <= 10:  # condição (depende do n)
    print(f'Tabuada do {n}:')
    multiplicador = 1  # inicialização da variável do while interno

    # para cada passo do while externo, são feitos 10 passos do while interno:
    while multiplicador <= 10:
        print(f'{n} x {multiplicador} = {n * multiplicador}')
        multiplicador += 1  # atualização da variável do while interno

    print()  # linha em branco
    n += 1  # atualização da variável do while externo

# Exercício: deixar a saída do programa mais legível
# Exercício: identificar inicialização, condição e atualização dos dois blocos while
