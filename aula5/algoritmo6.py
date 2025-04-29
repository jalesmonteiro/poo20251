class Produto:
    def __init__(self, nome, **detalhes):
        self.nome = nome
        self.detalhes = detalhes

p = Produto("Notebook", cor="prata", preco=3500, garantia=2)
print(p.detalhes)
# Saída: {'cor': 'prata', 'preco': 3500, 'garantia': 2}