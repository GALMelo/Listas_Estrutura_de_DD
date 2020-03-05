# 1° Questão de Função
# Eyder e Gabriel

def fatorial(n):
    x = n
    n = 1
    while (x >= 1):
        n = n * x
        x = x - 1
    return n

n = int(input("Adicione um Número inteiro: "))
a = int(0)

print(fatorial(n))
