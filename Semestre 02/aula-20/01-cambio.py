import json

#Convenção: Variável com nome em MAIÚSCULAS é tratado como constante (valor não muda)
NOME_ARQUIVO = './semestre 02/aula-20/USD.json'

def main():
    with open(NOME_ARQUIVO, 'r') as arquivo:
        dados_cambio = json.load(arquivo)

    print('Dados lidos com sucesso!')
    print(f'Tipo de dado: {type(dados_cambio)}') # <class 'dict'> Traduzindo: dicionário
    print(f'Data de atualização dos dados: {dados_cambio['time_last_update_utc']}')

    print(f'Cambio do dolar para o real: 1 USD = {dados_cambio['rates']['BRL']}')

    #============================================================
    valor = input('Digite uma moeda (ex: USD, BRL, GBP): ').upper()
    
    if valor not in dados_cambio['rates']:
        print('Moeda desconhecida!')
    else:
        print(f' Câmbio: 1 USD = {dados_cambio['rates'][valor]} {valor}')
        

#Só executa main() se este arquivo for o princpal do programa
#(portanto, não executa se ele for, por exemplo, importado por outro arquivo)
if __name__ == '__main__':
    main()
