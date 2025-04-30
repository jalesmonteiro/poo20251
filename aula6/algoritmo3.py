class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario:.2f}")

    def calcular_bonus(self):
        return self.salario * 0.05

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Departamento: {self.departamento}")

# Criando os objetos
func1 = Funcionario("João", 2000)
gerente1 = Gerente("Maria", 5000, "vendas")

# Mostrando informações e bônus
print()
func1.mostrar_informacoes()
print()
gerente1.mostrar_informacoes()
print()