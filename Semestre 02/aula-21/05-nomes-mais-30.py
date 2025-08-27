def main():
    idades = {
        'Luiza': 70,
        'Abner': 19,
        'Flavia': 24,
        'Paulo': 40
    }

    def filtro(idade):
        return idade > 30

    # Imprimir nomes de quem tem mais de 30 anos usando filtro
    for nome, idade in idades.items():
        if filtro(idade):
            print(nome)

main()