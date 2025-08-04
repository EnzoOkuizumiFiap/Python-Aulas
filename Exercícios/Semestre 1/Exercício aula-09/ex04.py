#É o exercício da tabuada só que mais limpo

n = 1

while n <= 10:
    print(f'Tabuada do {n}:')
    multiplicador = 1
    while multiplicador <= 10:
        print(f'{n} x {multiplicador} = {n * multiplicador}')
        multiplicador += 1

    print()
    n += 1  # atualização da variável do while externo
