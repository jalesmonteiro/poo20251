class Veiculo:
    """
    Classe base para veículos.
    
    Atributos:
        Nenhum.
    Métodos:
        mover(): Exibe uma mensagem indicando que o veículo está em movimento.
    """
    def mover(self):
        """Exibe uma mensagem indicando que o veículo está em movimento."""
        print("Veículo em movimento.")

class Caminhao(Veiculo):
    """
    Representa um caminhão, que é um tipo de veículo.

    Métodos:
        carregar(): Exibe uma mensagem indicando que o caminhão está carregando mercadorias.
    """
    def carregar(self):
        """Exibe uma mensagem indicando que o caminhão está carregando mercadorias."""
        print("Caminhão carregando mercadorias.")

class CaminhaoBau(Caminhao):
    """
    Representa um caminhão baú, que é um tipo específico de caminhão.

    Métodos:
        abrir_bau(): Exibe uma mensagem indicando que o baú foi aberto.
    """
    def abrir_bau(self):
        """Exibe uma mensagem indicando que o baú foi aberto."""
        print("Baú aberto.")

# Exemplo de uso:
truck = CaminhaoBau()
truck.mover()         # Saída: Veículo em movimento.
truck.carregar()      # Saída: Caminhão carregando mercadorias.
truck.abrir_bau()     # Saída: Baú aberto.
