import time
import threading as th

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.age = 1
        self.breed = breed
        self.happiness = 70 
        self.energy = 100  
        self.awake = True
        self.hunger = 10  
        self.food = 5  
        self.money = 50  
        self.time_alive = 1  
        self.running = True  
        if self.energy == 0:
            self.awake=False
            print(f"{self.name} foi dormir.")

    def feed(self):
        if not self.awake:
            print(f"{self.name} está dormindo. Acorde-o primeiro.")
        elif self.food > 0:
            self.food -= 1
            self.hunger = max(0, self.hunger - 50)
            print(f"{self.name} comeu! Fome reduzida. Comida restante: {self.food}")
        else:
            print("Você não tem comida suficiente. Compre mais.")

    def play(self):
        if not self.awake:
            print(f"{self.name} está dormindo. Acorde-o primeiro.")
        elif self.energy < 10:
            print(f"{self.name} está muito cansado para brincar. Faça-o descansar.")
        else:
            self.happiness = min(100, self.happiness + 20) 
            self.energy -= 20
            self.hunger +=10
            print(f"Você brincou com {self.name}. Ele está mais feliz, mas gastou energia.")

    def work(self):
        self.money += 20
        self.time_alive += 100 
        if self.hunger < 100:   
            self.hunger += 15
        elif self.hunger >= 100:
            self.hunger = 100
        if self.happiness > 0:
            self.happiness -= 15
        elif self.happiness <= 0:
            self.happiness = 0
        
        print(f"Você trabalhou e ganhou $20. Dinheiro total: ${self.money}")

    def buy_food(self):
        if self.money >= 10:
            self.money -= 10
            self.food += 3
            print(f"Você comprou comida. Comida total: {self.food}. Dinheiro restante: ${self.money}")
        else:
            print("Você não tem dinheiro suficiente para comprar comida.")

    def hit(self):
        self.happiness = max(0, self.happiness - 50)
        if not self.awake:
            self.awake = True
        print(f"Você bateu no {self.name}! Ele parece muito triste...")

    def ignore(self):
        if not self.awake:
            print(f"Você ignora {self.name} e o deixa dormindo tranquilamente.")
        else:
            self.happiness = max(0, self.happiness - 20) 
            print(f"Você ignorou {self.name}. Ele parece um pouco mais triste...")

    def wake_up(self):
        if self.energy < 40:
            print(f"{self.name} está cansado demais para acordar.")
        elif self.awake:
            print(f"{self.name} já está acordado.")
        else: 
            if not self.awake:
                self.awake = True
                print(f"{self.name} acordou e está pronto para brincar.")
            else:
                print(f"{self.name} já está acordado.")

    def sleep(self):
        if self.awake:
            self.awake = False
            self.energy = 100
            self.happiness = min(100, self.happiness + 10)
            print(f"{self.name} foi dormir. Energia restaurada!")
        else:
            print(f"{self.name} já está dormindo.")

    def show_status(self):
        print("\n--- Status do Cachorro ---")
        print(f"Nome: {self.name}")
        print(f"Raça: {self.breed}")
        print(f"Idade: {self.age} anos")
        print(f"Fome: {self.hunger}/100")
        print(f"Felicidade: {self.happiness}/100")
        print(f"Energia: {self.energy}/100")
        print(f"Comida disponível: {self.food}")
        print(f"Dinheiro: ${self.money}")
        print(f"Está acordado? {'Sim' if self.awake else 'Não'}")
        print(f"Tempo até o próximo aniversário: {1000 - (self.time_alive % 1000)} segundos.")
        print("-------------------------\n")

    def update_status(self):
        while self.running:
            time.sleep(1) 
            self.time_alive += 1
            if self.hunger < 100:
                self.hunger += 2  
            if self.happiness > 0:
                self.happiness -= 2 
          
            if self.time_alive >= 1000:
                self.time_alive = 0
                self.age += 1
                print(f"\n{self.name} fez aniversário! Agora tem {self.age} anos!\n") 
    


    def stop(self):
        self.running = False

    

dog_name = input("Escolha um nome para seu cachorro: ").strip().capitalize()
while not dog_name:
    dog_name = input("O nome não pode estar vazio! Escolha um nome para seu cachorro: ").strip().capitalize()

dog_breed = input("Escolha a raça do seu cachorro: ").strip().capitalize()
while not dog_breed:
    dog_breed = input("A raça não pode estar vazia! Escolha uma raça para seu cachorro: ").strip().capitalize()

my_dog = Dog(name=dog_name, breed=dog_breed)

update_thread = th.Thread(target=my_dog.update_status, daemon=True)
update_thread.start()

while True:
    print("\nOpções:")
    print("1 - Ver status do cachorro")
    print("2 - Alimentar")
    print("3 - Brincar")
    print("4 - Trabalhar")
    print("5 - Comprar comida")
    print("6 - Bater")
    print("7 - Ignorar")
    print("8 - Acordar")
    print("9 - Colocar para dormir")
    print("10 - Sair")

    choice = input("Escolha uma opção: ").strip()

    if choice == "1":
        my_dog.show_status()
    elif choice == "2":
        my_dog.feed()
    elif choice == "3":
        my_dog.play()
    elif choice == "4":
        my_dog.work()
    elif choice == "5":
        my_dog.buy_food()
    elif choice == "6":
        my_dog.hit()
    elif choice == "7":
        my_dog.ignore()
    elif choice == "8":
        my_dog.wake_up()
    elif choice == "9":
        my_dog.sleep()
    elif choice == "10":
        my_dog.stop()
        print("Saindo... Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente.")
