# Usando except... Podemos fazer vários except...
# (Baseado no programa 01, não no 02, para simplificar a lógica)

'''Exercício: no programa acima, simule a execução nos seguintes cenários:

Cenário 1: entrada do usuário é "1990" - tem um if que vê se ano_nascimento é menor que o ano_minimo e se ano_nascimento é maior que ano_atual... se for vdd, vai executar raise ValueError()
Cenário 2: entrada do usuário é "abc" - ValueError
Cenário 3: usuário dá Ctrl+C para encerrar o programa - KeyboardInterrupt

* Qual a sequência de execução das linhas em cada cenário?
* Qual linha gera erro (capturado no Except) no Cenário 2?
* Qual linha gera erro (capturado no Except) no Cenário 3?

Exercício: Replicar no programa acima a lógica do loop, como no programa 02.
'''

ANO_MINIMO = 1900
ANO_ATUAL = 2025

def idade(ano_nascimento):
    if ano_nascimento < ANO_MINIMO or ano_nascimento > ANO_ATUAL:
        raise ValueError()
    return ANO_ATUAL - ano_nascimento

def main():
    print('Em que ano você nasceu?')
    try:
        ano = int(input())
        print('Sua idade é', idade(ano))
    except ValueError: 
        # tratamento do erro ValueError
        print('Entrada inválida. Terminando...')
    except KeyboardInterrupt:
        # tratamento de Keyboard Interrupt
        print('Ocorreu um erro e o programa foi terminado.')

main()