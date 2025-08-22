'''
Dicionário é uma sequência de dados similiar à lista.

Na lista, os elementos são identificados por suas posições (ÍNDICES).

Os índices são 0, 1, 2, 3,... (sempre em sequência)

No dicionário, os elementos são identificados por CHAVES.
As chaves são identificadores únicos de cada dado.
Podem ser inteiros (sem precisar ser sequencial), float, string, entre outros.

O mais usado é string

'''

cliente = {} # Criando dicionário vazio

print("Qual o nome do cliente?")
#O dicionário não tinha chave "nome", mas essa linha está criando esse campo
cliente['nome'] = input()

print("Qual o CPF do cliente?")
cliente['cpf'] = input()

print("Qual o telefone do cliente?")
cliente['telefone'] = input()

print(f"Nome do cliente {cliente['nome']}")
print(f"Telefone do cliente {cliente['telefone']}")
print(f"CPF do cliente {cliente['cpf']}")


'''
O dicionário não tem "append" como a lista.
As chaves são criadas no momento em que as usamos pela primeira vez para escrita.
'''