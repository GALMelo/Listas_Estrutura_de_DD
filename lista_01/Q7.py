def compare(dia):
    if (dia == 1):
        dia = "Domingo"
        return dia
    elif (dia == 2):
        dia = "Sabado"
        return dia
    elif (dia == 3):
        dia = "Segunda"
        return dia
    elif (dia == 4):
        dia = "Terça"
        return dia
    elif (dia == 5):
        dia = "Quarta"
        return dia
    elif (dia == 6):
        dia = "Quinta"
        return dia
    elif (dia == 7):
        dia = "Sexta"
        return dia
    else:
        dia = "Valor Inválido"
        return dia

dia = int(input())

print(compare(dia))
