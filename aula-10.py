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

print("\n")
'''
Vamos introduzir outra forma de realizar repetições em Python: o comando For.

O While é mais versátil/Universal.
O For se aplica apenas a alguns casos; Mas nesses casos, geralmente permite código mais simples e compacto.
(Em Python, o For serve apenas para percorrer sequência de dados.)

Um código assim vai printar todos os elementos de uma sequência de dados
for elemento in SEQUENCIA:
    print(elemento)

"for" significa "para".
A leitura da linha "for elemento in SEQUENCIA" é "para cada elemento uma sequência..."
'''
      
mensagem = 'exemplo'
for elemento in mensagem:
    print(elemento)


'''
Range

Um novo tipo de sequência de dados: o range, que é um intervalo numérico
'''

for n in range(2, 15):
    print(n)

'''
O For logo acima equivale ao seguinte código:

n = 2
while n < 15:
    print(n)
    n = n + 1
'''


'''
Alguns tipos sequênciais existentes em Python:

* string (Texto. Por exemplo, 'bom dia' é uma sequência com elementos.)

* range (Intervalo numérico. Por exemplo, range(6, 10) é intervalo contendo {6, 7, 8, 9})

* lista (Veremos em breve)

* tupla (Veremos um pouco em breve)

* dicionário (Veremos ainda esse bimestre)
'''