mensagem = "exemplo de string"

#Usando o comando For é uma maneira mais simplificada de percorrer sequências de dados

#A cada passo da repetição, a variável "item" terá como valor um dos elementos na sequência de dados.
for caractere in mensagem: 
    print(caractere)



#For serve para percorrer qualquer sequência de dados

#Exemplo: String
mensagem = "bom dia"
for item in mensagem:
    print(item)

print() #Pular linha
#Exemplo: range (intervalo numérico)
for numero in range(3, 10):
    print(numero)

print()

#Exemplo: lista (Sequência de dados quaisquer)
compras = ['goiaba', 'alface', 'pao']
for item in compras:
    print(item)