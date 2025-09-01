# Arquivo 07 da aula passada

# Vamos acessar a API de câmbio diretamente pelo Python,
# em vez de baixar o JSON manualmente.

# Exercício 1: mude a URL para acessar USD em vez de GBP
# Exercício 2: printe na tela a taxa de câmbio de USD para CAD

import requests

URL = 'https://open.er-api.com/v6/latest/'  

def main():
    # resposta guarda o que o servidor me responder
    resposta = requests.get(URL)

    if resposta.status_code == 200:
        cambio = resposta.json()

        print(f'Cambio do dolar para CAD: 1 USD = {cambio['rates']['CAD']} CAD.')
    else:
        print('Servidor respondeu com erro.')
        exit() # termino o meu programa

    # printamos o dicionário todo, só pra ver que deu certo
    print("\n", cambio['rates'])

main()