#Vamos acessar a API de câmbio diretamente pelo Python, em vez de baixar o JSON manualmente
import requests

URL = 'https://open.er-api.com/v6/latest/GBP'

def main():
    #resposta guarda o que o servidor me responder. Ela é um objeto e tem vários atributos
    resposta = requests.get(URL)

    if resposta.status_code == 200:
        cambio = resposta.json()
    else:
        print("Servidor não respondeu")
        exit() #termino o programa

    print(cambio) #Printamos o dicionário todo, só pra ver se deu certo

main()