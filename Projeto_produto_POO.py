#Atividade: Criando uma classe 'Produto'
#  1.Crie uma classe Produto com os atributos:
#  __nome (privado)
#  __preço (Privado)
#  quantidade (público)
#
#  -2. implemente Getters e Setters para os atributos privados.
#  -3. valide no Setter que o preço não pode ser negativo.
#  -4. instancie um objeto produto e teste os métodos.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.quantidade = quantidade

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_preco(self):
        return self.__preco
    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Não é permitido valor negativo!")
produto1 = Produto("prego", 1.5, 200)
# print(Produto.get_nome())
# print("Tentando modificar o nome do produto")
# novoNomeProduto = input ("Digite o nome do produto: ")
# produto1.set_nome(NovoNomeProduto)
# print("Nome do produto: ")
# Print(produto1.get_nome())
novoPreco = float(input("Digite o novo preço do produto: "))
produto1.set_preco(novoPreco)

print(f"Preço do {produto1.get_nome()}: {produto1.get_preco()}")