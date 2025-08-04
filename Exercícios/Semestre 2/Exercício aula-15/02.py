#Escreva um progama que lê um número inteiro N por input e printa "ok" se N for múltiplo de 3. Se N não é múltiplo de 3, o programa mostra o resto da divisão de N por 3.

num = int(input("Digite um número Inteiro:"))

if num % 3 == 0: 
    print("ok!")
else:
    print(num % 3)
    