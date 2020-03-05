def inverte(text):
	if len(text) == 0:
		return ""

	s2 = text[:-1]
	return text[-1] + inverte(s2)


print(inverte("gabriel afonso"))
