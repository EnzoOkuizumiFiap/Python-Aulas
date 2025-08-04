# Esse programa organiza o 02-dicionario.py criando função

def mostra_dados_cliente(cliente):
    print(f"Nome do cliente {cliente['nome']}")
    print(f"Telefone do cliente {cliente['telefone']}")
    print(f"CPF do cliente {cliente['cpf']}")
    print(f"Idade do cliente {cliente['idade']}")

cliente1 = {
    'nome': 'João',
    'cpf': '123',
    'telefone': '11949007573',
    'idade': 39
}

# Posso escrever em uma linha mas prejudica um pouco a leitura
cliente2 = {'nome': 'Ana', 'cpf': '123', 'telefone': 981, 'idade': 43}

mostra_dados_cliente(cliente1)
print("\n")
mostra_dados_cliente(cliente2)

'''
Poderíamos ter uma lista de clientes
(cada elemento da lista é um dicionário representando um cliente diferente)

Para mostrar todos os clientes, faríamos algo assim>
for cliente in clientes:
    mostra_dados_cliente(cliente)
'''