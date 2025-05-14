#Recebe uma sequência de dados (lista, string...) e retorna o primeiro valor da sequência
def primeiro_valor(sequencia):
    primeiro = sequencia[0]
    return primeiro

lista = [3, 1, 4, 5, 9, 2, 6, 5]
mensagem = 'bom dia'

print("Primeiro elemento da lista: ", primeiro_valor(lista))
print("Primeiro elemento da mensagem: ", primeiro_valor(mensagem))
