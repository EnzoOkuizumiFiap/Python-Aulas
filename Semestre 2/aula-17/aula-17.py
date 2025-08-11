#01-dicionario
paciente = {} #dicionário vazio

#Vamos ler o campo nome por input e guardar no dicionário
paciente['nome'] = input('Qual o nome do paciente?')

#de forma similiar, Ler campos IDADE e QUEIXA, e guardar no dicionário
paciente['idade'] = int(input('Qual a sua idade?'))

paciente['queixa'] = input('Qual a sua queixa?')

#Ao final, mostrar como ficou o dicionário
print(paciente)


#===========================================================================
#02-dicionario

def le_dados_paciente():
    paciente2 = {}
    #lê dados do paciente como no programa anterior

    #nome
    paciente2['nome'] = input('Qual o nome do paciente?')
    
    #idade
    paciente2['idade'] = int(input('Qual a sua idade?'))

    #queixa
    paciente2['queixa'] = input('Qual a sua queixa?')

    return paciente2


def main1():
    paciente2 = le_dados_paciente()
    print("\nO paciente lido foi: ")
    print(paciente2)

#Chamamos main() para que o programa seja executado
main1()

#===========================================================================
#03-JSON
'''
Modificação do programa 02.
Lê os dados de paciente3 e guarda em um arquivo paciente3.json
'''
import json

def le_dados_paciente():
    paciente3 = {}
    paciente3['nome'] = input('Qual o nome do paciente?')
    paciente3['idade'] = int(input('Qual a sua idade?'))
    paciente3['queixa'] = input('Qual a sua queixa?')
    return paciente3


def main2():
    paciente3 = le_dados_paciente()
    print("\nO paciente lido foi: ")
    print(paciente3)
    
    with open('paciente3.json', 'w') as arquivo:
        json.dump(paciente3, arquivo, indent=4)

main2()

#===========================================================================
#04-JSON
'''
Esse programa só funciona se já existir o arquivo paciente3.json
Podendo ter sido criado manualmente ou pela execução do programa 03
'''

import json

def main3():
    with open('paciente3.json') as arquivo:
        paciente4 = json.load(arquivo)

        print("Li paciente3 do arquivo. Dados")
        print(paciente4)

main3()

#===========================================================================
#05-json-cambio

'''
Passo 1: Salvamos localmente (Como usd.json) o arquivo acessível em https://open.er-api.com/v6/latest/USD
(dados de câmbio da moeda USD)
'''

import json

def main4():
    with open('USD.json') as arquivo:
        dados_usd = json.load(arquivo)

    with open('brl.json') as arquivo:
        dados_brl = json.load(arquivo)

    with open('GBP.json') as arquivo:
        dados_gbp = json.load(arquivo)
    
    print("Taxas de câmbio de USD para outras moedas: ")
    #Nesse JSON, é o campo "rates" que tem as taxas de câmbio
    #(O restante são metadados)
    print(dados_usd['rates'])

    print('---')
    usd_para_cad = dados_usd['rates']['CAD']
    print(f'1 USD = {usd_para_cad} CAD')

    print('---')
    brl_para_cad = dados_brl['rates']['CAD']
    print(f'1 BRL = {brl_para_cad} CAD')

    print('---')
    gbp_para_cad = dados_gbp['rates']['CAD']
    print(f'1 gbp = {gbp_para_cad} CAD')

main4()

#===========================================================================
#06-json-cambio-http

import requests

def main5():
    moedas = ['USD', 'BRL', 'GBP']
    dados = {}
    
    for moeda in moedas:
        url = f'https://open.er-api.com/v6/latest/{moeda}'
        resposta = requests.get(url)
        resposta.raise_for_status() # Verifica se a requisição foi bem-sucedida
        dados[moeda] = resposta.json()
    
    print("Taxas de câmbio para CAD:")
    print('---')

    for moeda in moedas:
        taxa = dados[moeda]['rates']['CAD']
        print(f'1 {moeda} = {taxa} CAD')

main5()
