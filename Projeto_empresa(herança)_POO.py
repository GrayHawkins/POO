#Objetivo da atividade
#  -Aplicar herança para evitar repetição de código. 
#  -Utilizar encapsulamento para proteger dados dos objetos. 
#  -Praticar o uso de getters e setters. 
#  -Desenvolver um sistema orientado a objetos em Python. 

#Contexto

#  💼 A empresa “TechSolutions” está criando um sistema de cadastro de funcionários.
#  📋 Funcionários podem ser:
#    Administrativos
#    Operacionais
#    Gerentes
#  🎯 Cada tipo de funcionário possui características em comum e algumas específicas.

#Desafio

#  Crie as seguintes classes em Python:
#  Funcionario (classe base)
#  Gerente (herda de Funcionario)
#  Operacional (herda de Funcionario)
#  Aplique encapsulamento nos atributos.
#  Use getters e setters para acessar os dados.

#Requisitos de classe funcionario

#  Atributos privados: nome, cpf, salario
#  Métodos:
#  Construtor para inicializar os atributos
#  Getters e Setters para cada atributo
#  Método exibir_dados() que imprime os dados

#requisitos das subclasses

#  🧑‍💼 Gerente
#    Atributo adicional: bonus (privado)
#    Sobrescreve o método exibir_dados() mostra salário final (salário + bônus)

#  👷 Operacional
#    Atributo adicional: turno (privado)
#    exibir_dados() mostra o turno também
#    Funcionários(Superclasse)
#    Atributos privados: nome, cpf, salario
#    Métodos:
#      Construtor para inicializar os atributos
#      Getters e Setters para cada atributo
#      Método exibir_dados() que imprime os dados

#  🧑‍💼 Gerente(Funcionários)
#    Atributo adicional: 
#    bonus (privado)
#    Método:
#      método exibir_dados() mostra salário final (salário + bônus)

#  👷 Operacional(Funcionários
#    Atributo adicional: 
#    turno (privado)
#    Método:
#      exibir_dados() mostra o turno também

#Exemplo de saida
#  Nome: Bruno Castro
#  CPF: 111.222.333-44
#  Salário Base: R$ 5000.00
#  Bônus: R$ 1200.00
#  Salário Total: R$ 6200.00
#  ------------------------------


# Classe base
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    # Getters
    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_salario(self):
        return self.__salario

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_salario(self, salario):
        self.__salario = salario

    # Método comum
    def exibir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"CPF: {self.__cpf}")
        print(f"Salário Base: R$ {self.__salario:.2f}")


# Subclasse Gerente
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, bonus):
        super().__init__(nome, cpf, salario)
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def exibir_dados(self):
        salario_total = self.get_salario() + self.__bonus
        print(f"Nome: {self.get_nome()}")
        print(f"CPF: {self.get_cpf()}")
        print(f"Salário Base: R$ {self.get_salario():.2f}")
        print(f"Bônus: R$ {self.__bonus:.2f}")
        print(f"Salário Total: R$ {salario_total:.2f}")
        print("-" * 30)


# Subclasse Operacional
class Operacional(Funcionario):
    def __init__(self, nome, cpf, salario, turno):
        super().__init__(nome, cpf, salario)
        self.__turno = turno

    def get_turno(self):
        return self.__turno

    def set_turno(self, turno):
        self.__turno = turno

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Turno: {self.__turno}")
        print("-" * 30)


# Teste do sistema
gerente1 = Gerente("Bruno Castro", "111.222.333-44", 5000.00, 1200.00)
operacional1 = Operacional("Ana Lima", "555.666.777-88", 2500.00, "Noturno")

gerente1.exibir_dados()
operacional1.exibir_dados()
