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

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)