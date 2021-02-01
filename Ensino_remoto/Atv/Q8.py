valorRs = int(input())
x = 0

while True:
    if valorRs >= 100:
        x = valorRs // 100
        valorRs = valorRs - (x * 100)
        print('{} nota(s) de R$100.'.format(x))
    elif valorRs >= 50:
        x = valorRs // 50
        valorRs = valorRs - (x * 50)
        print('{} nota(s) de R$50.'.format(x))
    elif valorRs >= 20:
        x = valorRs // 20
        valorRs = valorRs - (x * 20)
        print('{} nota(s) de R$20.'.format(x))
    elif valorRs >= 10:
        x = valorRs // 10
        valorRs = valorRs - (x * 10)
        print('{} nota(s) de R$10.'.format(x))
    elif valorRs >= 5:
        x = valorRs // 5
        valorRs = valorRs - (x * 5)
        print('{} nota(s) de R$5.'.format(x))
    elif valorRs >= 1:
        x = valorRs // 1
        valorRs = valorRs - (x * 1)
        print('{} nota(s) de R$1.'.format(x))
    else:
        break