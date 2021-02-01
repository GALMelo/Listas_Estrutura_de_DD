class Livro:
    def __init__(self, isbn, titulo, ano, lista_autores):
        self.isbn = isbn
        self.titulo = titulo
        self.ano = ano
        self.lista_autores = lista_autores

    def print(self):
        print(self.titulo)