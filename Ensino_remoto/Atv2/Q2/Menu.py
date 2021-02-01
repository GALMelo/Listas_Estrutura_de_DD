from Q2.Autor import Autor
from Q2.Livro import Livro
from Q2.Exemplares import Exemplar

autor_data = []
livros_data = []
exemplares = []

a = Livro
#Start Autor
def listar_autores():
    for x in autor_data:
        print(x.nome)

def achar_autor(cpf):
    for x in autor_data:
        if x.cpf == cpf:
            print(x.nome, x.endereco, x.cpf, x.num_obras, x.descricao)

def deletar_autor(cpf):
    y = 0
    for x in autor_data:
        if x.cpf == cpf:
            del autor_data[y]
            break
        else:
            y += 1
#End Autor

#Start Livros
def listar_livros():
    for x in livros_data:
        a = qty_exemplares(x, exemplares)
        print('ISBN {}, Titulo {}, Ano de Lançamento {}, Autor(es) {}'.format(x.isbn, x.titulo, x.ano, x.lista_autores))
        print(a)

def qty_exemplares(Livro, exemplares):
    quantidade = 0
    custo = 0
    for e in exemplares:
        if e.livro == Livro:
            quantidade += 1
            custo += e.custo
            return 'Temos {} em estoque e o valor total é R${:.2f}'.format(quantidade, custo)


def achar_livro(isbn):
    for x in livros_data:
        if x.isbn == isbn:
            return x.isbn, x.titulo, x.ano, x.lista_autores

def achar_livro_para_qty(isbn):
    for x in livros_data:
        if x.isbn == isbn:
            return x

def deletar_livro(isbn):
    y = 0
    for x in livros_data:
        if x.isbn == isbn:
            del livros_data[y]
            break
        else:
            y += 1
#End livros



while True:
    print('\nMenu'
          '\nDigite 1 para cadastrar autor'
          '\nDigite 2 para listar autores'
          '\nDigite 3 para encontrar dados de um autor'
          '\nDigite 4 para deletar um autor'
          '\nDigite 5 para cadastrar um livro'
          '\nDigite 6 para listar livros'
          '\nDigite 7 para encontrar um livro no acervo' 
          '\nDigite 8 para cadastrar um exemplar')

    escolha = int(input())

    if escolha == 1:
        nome = input('Digite o nome do autor: ')
        endereco = input('Digite o endereco do autor: ')
        cpf = input('Digite o cpf do autor: ')
        num_obras = input('Digite o numero de obras do autor: ')
        descricao = input('Adicione uma descrição do autor: ')
        autor_novo = Autor(nome, endereco, cpf, num_obras, descricao)
        autor_data.append(autor_novo)

    elif escolha == 2:
        listar_autores()

    elif escolha == 3:
        cpf = input('Digite o cpf do autor que deseja encontrar: ')
        achar_autor(cpf)

    elif escolha == 4:
        cpf = input('Digite o cpf do autor que deseja deletar: ')
        deletar_autor(cpf)

    elif escolha == 5:
        isbn = input('Digite o ISBN do livro: ')
        titulo = input('Digite o titulo do livro: ')
        ano = input('Digite o ano que o livro foi criado: ')
        lista_autores = input('Digite o nome dos autor(es): ').split()
        livro_novo = Livro(isbn, titulo, ano, lista_autores)
        livros_data.append(livro_novo)
        livro_novo.print()

    elif escolha == 6:
        listar_livros()

    elif escolha == 7:
        isbn = input('Digite o isbn do livro que deseja encontrar: ')
        livro = achar_livro(isbn)
        print(livro)

    elif escolha == 8:
        isbn = input('Digite o isbn do livro precadastrado: ')
        livro = achar_livro_para_qty(isbn)
        data_aquisicao = input('Digite a data da compra: ')
        custo = int(input('Digite o custo da compra: '))
        exemplar_novo = Exemplar(livro, data_aquisicao, custo)
        exemplares.append(exemplar_novo)

    else:
        break

