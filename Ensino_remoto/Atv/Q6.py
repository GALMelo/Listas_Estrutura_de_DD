filhos = 0
maiorSal = float(0)
salarios = 0
tdsSalarios = float(0)
todos = 0


while True:
    list = input().split(' ')
    if list[0] == "-1":
        break
    else:
        sal = float(list[0])
        flh = int(list[1])

        if sal <= 2500:
            salarios += 1
            if sal > maiorSal:
                maiorSal = sal
                filhos += flh
                tdsSalarios += sal
                todos += 1
        else:

            if sal > maiorSal:
                maiorSal = sal
                filhos += flh
                tdsSalarios += sal
                todos += 1

mediaSalario = (tdsSalarios / todos)
mediaFilhos = (filhos / todos)
salmin = (salarios / todos)

print('{:.2f} {:.1f} {} {:.2f}'.format(mediaSalario, mediaFilhos, maiorSal, salmin))
