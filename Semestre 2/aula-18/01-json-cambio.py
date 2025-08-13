import json

# resolução do exempo 5 da aula passada

'''
Primeiro, salvamos localmente (como GBP.json) o arquivo acessível em
https://open.er-api.com/v6/latest/GBP

(dados de câmbio da moeda GBP, isto é, libra esterlina,
para outras moedas.)
'''

def main():
    with open('./semestre 2/aula-18/GBP.json') as arquivo:
        # esse arquivo descreve um único objeto, portanto vem
        # para nosso programa na forma de dicionário
        dados_gbp = json.load(arquivo)
    
    print('Taxas de câmbio de GBP para outras moedas:')
    # nesse JSON, é o campo "rates" que tem as taxas de câmbio
    # (o restante são metadados)
    print(dados_gbp['rates'])

    print('---')

    gbp_para_cad = dados_gbp['rates']['CAD']
    print(f'1 GBP = {gbp_para_cad} CAD')

    '''
    fazer prints similares ao anterior, para mostrar:
        * câmbio de GBP para BRL;
        * câmbio de GBP para USD

    (resolução no início da próxima aula)
    '''
    
    gbp_para_brl = dados_gbp['rates']['BRL']
    print(f'1 GBP = {gbp_para_brl} BRL')

    gbp_para_usd = dados_gbp['rates']['USD']
    print(f'1 GBP = {gbp_para_usd} USD')
    
main()
