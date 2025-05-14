def idade(ano_nascimento):
    #Recebe de ano de nascimento e retorna qual a idade atual
    ano_atual = 2025
    return ano_atual - ano_nascimento

#Exemplo de uso 
print(idade(1990))
print(idade(2006))
print(idade(2012))

print("Em que ano você nasceu?")
ano = int(input())
print("Sua idade atual é", idade(ano))