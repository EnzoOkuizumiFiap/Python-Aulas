def main():
    pessoas = {
        'Luiza' : {
            'idade' : 70,
            'altura' : 1.65
        },
        'Abner' : {
            'idade' : 19,
            'altura' : 1.78
        },
        'Flavia': {
            'idade' : 24,
            'altura' : 1.80
        },
        'Paulo' : {
            'idade' : 40,
            'altura' : 1.72
        }
    }

    # Exercício (a): imprimir nomes de quem tem mais de 30 anos
    for nome, dados in pessoas.items():
        if dados['idade'] > 30:
            print('Pessoas com mais de 30 anos:',nome)

    # Exercício (b): imprimir nomes de quem tem altura > 1.75
    for nome, dados in pessoas.items():
        if dados['altura'] > 1.75:
            print('Pessoas com altura maior que 1.75',nome)

main()