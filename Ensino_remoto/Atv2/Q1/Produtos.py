class Produto:
    produto_data = []

    def __init__(self, idendtificador, nome, descricao, valor):
        self.identificador = idendtificador
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        Produto.produto_data.extend((idendtificador, nome, descricao, valor))

    def acharProduto(identificador):
        if identificador in Produto.produto_data:
            x = 0
            for x in range(len(Produto.produto_data)):
                if Produto.produto_data[x] == identificador:
                    return Produto.produto_data[x+3]
                else:
                    x += 4
        else:
            return 404
