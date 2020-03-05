def todos(n):
	if n > 0:
		print(n)
		return todos(n-1)
	
	else:
		return 0

n = int(input("Digite um valor inteiro positivo: "))
print(todos(n))
