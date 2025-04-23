#Sintaxe de colchetes [] para acessar item específico dentro de sequência de dados

mensagem = 'está é uma string'

#Mostra o caractere na índice 2 da string
#Atenção: Começamos do índice 0, portanto índice 2 é o terceiro caractere (t)

print('Caractere no índice 2 é:',mensagem[2]) 

print("Vamos mostrar a string, um caractere por vez:")

i = 0
while i < len(mensagem):
    print(mensagem[i])
    i = i + 1

