class Grupo:
    def __init__(self, homens, *nomes):
        self.homens = homens
        self.membros = list(nomes)

# Criando grupos com diferentes quantidades de membros
grupo1 = Grupo(2, "Ana", "Bruno", "Carlos")
grupo2 = Grupo(1, "Maria", "João")

print(grupo1.homens)  # Saída: 2
print(grupo2.homens)  # Saída: 1
print(grupo1.membros)  # Saída: ['Ana', 'Bruno', 'Carlos']
print(grupo2.membros)  # Saída: ['Maria', 'João']