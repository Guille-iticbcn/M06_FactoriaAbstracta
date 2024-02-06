from abc import ABC, abstractmethod

# Factoria Abstracta
class FabricaVideojuegos(ABC):
    @abstractmethod
    def crearVideojuego():
        pass