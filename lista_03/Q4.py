def nat(n):
    
    if n < 0:
        return ""
    if n == 0:
        return "{}" .format(n)

    return "{}, {}".format(nat(n-1), n) 

print(nat(5))