#Exercício 04 Bônus

numero_pessoas = int(input("Quantas pessoas serão cadastradas? "))

idades = {} #Dicionário começa vazio

for i in range(numero_pessoas):
    nome = input('Digite o nome:')
    print('Digite a idade de', nome, ":")
    idade = int(input())
    
    #Registro os dados recebidos no dicionário
    idades[nome] = idade

#Printar sem ordem alfabética
print(idades)

#Printar mais bonito
for nome in idades:
    print(nome, 'tem', idades[nome], 'anos de idade.')
