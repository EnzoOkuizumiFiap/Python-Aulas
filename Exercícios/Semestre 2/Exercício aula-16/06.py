
def cumprimenta(nome = "Cliente", horario = None):
    if horario is None:
        print("Olá", nome)
    elif 5 <= horario <= 12:
        print("Bom dia", nome)
    elif 13 <= horario <= 18:
        print("Boa tarde", nome)
    elif 19 <= horario <= 23 or 0 <= horario <= 4:
        print("Boa noite", nome)

cumprimenta("Enzo", 14)
cumprimenta("Roberto", 3)
cumprimenta()
