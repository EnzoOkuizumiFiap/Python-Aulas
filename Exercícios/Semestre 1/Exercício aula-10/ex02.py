'''
Exercício: Peça ao usuário digitar uma palavra ou frase
Imprima uma letra por vez, mas pulando todas as ocorrências da letra 'a'
'''

mensagem = input('Digite uma mensagem qualquer:')

i = 0
while i < len(mensagem):
    #Imprime apenas as posições que não contêm 'a'
    if mensagem[i] != 'a':
        print(mensagem[i])
    i += 1
