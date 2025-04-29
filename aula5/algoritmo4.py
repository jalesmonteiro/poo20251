class Grupo:
    def __init__(self, *nomes):
        self.membros = list(nomes)

# Criando grupos com diferentes quantidades de membros
grupo1 = Grupo("Ana", "Bruno", "Carlos")
grupo2 = Grupo("Maria", "João")
grupo3 = Grupo("Lívia")