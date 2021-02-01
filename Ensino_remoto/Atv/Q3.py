list = []
length = int(input())

list = input().split()
place = 1
x = 0
lowest = int(0)

while x < len(list):
    if int(list[x]) <= int(lowest):
        lowest = list[x]
        place = x
        x += 1
    else:
        x+=1

if len(list) > length:
    print('Sua lista é maior que o esperado, mas:')
    print('Menor valor:', lowest)
    print('Posicao:', place)

elif len(list) < length:
    print('Sua lista é menor que o esperado, mas:')
    print('Menor valor:', lowest)
    print('Posicao:', place)

else:
    print('Menor valor:', lowest)
    print('Posicao:', place)