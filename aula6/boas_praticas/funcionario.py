class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario:.2f}")

    def calcular_bonus(self):
        return self.salario * 0.05