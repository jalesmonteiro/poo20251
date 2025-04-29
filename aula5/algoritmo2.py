class Retangulo:
  def __init__(self, largura, altura):
    self.largura = largura
    self.altura = altura
    self.area = largura * altura

r = Retangulo(5, 3)
print(r.area)  # Saída: 15