# Pergunte a nota de um aluno em três atividades diferentes. Calcule a média entre as três. 
# Imprima "aprovado" se a média for maior ou igual a 6, e "fará recuperação" caso contrário.

# Solicita as notas das três atividades
nota1 = float(input("Digite a nota da primeira atividade: "))
nota2 = float(input("Digite a nota da segunda atividade: "))
nota3 = float(input("Digite a nota da terceira atividade: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Verifica se o aluno foi aprovado ou fará recuperação
if media >= 6:
    print("Aprovado")
else:
    print("Fará recuperação")