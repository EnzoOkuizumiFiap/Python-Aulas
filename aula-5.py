#Aula 5 de Python - 24/03

#Use o datetime para mostrar a data e horário completos
import datetime

data_atual = datetime.datetime.now()

print('Estamos na hora', data_atual.hour)
print('Estamos no minuto', data_atual.minute)
print('Estamos no segundo', data_atual.second)

print('Estamos no dia', data_atual.day)
print('Estamos no mês', data_atual.month)

print('Estamos no ano', data_atual.year)

#If e else com horários
if data_atual.hour > 18 < 24:
    print("Boa noite")
if data_atual.hour > 12 < 18:
    print("Boa tarde")
else:
    print("Bom dia")



#Usando If e Else para selecionar opções de cálculo
x = float(input("Digite um número:"))
y = float(input("Digite outro número:"))

print("Qual operação você deseja realizar: 1. Soma, 2. Multiplicação")

opcao = int(input())
if (opcao == 1):
    print(x + y)
else: 
    print(x * y)



#Se o usuário nasceu antes de 2001, diga que ele nasceu no século passado
idade = int(input("Em que ano você nasceu?"))

if idade < 2001:
    print("Você nasceu no século 20")
else:
    print("Você nasceu no século 21")
