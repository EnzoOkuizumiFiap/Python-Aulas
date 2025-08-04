'''
Exercício:

Use while para mostrar na tabela a tabuada do 7

(depois, em vez da tabuada do 7, pegue por input
a tabuada desejada)
'''
import time

print('Escolha uma tabuada')

t = int(input())
x = 0

while x <= 10:
    print(f'{t} x {x} = {t*x}')
    x += 1
    time.sleep(.75)

