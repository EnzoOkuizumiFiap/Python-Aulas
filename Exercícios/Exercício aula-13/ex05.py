'''
Calculadora interativo com menu e operações em funções
'''

def mostra_menu():
    print("Escolha uma opção: \n0 - Encerrar o programa \n1 - Soma \n2 - Divisão")
    
def le_dois_numeros():
    print("Digite o primeiro número:")
    x = int(input())
    print("Digite o segundo número:")
    y = int(input())
    return x, y
    
def funcionalidade_soma():
    print("Vamos realizar soma.")
    x, y = le_dois_numeros()
    print("Resultado:", x + y)
    
def funcionalidade_divisao():
    print("Vamos realizar divisão.")
    x, y = le_dois_numeros()
    print("Resultado:", x / y)    
    
    
#retorna opção do usuário (número inteiro)
def pega_opcao():
    opcao = input()
    return int(opcao)

def main(): 
    em_execucao = True
    
    while em_execucao:
        mostra_menu()
        opcao = pega_opcao()
        
        if opcao == 0:
            print("Encerrando o programa...")
            em_execucao = False
        elif opcao == 1:
            funcionalidade_soma()
        elif opcao == 2:
            funcionalidade_divisao()
        else:
            print("Opção inválida")
            
main()