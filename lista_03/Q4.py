def natural(inteiro):
    if (inteiro < 0):
        pass
    else:
        lista.append(inteiro)
        return natural(inteiro-1)

def inverso(inteiro):
    if (len(inteiro) == 0):
        pass
    else:
        lista_inversa.append( lista[len(inteiro)-1] )
        return inverso(inteiro[:-1])


lista = []
lista_inversa = []
natural(int(input("Adicione um número positivo: ")))
inverso(lista)
print(lista_inversa)