'''
Peça para o usuário digitar uma palavra

Imprima quantas vezes aparece a letra 'e' na mensagem digitada
'''

mensagem = input("Digite uma mensagem qualquer:")

i = 0
contagem = 0
while i < len(mensagem):
    if mensagem[i].lower() == 'e':
        contagem += 1
    i += 1

print("Número de ocorrências da Letra E:", contagem)