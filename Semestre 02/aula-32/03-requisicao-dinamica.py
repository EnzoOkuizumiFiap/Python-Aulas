from fastapi import FastAPI
import uvicorn

#nosso app é uma instância da classe FastAPI
app = FastAPI()

# decorator diz qual caminho na aplicação web cai aqui
@app.get('/')
async def root():
    dic = {
        'mensagem': 'Hello, World!'
    }
    return dic

@app.get('/teste')
async def teste():
    return 'Acessando página teste'

@app.get('/challenge')
async def challenge():
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

estudantes = ['Amanda', 'Breno', 'Camila']
@app.get('/dados')
async def dados_completo():
    return estudantes

@app.get('/dados/id/{id}')
async def dados_por_id(id : int):
    if id >= len(estudantes):
        return 'Este id é inválida!'
    else:
        return estudantes[id]
    
@app.get('/dados/nome/{nome}')
async def dados_por_nome(nome : str):
    if nome in estudantes:
        return f'{nome} está na base de dados de estudantes com id {estudantes.index(nome)}'
    else:
        return f'{nome} não está na base de dados!'

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)