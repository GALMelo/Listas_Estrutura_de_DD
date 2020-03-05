def eh_primo(n):
    div = 1
    for x in range (1,n):
        if n / x == n // x :
            div += 1
        
    if div == 2:
        return False
    else:
        return True
           
            
n = int(input())
print(eh_primo(n))
