print('Qual a tabuada desejada? (Digite número inteiro)')
T = int(input())
N = 1
while N <= 10:
    print(T*N)
    N = N + 1

"""
Esquema clássico do while:

1.  INICIALIZAÇÃO DA VARIÁVEL
2.  WHILE <CONDIÇÃO ENVOLVENDO A VARIÁVEL>:
        <TAREFA ENVOLVENDO A VARIÁVEL>
        <ATUALIZAÇÃO DA VARIÁVEL>

(Geralmente a lógica fica mais simples e limpa quando
deixamos a atualização da variável como última coisa)
"""