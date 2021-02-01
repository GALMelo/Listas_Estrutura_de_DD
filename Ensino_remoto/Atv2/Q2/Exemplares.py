from Q2.Livro import Livro

class Exemplar:
    def __init__(self, livro, data_aquisicao, custo):
        self.livro = livro
        self.data_aquisicao = data_aquisicao
        self.custo = custo