class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Ao criar uma nova Pessoa, o construtor é chamado automaticamente
pessoa1 = Pessoa("Ana", 25)
print(pessoa1.nome)  # Saída: Ana
print(pessoa1.idade) # Saída: 25