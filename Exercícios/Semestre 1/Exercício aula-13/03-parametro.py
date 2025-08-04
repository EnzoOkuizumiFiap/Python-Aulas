#Função pode receber Parâmetros (Dados sobre quais ela vai operar)
#Parâmetros são variáveis que colocamos entre os parênteses do def

def cumprimento(nome):
    #No corpo da função, a variável "nome" carrega o valor que a função recebeu ao ser chamada
    print("Bom dia", nome)

#A chamada abaixo provoca a execução do corpo da Função

#A variável "nome" (no def da função) é inicializada com valor 'João'
cumprimento("João")

#Essa chamada inicializa com valor "Alice"
cumprimento("Alice")

#Essa chamada incializa nome com valor 3
cumprimento(3)
