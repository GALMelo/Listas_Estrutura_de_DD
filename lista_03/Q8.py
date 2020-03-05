def eh_palindromo(texto):
    texto_tratado = ""
    texto = texto.lower()
    if " " in texto or "á" in texto or "é" in texto or "í" in texto or "ó" in texto or "ú" in texto:
        for x in texto:
            if x not in " .,:!?":
                if x in "áâãà":
                    texto_tratado += "a"
                elif x in "éêè":
                    texto_tratado += "e"
                elif x in "íîì":
                    texto_tratado += "i"
                elif x in "óôõò":
                    texto_tratado += "o"
                elif x in "úûù":
                    texto_tratado += "u"
                elif x in "ç":
                    texto_tratado += "u"
                else:
                    texto_tratado += x
    else:
        texto_tratado = texto
    if texto_tratado == '':
        return "É palíndromo"
    elif texto_tratado[0] == texto_tratado[-1]:
        return eh_palindromo(texto_tratado[1:-1])
    else:
        return "Não é palindromo"


print(eh_palindromo("E até o papa poeta é"))   # É palíndromo
print(eh_palindromo("Amo Omã. Se Roma me tem amores, amo Omã!"))  # É palíndromo
print(eh_palindromo("Me vê se a panela da moça é de aço, Madalena Paes, e vem."))  # É palíndromo
print(eh_palindromo("A base do teto desaba."))  # É palíndromo
print(eh_palindromo("A base da casa desaba."))  # Náo é palíndromo
