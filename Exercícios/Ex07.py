
#Ex 06 Peça para o usuário informar por input uma opção dentre as seguites: a, b, ou c.
'''
Se a opção for "a", imprima uma mensagem "bom dia"
Se a opção for "b", imprima uma mensagem "boa tarde"
Se a opção for "c", imprima uma mensagem "boa noite"
Se for qualquer outra opção, imprima "opção inválida"
'''

choice = input("Escolha entre 'a', 'b' e 'c': ")

if choice == 'a':
    print("Bom dia!")
elif choice == 'b':
    print("Boa tarde!")
elif choice == 'c':
    print("Boa noite!")
else:
    print("Comando incorreto!")

#Ex 07 (Continuação do exercício 5) Leia as três notas, e em cada um dos casos, se a nota for menor que 0 (zero) ou maior que 10 (dez), diga que a entrada é inválida e o resultado não fará sentido. (No entanto, prossiga normalmente com a lógica do cálculo e das mensagens de Aprovado/Reprovado/Recuperação)

nota1 = float(input("Nota 1:"))
nota2 = float(input("Nota 2:"))
nota3 = float(input("Nota 3:"))

#Condição Composta
if nota1 < 0 or nota2 < 0 or nota3 < 0:
    print("Nota com valor incorreto! (<0)")
elif nota1 > 10 or nota2 > 10 or nota3 > 10:
    print("Nota com valor incorreto! (>10)")

resultado = (nota1 + nota2 + nota3) / 3
print("Sua nota é", resultado)

if resultado >= 7:
    print("Aprovado!")
elif resultado <= 3:
    print("Reprovado!")
else:
    print("Recuperação!")



#Ex 08 Exercício "DOAÇÃO DE SANGUE", parte 1. Pergunte a idade da pessoa. (Teremos outras versões desse exercício, levando em conta mais requisitos para doar sangue.) Se a idade estiver no intervalo de 18 a 60 anos, diga "Pode doar sangue!" Se a idade for menor de 18, mas pelo menos 16, pergunte se tem autorização dos pais. (Pode instruir a pessoa a digitar S ou N, por exemplo.) Imprima mensagens diferentes dependendo da resposta.


idade = int(input("Qual a sua idade? "))

if idade >= 18 and idade <= 60:
    print("Pode doar sangue!")
elif idade >= 16 and idade < 18:
    print("Você pode doar sangue, mas com autorização dos pais")
    escolha = input("Seus pais autorizaram a doação de sangue? S ou N: ")
    if escolha == 'S':
        print("Vamos doar sangue!")
    elif escolha == 'N':
        print("Okk, volte quando completar 18 anos")
else:
    print("Você não tem idade o suficiente para doar sangua, volta quando completar 18 anos")