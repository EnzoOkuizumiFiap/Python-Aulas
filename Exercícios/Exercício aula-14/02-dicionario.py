#Outra forma de criar o dicionário e já colocar alguns dados pré-existentes
cliente = {
    'nome': 'João',
    'cpf': '123',
    'telefone': '11949007573',
    'idade': 39
}

# Posso escrever em uma linha mas prejudica um pouco a leitura
exemplo = {'nome': 'Ana', 'cpf': '123', 'telefone': 981, 'idade': 43}

print(f"Nome do cliente {cliente['nome']}")
print(f"Telefone do cliente {cliente['telefone']}")
print(f"CPF do cliente {cliente['cpf']}")
print(f"Idade do cliente {cliente['idade']}")

print("\n")

print(f"Nome do cliente {exemplo['nome']}")
print(f"Telefone do cliente {exemplo['telefone']}")
print(f"CPF do cliente {exemplo['cpf']}")
print(f"Idade do cliente {exemplo['idade']}")
