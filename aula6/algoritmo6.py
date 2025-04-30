class Veiculo:
    def mover(self):
        print("Veículo em movimento.")

class Caminhao(Veiculo):
    def carregar(self):
        print("Caminhão carregando mercadorias.")

class CaminhaoBaú(Caminhao):
    def abrir_bau(self):
        print("Baú aberto.")

truck = CaminhaoBaú()
truck.mover()
truck.carregar()
truck.abrir_bau()
