def is_perfect(number):
    divisores = 0
    for x in range(number, 0, -1):
        if number % x == 0:
            divisores += x
    if (number * 2) == divisores:
        return 'SIM'
    else:
        return 'NÃO'

array = []

while True:
    n = int(input())
    if n == -1:
        break
    else:
        array.append(n)

for y in array:
    print(is_perfect(y))