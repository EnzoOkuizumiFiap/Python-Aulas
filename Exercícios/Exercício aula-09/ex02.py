#Ex 02 - Se você já fez isso, próximo exercício: Modificar o programa da tabuada para que mostre todas as tabuadas desde 1 até 10. (Você vai acabar fazendo um programa com while dentro do while)

for i in range(1, 11):
    print(f"Tabuada do {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()
