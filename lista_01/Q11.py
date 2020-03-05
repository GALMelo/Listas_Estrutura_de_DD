def soma_numero(n):
    x = 0
    a = 0
    while True:
        if x < n:
            x += 1
            a += x
        else:
            break
    return a

n = int(input("Digite um numero: "))
print(soma_numero(n))