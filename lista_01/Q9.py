def eh_bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    else:
        return False

ano = int(input())
print(eh_bissexto(ano))
