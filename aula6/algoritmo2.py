class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario:.2f}")

    def calcular_bonus(self):
        return self.salario * 0.05

class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15

# Criando os objetos
func1 = Funcionario("João", 2000)
dev1 = Desenvolvedor("Carlos", 4000)
gerente1 = Gerente("Maria", 5000)

# Mostrando informações e bônus
print()
for funcionario in [func1, dev1, gerente1]:
    funcionario.mostrar_informacoes()
    print(f"Bônus: R${funcionario.calcular_bonus():.2f}")
    print("-" * 30)