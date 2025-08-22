#Vamos reorganizar o arquivo 01-cambio.py
import json

NOME_ARQUIVO = './semestre 02/aula-20/USD.json'

def abre_json(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return json.load(arquivo)
    
def mostra_cambio(dicionario_cambio, moeda_alvo):
    if moeda_alvo not in dicionario_cambio['rates']:
        print('Moeda desconhecida!')
    else:
        print(f' Câmbio: 1 USD = {dicionario_cambio['rates'][moeda_alvo]} {moeda_alvo}')

def main():
    dados_cambio = abre_json(NOME_ARQUIVO)

    print('Dados lidos com sucesso!')
    print(f'Tipo de dado: {type(dados_cambio)}')
    print(f'Data de atualização dos dados: {dados_cambio['time_last_update_utc']}')

    print(f'Cambio do dolar para o real: 1 USD = {dados_cambio['rates']['BRL']}')

    moeda_desejada = input('\nDigite uma moeda (ex: USD, BRL, GBP): ').upper()
    mostra_cambio(dados_cambio, moeda_desejada)

        

if __name__ == '__main__':
    main()
