class Eletrico:
    def carregar_bateria(self):
        print("Bateria carregando...")

class Veiculo:
    def ligar(self):
        print("Veículo ligado.")

class CarroEletrico(Veiculo, Eletrico):
    pass

tesla = CarroEletrico()
tesla.ligar()
tesla.carregar_bateria()
