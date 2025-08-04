print("Qual o seu ano de nascimento?")
ano_nasc = int(input())
idade = 2025 - ano_nasc

if idade < 18:
    # As linhas sujeitas ao IF vêm com espaçamento em relação ao IF, isso se chama Indentação
    print("Você é menor de idade.")
else: 
    print("Você é maior de idade.")
