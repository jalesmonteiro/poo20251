class Veiculo:
    def ligar(self):
        print("Veículo ligado.")

class Moto(Veiculo):
    def empinar(self):
        print("Moto empinando.")

class Onibus(Veiculo):
    def embarcar_passageiros(self):
        print("Passageiros embarcando.")

moto = Moto()
onibus = Onibus()
moto.ligar()
moto.empinar()
onibus.ligar()
onibus.embarcar_passageiros()
