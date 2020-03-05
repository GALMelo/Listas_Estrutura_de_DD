def compare(a,b,c):
    if (a > b > c):
        return a
    elif (a > c > b):
        return a
    elif (b > a > c):
        return b
    elif (b > c > a):
        return b
    elif (c > a > b):
        return c
    else:
        return c

a = int(input())
b = int(input())
c = int(input())
print(compare(a, b, c))
