import requests

NOME_ARQUIVO = 'https://open.er-api.com/v6/latest/USD'

def abre_json(nome_arquivo):
    if nome_arquivo.startswith('http'):
        resposta = requests.get(nome_arquivo)
        return resposta.json()
    
def mostra_cambio(dicionario_cambio, moeda_alvo):
    if moeda_alvo not in dicionario_cambio['rates']:
        print('Moeda desconhecida!')
    else:
        print(f' Câmbio: 1 USD = {dicionario_cambio['rates'][moeda_alvo]} {moeda_alvo}')

def mostra_todos_cambios(dicionario_cambio):
    for moeda, valor in dicionario_cambio['rates'].items():
        print(f'1 USD = {valor} {moeda}')

def mostra_moedas_abaixo_de_valor(dicionario_cambio, valor_limite):
    print(f'Moedas com valor abaixo de {valor_limite}:')
    for moeda, valor in dicionario_cambio['rates'].items():
        if valor < valor_limite:
            print(f'1 USD = {valor} {moeda}')

def mostra_cambio_fortes(dicionario_cambio):
    print("Moedas que valem mais que o dólar:")
    for moeda, valor in dicionario_cambio['rates'].items():
        if valor < 1:
            print(f'1 {moeda} = {1/valor:.2f} USD')


def main():
    dados_cambio = abre_json(NOME_ARQUIVO)

    print('Dados lidos com sucesso!')
    print(f'Tipo de dado: {type(dados_cambio)}')
    print(f'Data de atualização dos dados: {dados_cambio['time_last_update_utc']}')

    print(f'Cambio do dolar para o real: 1 USD = {dados_cambio['rates']['BRL']}')

    #Mostra câmbio para todas as moedas
    mostra_todos_cambios(dados_cambio)

    #Mostra câmbio para moedas abaixo de um valor específico
    valor_limite = float(input('\nDigite o valor limite para filtrar moedas: '))
    mostra_moedas_abaixo_de_valor(dados_cambio, valor_limite)

    print("\n")
    #Mostrar moedas que valem mais que o dolár
    mostra_cambio_fortes(dados_cambio)


    moeda_desejada = input('\nDigite uma moeda (ex: USD, BRL, GBP): ').upper()
    mostra_cambio(dados_cambio, moeda_desejada)
        

if __name__ == '__main__':
    main()
