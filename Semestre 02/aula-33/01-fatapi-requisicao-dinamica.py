# Baseado no arquivo 03 da aula anterior (22/10)

from fastapi import FastAPI
from datetime import datetime 

# nosso app é uma instância da classe FastAPI
app = FastAPI()

# decorator diz qual caminho na aplicação web cai aqui
# o endereço '/' é a raiz da aplicação
@app.get('/')
async def root():
    dic = {
        'mensagem' : 'Hello, world!'
    }
    return dic

@app.get('/teste')
async def teste():
    return 'Acessando página teste'

estudantes = [ 'Amanda', 'Breno', 'Camila' ]
@app.get('/dados')
async def dados_completo():
    return estudantes

# essa parte {id} é um número qualquer que pode ser escrito no endereço da requisição
# por exemplo: 127.0.0.1:8000/dados/id/1 --> nesse caso, o {id} é 1
# a função recebe esse id como parâmetro
@app.get('/dados/id/{id}')
async def dados_por_id(id : int):
    if id >= len(estudantes):
        return 'Este id é inválido!'
    else:
        return estudantes[id]

@app.get('/dados/nome/{nome}')
async def dados_por_nome(nome : str):
    if nome in estudantes:
        return f'{nome} está na base de estudantes com id {estudantes.index(nome)}'
    else:
        return f'{nome} não está na base!'
    
@app.get('/oi/{nome}')
async def cumprimenta(nome : str):
    return f'Olá, {nome}!'

'''
Exercícios:

1. criar um endereço '/grupo' que retorna uma lista dos integrantes do seu grupo do Challenge

2. criar um endereço '/data' que retorna a data atual. (Usar datetime do Python)
'''

@app.get('/grupo')
async def grupo():
    dic = {
        'Nome grupo': 'Grupo ELM',
        'Nome do projeto': 'SimplesHC',
        'Integrantes': {
            'Integrante 1': 'Enzo Okuizumi',
            'Integrante 2': 'Lucas Barros',
            'Integrante 3': 'Milton Marcelino'
        },
        'turma': '1TDSPG'
    }
    return dic

@app.get('/data')
async def data():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")