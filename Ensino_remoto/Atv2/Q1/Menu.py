from Q1.Compras import Compra
from Q1.Produtos import Produto
from Q1.Cliente.Cliente import Cliente


p = Produto
c = Compra

while True:
    print('\nMenu:'
          '\nDigite 1 para Cadastrar produto',
          '\nDigite 2 para Cadastrar compra',
          '\nDigite 3 para Listar compras',
          '\nDigite 4 para sair')
    n = int(input())

    if n == 1:
        while True:
            identificador = int(input("Digite o identificador do produto:"))
            nome = input('Digite o nome do produto: ')
            descricao = input('Digite a descrição do produto: ')
            valor = input('Digite o valor do produto: ')
            produtoNovo = Produto(identificador, nome, descricao, valor)
            break

    elif n == 2:
        clientData = 0
        total = 0
        while True:
            if clientData == 0:
                data = input('Digite a data de hoje: ')
                nome = input('Digite o Nome do Cliente: ')
                cpf = input('Digite o CPF do Cliente: ')
                rua = input('Digite a Rua onde o cliente mora: ')
                cep = input('Digite o CEP do cliente: ')
                cidade = input('Digite a Cidade onde o cliente mora: ')
                clienteNovo = Cliente(nome, cpf, rua, cep, cidade)
                identificador = int(input('Digite o identificador do produto(0 para parar): '))
                if identificador == 0:
                    break
                else:
                    produto = p.acharProduto(identificador)
                    if produto == 404:
                        print('Produto não existe')
                        break
                    else:
                        valor = p.acharProduto(identificador)
                        unidades = int(input('Digite quantas unidades do produto serão compradas: '))
                        total += valor * unidades
                        clientData += 1

            else:
                identificador = int(input('Digite o identificador do produto(0 para parar): '))
                if identificador == 0:
                    compraNova = Compra(data, nome, cpf, total)
                    break
                else:
                    produto = p.acharProduto(identificador)
                    if produto == 404:
                        print('Produto não existe')
                        break
                    else:
                        valor = p.acharProduto(identificador)
                        unidades = int(input('Digite quantas unidades do produto serão compradas: '))
                        total += valor * unidades


    elif n == 3:
        c.listarCompras()

    else:
        break