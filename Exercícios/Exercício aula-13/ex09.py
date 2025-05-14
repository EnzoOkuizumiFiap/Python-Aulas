def idade(ano_nascimento):
    #Recebe de ano de nascimento e retorna qual a idade atual
    ano_atual = 2025
    return ano_atual - ano_nascimento

datas = [1982, 2006, 1999, 2013, 2002, 1957]

print("Datas de nascimento cuja idade atual é maior que 20 anos:")

for data in datas:
    if idade(data) > 20:
        print(data)
