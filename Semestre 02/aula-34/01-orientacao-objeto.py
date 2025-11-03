#Como fazer classes em python

'''
Exercício: Modificar a classe abaixo para ter também atributo RM.
(Pode colocar também turma e curso se quiser!)

Você irá modificar o construtor para receber o RM e criar o atributo com o valor recebido.
Modifique também o método __str__ para incluir o RM na string criada...
'''

class Aluno: 
    def __init__(self, nome):
        self.nome = nome
    
    def muda_nome(self, novo_nome):
        self.nome = novo_nome
    
    #__str__ diz ao Python como transformar objeto dessa classe em string (Por exemplo, para printar)
    def __str__(self):
        return f'{self.nome}'

# Abaixo, o programa que usa a classe acima

aluno1 = Aluno(nome = 'Enzo')

#Em chamadas, o parâmetro "self" não aparece (é implícito)
aluno1.muda_nome(novo_nome = "Enzo Okuizumi")

aluno2 = Aluno(nome = 'Luiz')

print(f"Aluno 1: {aluno1}")
print(f"Aluno 2: {aluno2}")
