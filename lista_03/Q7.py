def fatorial(n):
	if n > 0:
		return n * fatorial(n-2)
	else:
		return 1


n = int(input("Digite o valor que deseja saber o fatorial: "))
print(fatorial(n))