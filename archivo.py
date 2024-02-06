from iJuegoPlataforma import *
from iJuegoRPG import *
from iJuegoShooter import *
from abc import ABC, abstractmethod

#Factoria Abstracta
class FabricaVideojuegos(ABC):
    @abstractmethod
    def crearVideojuego():
        pass
    
class Cliente:
    def __init__(self, FabricaVideojuegos):
        fabrica = FabricaVideojuegos
        self.fabrica = fabrica

    def obtenerNombreVideojuego(self):
        Videojuego = self.fabrica.crearVideojuego()
        return Videojuego.obtenerNombre()


