from math import sqrt
def hipotenusa(ca, cb):
    return sqrt((ca * ca)+(cb* cb))

ca = int(input('Digite um valor para o cateto A: '))
ca = int(input('Digite um valor para o cateto B: '))
print(hipotenusa(ca, cb))
