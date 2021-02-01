lines = int(input())
palíndromos = []

for x in range(lines):
    frases = input().split()
    qty = 0
    for y in frases:
        if y == y[::-1]:
            qty += 1
    palíndromos.append(qty)

for z in palíndromos:
    print(z)