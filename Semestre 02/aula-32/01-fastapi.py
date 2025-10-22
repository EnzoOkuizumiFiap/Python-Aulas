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


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)