def sum_fibo(n):
	a = 0
	b = 1
	y = 0

	for x in range(n-1):

		c = a + b
		a = b
		b = c
		y += a
	return y

n = int(input('Digite um valor: '))
print(sum_fibo(n))