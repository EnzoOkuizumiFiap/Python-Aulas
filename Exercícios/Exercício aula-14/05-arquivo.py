# Vamos acessar um arquivo para Escrita (criar)
# Temos que passar como parâmetro o modo 'w', de "write" (escrita)
with open('./Exercícios/saida_python.txt', mode = 'w', encoding = 'uft-8') as arquivo:
    arquivo.write("Olá, mundo!\n") #Precisa adicionar manualmente quebra de linha
    arquivo.write("Tchau, até mais!")

'''

Obs: Modos de acesso

* 'r' (read) = modo de leitura, é o modo padrão se não passarmos esse parâmetro.
    -> Esse modo simplesmente lê o conteúdo do arquivo, sem modificar

* 'w' (Write) = modo de escrita
    -> Se o arquivo não existe, ele é criado
    -> Se o arquivo existe, seu conteúdo é zerado!! (Cuidado!)
    -> Permite escrever no arquivo

* 'a' (append) = modo de adição
    -> Se o arquivo não existe, ele é criado
    -> Se o arquivo já existe, seu conteúdo é MANTIDO
    -> Permite escrever novas informações no final do arquivo

'''
