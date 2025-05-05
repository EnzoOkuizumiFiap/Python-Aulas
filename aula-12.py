# A palavra-chave 'def' é usada para definir funções em Python

# Exemplo 1: Função simples que imprime uma saudação
def saudacao():
    print("Olá, mundo!")  # Esta função imprime uma saudação

# Chamando a função
saudacao()

# Exemplo 2: Função que recebe parâmetros e retorna um valor
def soma(a, b):
    return a + b  # A função retorna a soma de 'a' e 'b'

# Usando a função de soma
resultado = soma(3, 5)
print("O resultado da soma é:", resultado)

# Exemplo 3: Função com valor padrão para um parâmetro
def cumprimentar(nome="Visitante"):
    print(f"Olá, {nome}!")  # Se nenhum nome for passado, usa "Visitante"

# Chamando a função com e sem argumento
cumprimentar("Carlos")
cumprimentar()  # Usa o valor padrão "Visitante"
