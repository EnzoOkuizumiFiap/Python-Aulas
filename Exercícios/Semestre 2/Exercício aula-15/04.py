quantidade = int(input("Quantas pessoas serão cadastradas? "))
cadastro = {}

for i in range(quantidade):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    cadastro[nome] = idade

nomes_ordenados = sorted(cadastro.keys())

print("\nNomes e idades cadastrados (ordem alfabética):")
for nome in nomes_ordenados:
    print(f"{nome}: {cadastro[nome]} anos")
