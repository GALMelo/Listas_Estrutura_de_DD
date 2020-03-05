def MDC(a, b):
	if b == 0:
		return a

	return MDC(b, a%b)

print(MDC(105,252))