class Carro:
    def __init__(self, marca, modelo, ano, cor, combustivel=100, ligado=False, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = combustivel
        self.ligado = ligado
        self.velocidade = velocidade

    def ligar(self):
        if self.combustivel > 0 and self.ligado:
            self.combustivel -= min(self.combustivel, 2)
            return f'O {self.modelo} já está ligado!\nFuel: {self.combustivel}'
        if self.combustivel > 0:
            self.ligado = True
            self.combustivel -= min(self.combustivel, 2)
            return f'O {self.modelo} foi ligado!\nFuel: {self.combustivel}'
        return f'O {self.modelo} está desligado por falta de combustível!\nFuel: {self.combustivel}'

    def acelerar(self):
        if self.combustivel > 0 and self.ligado:
            if self.combustivel >= 5:  
                self.velocidade += 10
                self.combustivel -= 5
                return f'O {self.modelo} está acelerando!\nVelocidade: {self.velocidade} km/h\nFuel: {self.combustivel}'
            else:
                return f'Combustível insuficiente para acelerar! Fuel: {self.combustivel}'
        return f'O {self.modelo} não pode acelerar. Verifique se está ligado e com combustível.'

    def freiar(self):
        if self.velocidade > 0 and self.ligado:
            self.velocidade = 0
            return f'O {self.modelo} está freando!\nVelocidade: {self.velocidade} km/h\nFuel: {self.combustivel}'
        return f'O {self.modelo} não está em movimento para frear.'

meu_carro = Carro(marca="Chevrolet", modelo="Celta", ano=2012, cor="branco")

while True:
    print("\nO que deseja fazer com o seu carro?")
    print("1 - Ligar")
    print("2 - Acelerar")
    print("3 - Freiar")
    print("4 - Sair")

    escolha = input("Digite a sua escolha: ")
    if not escolha.isdigit():
        print("Por favor, insira um número válido.")
        continue

    escolha = int(escolha)

    if escolha == 1:
        print(meu_carro.ligar())
    elif escolha == 2:
        print(meu_carro.acelerar())
    elif escolha == 3:
        print(meu_carro.freiar())
    elif escolha == 4:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Escolha entre 1 e 4.")
