class Compra:
    compras_data = []

    def __init__(self, data, nomeComprador, cpfComprador, total):
        self.data = data
        self.nomeComprador = nomeComprador
        self.cpfComprador = cpfComprador
        self.total = total
        Compra.compras_data.extend((data, nomeComprador, cpfComprador, total))

    def listarCompras():
        for x in Compra.compras_data:
            print(x)
