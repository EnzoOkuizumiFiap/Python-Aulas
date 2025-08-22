#Usando try e loop
ANO_ATUAL = 2025

def idade (ano_nascimento):
    return ANO_ATUAL - ano_nascimento

#Coloque o try/except em um loop para tentar de novo
#Até que o usuário digite uma entrada válida

def main():
    print("Em que ano você nasceu?")

    execucao = True
    while execucao == True:
        try:
            ano = int(input())
            print("Sua idade é", idade(ano))
            execucao = False
        except:
            print("Entrada inválida.")
            Valor = input("Deseja executar novamente? Y/N ").strip().upper()
            if Valor == "Y":
                print("Executando novamente...")
                main()
            else:
                print("acabou... Não sobrou nada para o beta, murray.")
                execucao = False
    print("\nTerminando...")

main()
