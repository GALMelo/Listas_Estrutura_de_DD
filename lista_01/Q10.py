def eh_bissexto(ano):
    
    if ano % 4 == 0 and ano % 100 != 0:
        return 1
    elif ano % 400 == 0:
        return 1
    else:
        return 0

def eh_data_valida(dia, mes, ano):
    
    if eh_bissexto(ano) == 1:
        if mes == 2:
            if 0 < dia < 30:
                return True
            else:
                return False
            
    else:
        if mes == 2:
            if dia > 28:
                return False
            else:
                return True
        else:
            if mes > 0 and mes <= 12:
                if dia > 0 and dia <= 31:
                    return True
                else:
                    return False
            else:
                return False



dia = int(input("Digite um dia: "))
mes = int(input("Digite um mes: "))
ano = int(input("Digite um ano: "))
print(eh_data_valida(dia, mes, ano))
