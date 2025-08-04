'''
Explicação Comando Range()

O comando range() cria um intervalo de números inteiros

Forma geral:

 range(inicio, fim, passo)

 Cria o intervalo começando do número "inicio", parando antes do número "fim" e atualizando o valor de acordo com o especificado pelo "passo".

 Exemplo:
 range(1, 10, 2): Intervalo 1, 3, 5, 7, 9

 range(5, 0, -1): Intervalo 5, 4, 3, 2, 1
 _______________________________________________________________

 Forma com dois valores:
 range(inicio, fim)

 Quando o "passo" é omitido, é considerado igual a 1 por padrão.
 
 Exemplo:
 range(1, 10): Intervalo 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
 _______________________________________________________________
 
 Forma com um valor só:
 range(fim)

 Quando o "inicio" é omitido, é considerado igual a 0 (zero)

 Exemplo:
 range(5): Intervalo 0, 1, 2, 3, 4
 
'''