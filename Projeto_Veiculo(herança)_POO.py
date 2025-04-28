#Atividade de 'veiculo' (herança)
#  -Crie uma classe 'Veiculo' com os atributos 'modelo' e 'ano'.
#  -Crie duas subclasse: `carro` e `Moto`, que herdem de `Veiculo`.
#  -Adicione métodos específicos para cada tipo de veículo.
#  -Use o `super()` no construtor das subclasses.

# Classe base
class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        print(f"Modelo: {self.modelo}, Ano: {self.ano}")

# Subclasse Carro
class Carro(Veiculo):
    def __init__(self, modelo, ano, portas):
        super().__init__(modelo, ano)
        self.portas = portas

    def ligar_ar_condicionado(self):
        print(f"{self.modelo} ligou o ar-condicionado.")

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Portas: {self.portas}")

# Subclasse Moto
class Moto(Veiculo):
    def __init__(self, modelo, ano, cilindradas):
        super().__init__(modelo, ano)
        self.cilindradas = cilindradas

    def empinar(self):
        print(f"{self.modelo} está empinando!")

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Cilindradas: {self.cilindradas}")

# Testes
carro1 = Carro("Fusca", 1980, 2)
carro1.exibir_dados()
carro1.ligar_ar_condicionado()

print()

moto1 = Moto("Honda CG", 2022, 150)
moto1.exibir_dados()
moto1.empinar()