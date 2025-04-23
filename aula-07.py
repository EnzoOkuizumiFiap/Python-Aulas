'''
Operadores lógicos juntam duas (ou mais) expressões lógicas em um único resultado.

Operadores:

Operador "or" (Ou)
-Fica verdadeiro contanto que uma das expressões seja verdadeira

Operadores "and" (E)
-Fica verdadeiro só se todas as expressões são verdadeiras

Operador "not" (Não)
-Inverte o resultado (transforma True em False e vice-versa)
'''

x = 3
y = 5
mensagem = 'oi'

if x > 8 or y < 10:
    print("Operador OR disse que está Ok")
else: 
    print("Operador OR disse que NAÕ está Ok")

if x > 8 and y < 10:
    print("Operador AND diz que está ok")
else:
    print("Operador AND diz que NÃO está Ok")

if x <= 8: #if not x > 8:
    print("X não é maior que 8")
else: 
    print("X é maior que 8")