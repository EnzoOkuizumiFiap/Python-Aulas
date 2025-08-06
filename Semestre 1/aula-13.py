# Resumo da Aula 13 - Funções em Python

# 1. Chamada de Funções Pré-existentes:
# - Python possui diversas funções embutidas que podem ser chamadas para realizar tarefas.
# - Exemplo: max(lista) retorna o maior valor de uma lista, min(lista) retorna o menor.
numeros = [10, 20, 5, 30]
maior_numero = max(numeros)
menor_numero = min(numeros)
print(f"Maior: {maior_numero}, Menor: {menor_numero}")

# 2. Definição de Funções (def):
# - O comando `def` é usado para criar (definir) novas funções.
# - Sintaxe:
#   def nome_da_funcao():
#       # Corpo da função (código a ser executado quando a função é chamada)
#       print("Esta função foi chamada!")
# - O corpo da função só é executado quando a função é explicitamente chamada.
# Exemplo:
def saudacao():
    print("Olá! Bem-vindo(a).")

saudacao() # Chamada da função

# 3. Parâmetros em Funções:
# - Funções podem receber dados para processar, chamados de parâmetros (ou argumentos).
# - Parâmetros são definidos entre os parênteses na declaração da função.
# - Quando a função é chamada, os valores passados são atribuídos aos parâmetros.
# Exemplo:
def cumprimentar_pessoa(nome):
    print(f"Olá, {nome}!")

cumprimentar_pessoa("Ana")
cumprimentar_pessoa("Carlos")

# 4. Retorno de Valores (return):
# - Funções podem devolver um resultado para quem a chamou usando a instrução `return`.
# - Quando `return` é executado, a função termina e o valor especificado é retornado.
# Exemplo:
def calcular_area_quadrado(lado):
    area = lado * lado
    return area

area_calculada = calcular_area_quadrado(5)
print(f"A área do quadrado é: {area_calculada}")
print(f"A área de um quadrado de lado 7 é: {calcular_area_quadrado(7)}")

# 5. Funções com Vários Parâmetros:
# - Funções podem ter múltiplos parâmetros, separados por vírgulas.
# - Ao chamar a função, é preciso fornecer valores para todos os parâmetros na ordem correta (a menos que se use argumentos nomeados).
# Exemplo:
def somar(a, b):
    return a + b

resultado_soma = somar(10, 15)
print(f"10 + 15 = {resultado_soma}")

def maior_de_tres(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
print(f"O maior entre 5, 2, 8 é: {maior_de_tres(5, 2, 8)}")

# 6. Funções Operando sobre Sequências:
# - Funções podem receber sequências (como listas ou strings) como parâmetros.
# - Dentro da função, podemos acessar elementos da sequência usando índices.
# Exemplo:
def obter_primeiro_elemento(sequencia):
    if len(sequencia) > 0:
        return sequencia[0]
    else:
        return None # Ou levantar um erro

minha_lista = [100, 200, 300]
minha_string = "Python"
print(f"Primeiro da lista: {obter_primeiro_elemento(minha_lista)}")
print(f"Primeiro da string: {obter_primeiro_elemento(minha_string)}")
print(f"Primeiro de lista vazia: {obter_primeiro_elemento([])}")

# Observações:
# - Funções ajudam a organizar o código, tornando-o mais modular, reutilizável e legível.
# - Uma função pode ter múltiplos comandos `return`, mas apenas o primeiro encontrado será executado, encerrando a função.
#   Isso é útil para diferentes caminhos lógicos dentro da função.
def verificar_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar" # Este return só é alcançado se o primeiro não for
print(f"4 é {verificar_par(4)}")
print(f"7 é {verificar_par(7)}")