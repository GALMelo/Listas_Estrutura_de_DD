class Cliente:
    cliente_data = []

    def __init__(self, nome, cpf, rua, cep, cidade):
        self.nome = nome
        self.cpf = cpf
        self.rua = rua
        self.cep = cep
        self.cidade = cidade
        Cliente.cliente_data.extend((nome, cpf, rua, cep, cidade))
