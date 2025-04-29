class Produto:
    def __init__(self, nome, preco=1.0):
        self.nome = nome
        self.preco = preco

p1 = Produto("Caneta")
p2 = Produto("Lápis", 1.5)
print(p1.preco)  # Saída: 1.0
print(p2.preco)  # Saída: 1.5