import requests

# Exercício 1: modifique esse programa para acessar câmbio do GBP em vez de USD
# Exercício 2: perguntar para o usuário qual a moeda de origem

URL_BASE = 'https://open.er-api.com/v6/latest/'

def main():
    moeda_origem = input("Digite uma moeda ORIGEM para cambiar:")
    URL = URL_BASE + moeda_origem
    resposta = requests.get(URL)

    if resposta.status_code == 200:
        cambio = resposta.json()

        print(f'Cambio do dolar para CAD: 1 USD = {cambio['rates']['CAD']} CAD.')

    else:
        print('Servidor respondeu com erro.')
        exit() # termino o meu programa

    print(cambio['rates'])

    print('Taxa de câmbio de USD para CAD:')
    print(cambio['rates']['CAD'])

main()