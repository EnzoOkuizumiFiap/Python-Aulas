""""
#Revisão do conteúdo
    - Breve revisão dos assuntos para o CP 3
        * Laço "for" (percorrimento de sequências)
        * Listas
        * Funções
    - Resolução dos exercícios restantes de função (Conforme o tempo permita)
"""

'''
Tópico 1: estrutura "for"
O for serve para percorrer uma sequência de dados.
'''

#String é sequência de caracteres
msg = 'bom dia'
for item in msg:
    print(item) #Printa cada caractere da string msg


#range: intervalo de número inteiros (sequência de números)
for n in range(3, 10):
    print(n)

'''
range tem três parâmetros possíveis: (inicio, fim, passo)
O intervalo começa no inicio, vai de "passo em passo".

exemplo: range(3, 10, 2) é a sequência: 3, 5, 7, 9

quando o passo é omitido, considera-se igual a 1.
quando o inicio é omitido, considera-se igual a 0.

range(5) é a sequência 0, 1, 2, 3, 4
'''

# -----------------------------------------------------------------------------

'''
Tópico 2: lista.

Sequência de dados QUAISQUER.
Em Python, lista pode ser heterogênea, isto é, os dados presentes nela podem ser de diferentes tipos. 

(Mas é comum na prática ela acabe sendo homogênea, isto é, é que os dados sejam todos do mesmo tipo)

'''

lista_heterogenea = [3.14, 'bom dia', 8, False, [1, 2, 3], 'ok']

print('Criei uma lista de tamnho', len(lista_heterogenea))

for item in lista_heterogenea:
    print(item)

'''
Obs: Len() retorna o tamanho de uma sequência de dados

exemplo:
    len('ok') -> 2
    len(range(1, 4)) -> 3
    len([4, 5, 0, 1]) -> 4
'''

'''
Os elementos de uma lista podem ser acessados através do índice
Os índices começam do zero (0): 0, 1, 2, 3...
'''

temperaturas = [15.7, 16.4, 18.0, 19.8, 22.5, 21.0, 20.6]

print(temperaturas[3]) #Imprime 19.8, "quarto" elemento da lista.

temperaturas[0] = 14.9 #Substitui o primeiro elemento da lista por 14.9
print(temperaturas)

#Operações prontas envolvendo lista:
soma = sum(temperaturas)
minimo = min(temperaturas)
maximo = max(temperaturas)

print(f"Nessa lista de temperaturas, a mínima foi {minimo}, e a máxima foi {maximo} e a soma {soma}")

#ordena a lista, ou seja, rearranja em ordem crescente
temperaturas.sort()
print(temperaturas)

#Append permite colocar novos itens na lista

compras = ['maça', 'iogurte']
compras.append('alface')
print(compras)

#Padrão comum: Começar com lista vazia e adicionar itens ao longo da execução

valores = [] #lista vazia

for n in range(3, 10, 2):
    valores.append(n ** 2)

print(valores)

# -----------------------------------------------------------------------------

'''
Tópico 3: Funções

    Uma função é um bloco de código ao qual damos um nome.
    Para executar esse bloco de código, basta CHAMAR a função, usando seu nome.

    Já usamos diversas funções do Python: print(), input(), len(), etc.

    Chamada de função é sempre dessa forma: 
    
    nome_da_função()

    (Se a função precisa de parâmetros, colocamos os parâmetros entre os parênteses.)

    Nosso programa é executado linha por linha.
    Ao chegar em uma chamada de função, o fluxo do programa passa a executar o código da função. Ao término da função, o fluxo de execução é devolvido ao programa principal.

'''

'''
Além de usar as funções prontas, nós podemos CRIAR nossas próprias funções usando o comando "def".

'''

def minha_funcao():
    print("Minha função é executada!")

minha_funcao()
minha_funcao()
minha_funcao()

#Função pode receber parâmetro

def cumprimenta(nome):
    print("Bom dia", nome)

cumprimenta("Enzo")
cumprimenta("Luiza")
cumprimenta("Sara")

#Função pode retornar um valor como resultado

def quadrado(x):
    resultado = x ** 2
    return resultado

#O valor da expressão "quadrado(12)" é aquilo que a função retornar
y = quadrado(2)
print("Resultado do quadrado:", y)


#Múltiplos parâmetros devem ser separados por vírgula

'''
Essa função recebe dois valores, x e y, retorna o menor dentre eles
'''

def menor(x, y):
    if x < y:
        return x
    else:
        return y
    
print(menor(3, 8)) #Printa 3
print(menor(11, 4)) #Printa 4

#Função pode retornar mais do que um valor de uma vez

def min_max(lista):
    '''
    Função recebe uma lista e retorna o mínimo e máximo valores, nessa ordem
    '''
    minimo = min(lista)
    maximo = max(lista)
    return minimo, maximo

temperaturas = [15.7, 16.4, 18.0, 19.8, 22.5, 21.0, 20.6]

#Como a função retorna duas coisas, preciso de duas variáveis para receber
minimo, maximo = min_max(temperaturas)

print(f"Min = {minimo} \nMax = {maximo}")

