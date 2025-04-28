#Introdução à herança em POO
#(Programação Orientada a objetos em Python)
#  *Herança é um principio da Programação Orientada a Objetos que permite que uma classe herde atributos e métodos de outra classe.
#  -Promove reutilização de código.
#  -Facilita a manutenção e organização.
#  -Permite criar especializações a partir de uma classe genérica.
#
#Terminologia Importante
#  -Superclasse (Classe Base): Classe que fornece atributos e métodos para serem herdados.
#  -Subclasse (Classe Derivada): Classe que herda da superclasse e pode adicionar ou modificar comportamentos.
#  -`Super()`: Função usada para acessar métodos da superclasse.
#Exemplos Simples de Herança
class Animal:
    def __init__(self,nome):
        self.nome = nome
    def fazer_som(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def fazer_som(self):
        print(f"{self.nome} diz: Au Au!")
#Usando o super()
class Animal:
    def __init__(self,nome):
        self.nome = nome
class Cachorro(Animal):
    def __init__(self,nome,raca):
        super().__init__(nome)
        self.raca = raca