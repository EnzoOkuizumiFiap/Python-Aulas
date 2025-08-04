quantidade = int(input("Digite quantas pessoas serão cadastradas:"))

nomes = []

for i in range(quantidade):
    nome = input(f"Digite o nome da {i + 1}° pessoa:")
    nomes.append(nome)

nomes.sort()

print("\nNomes cadastrados em ordem alfabética:")
for nome in nomes:
    print(nome)