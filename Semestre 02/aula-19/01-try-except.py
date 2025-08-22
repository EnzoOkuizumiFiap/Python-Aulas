#Usando try e except
ANO_ATUAL = 2025

def idade (ano_nascimento):
    return ANO_ATUAL - ano_nascimento

def main():
    print("Em que ano você nasceu?")
    try:
        ano = int(input())
        print("Sua idade é", idade(ano))
    except:
        print("Entrada inválida.")
        
main()
