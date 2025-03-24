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