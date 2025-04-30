from funcionario import Funcionario
from desenvolvedor import Desenvolvedor
from gerente import Gerente
# Outras possíbilidades:
# from desenvolvedor import Funcionario
# from gerente import Funcionario

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