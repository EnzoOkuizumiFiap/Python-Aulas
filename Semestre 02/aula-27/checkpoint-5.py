import json
import requests
URL = 'https://uselessfacts.jsph.pl/api/v2/facts/random' 
ARQUIVO_LOCAL = './Semestre 02/aula-27/fato_padrao.json' #Precisa mudar o caminho na sua máquina...

def conexao():
    #Realizando conexão e tratamento de erros
    try: 
        resposta = requests.get(URL)
        resposta.raise_for_status()

        fato_inutil = resposta.json()
        print(f"\nFrase Inútil = {fato_inutil['text']}")
    except Exception as e:
        print(f"\nErro ao acessar a API: {e}")
        print("\nExibindo Frase Padrão do Arquivo Local")

        try:
            with open(ARQUIVO_LOCAL, 'r', encoding='utf-8') as arquivo:
                fato_local = json.load(arquivo)
                print(f"\nFrase Padrão = {fato_local['text']}")
        except Exception as e:
            print(f"\nErro ao acessar o arquivo local: {e}")


def continua():
    while True:
        try:
            #Mostrando opções para o usuário
            opcao = int(input("\nO que deseja: \n1 - Ver um fato novo \n2 - Sair \nDigite a opção: "))

            if opcao == 1:
                conexao()
            elif opcao == 2:
                print("Saindo do programa!")
                break
            else:
                print("valor inválido...")
        
        #Tratamento de erros
        except KeyboardInterrupt:
            print('O programa foi interrompido e portanto não foi possível ler dados.')
        except ValueError:
            print('Input inválido: não é um número inteiro.')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')


def main(): 
    continua()

main()
