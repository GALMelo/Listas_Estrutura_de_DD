def repetida(p,k):
	if len(p) == 0:
		return 0

	if p[0] == k:
		return 1 + repetida(p[1:], k)

	else:
		return 0 + repetida(p[1:], k)


print(repetida("estruturauuuuuu", "u"))

