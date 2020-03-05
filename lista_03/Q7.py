def fatorial(n):
	if n < 2:
		return 1

	if n % 2 == 1:
		return n * fatorial(n-1)
	else:
		return fatorial(n-1)


n = int(input("Digite o valor que deseja saber o fatorial: "))
print(fatorial(n))