from datetime import datetime

'''
Função que recebe um nome como parâmetro e cumprimenta esse nome de acordo com o horário
'''

def cumprimenta(nome):
    # campo hour traz a hora cheia atual
    hora_atual = datetime.now().hour    
    
    if hora_atual < 12:
        saudação = 'Bom dia'
    elif hora_atual < 18:
        saudação = 'Boa tarde'
    else:
        saudação = 'Boa noite'
    
    print(saudação, nome)
    
def main():        
    print("Olá! Qual o seu nome?")
    nome = input()
    cumprimenta(nome)
    
main() #Chama o main