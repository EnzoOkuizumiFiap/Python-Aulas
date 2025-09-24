print('Insira um valor inteiro:')

try:
    numero = int(input())
    resultado = 5 / numero
    print(f'5/{numero} = {resultado}')

except ValueError:
    print('Foi fornecido um input que não pode ser convertido para número inteiro.')
except KeyboardInterrupt:
    print('O programa foi interrompido e portanto não foi possível ler dados.')
except ZeroDivisionError:
    print('Não é possível dividir por zero, portanto a conta não foi realizada.')

# o próximo bloco pega qualquer outra exceção
except Exception as e:
    print(f'Ocorreu um erro desconhecido: {e}')
    
# o bloco do finally é executado ao final, independente de qual dos casos acima tenha chegado ao fim
finally:
    print('O programa está sendo encerrado.')