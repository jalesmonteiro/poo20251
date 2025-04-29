class Produto:
    def __init__(self, nome, **detalhes):
        self.nome = nome
        self.detalhes = detalhes

p = Produto("Notebook", cor="prata", preco=3500, garantia=2)
p2 = Produto("RAM", modelo="DDR5", preco=500, tamanho=16, garantia=1)
print(p.detalhes)
print(p2.detalhes)