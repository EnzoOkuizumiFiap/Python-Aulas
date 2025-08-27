# Exercício: implementar a função abaixo

def filtra_por_inicial(strings, inicial):
    resultado = []
    for letra in strings:
        if letra.startswith(inicial):
            resultado.append(letra)
    return resultado

def main():
    alunos = [ 'Alberto', 'Bruna', 'Carla', 'Douglas' ]
    alunos_com_b = filtra_por_inicial(alunos, 'B')
    print(alunos_com_b)

main()