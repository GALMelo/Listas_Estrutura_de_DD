def compare(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

a = int(input())
b = int(input())

print(compare(a, b))
