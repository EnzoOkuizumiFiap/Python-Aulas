'''
Exercício:

Pergunte ao usuário: *nome *sobrenome

Mostre as iniciais do usuário

Exemplo: Nome = João Sobrenome = Souza
Iniciais: J. S.

Para isso, você irá acessar os caracteres na posição 0 do nome e sobrenome
'''

Nome = input("Nome: ")
Sobrenome = input("Sobrenome: ")

print(f"Inicias do seu nome: {Nome[0] + '.' + Sobrenome[0] + '.'}")