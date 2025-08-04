#Pergunte a idade do usuário (em anos). Imprima uma mensagem especial se ele já viveu mais do que 10 mil dias.

idade = int(input("Digite sua idade em anos: "))
dias_vividos = idade * 365

if dias_vividos > 10000:
    print(f"Parabéns, você já viveu {dias_vividos} dias!")
else:
    print("Você ainda não viveu mais de 10 mil dias.")
    print(f"Você já viveu {dias_vividos} dias.")