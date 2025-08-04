x = float(input("Digite o valor X: "))
y = float(input("Digite o valor Y: "))

print("Qual operação desejada? Digite o número correspondente")
opcao = int(input("1.Soma; 2.Multiplicação; 3.Divisão; 4.Exponenciação: "))

if opcao == 1:
    print(f"{x} + {y} = ", x + y)
elif opcao == 2:
    print(f"{x} * {y} = ", x * y)
elif opcao == 3:
    print(f"{x} / {y} = ", x / y)
elif opcao == 4:
    print(f"{x} ** {y} = ", x ** y)
else:
    print("Opção inserida inválida")