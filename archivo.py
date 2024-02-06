from abc import ABC, abstractmethod

#Producto abstracto
class Videojuego(ABC):
    @abstractmethod
    def obtenerNombre(self):
        pass

#Producto concreto
class JuegoRPG(Videojuego):
    def obtenerNombre(self):
        return "RPG"
    
#Produco concreto    
class JuegoShooter(Videojuego):
    def obtenerNombre(self):
        return "Shooter"
    
#Producto concreto    
class JuegoPlataforma(Videojuego):
    def obtenerNombre(self):
        return "Plataforma"
    
#Factoria Abstracta
class FabricaVideojuegos(ABC):
    @abstractmethod
    def crearVideojuego():
        pass

#Factorias Concretas
class FabricaPC(FabricaVideojuegos):
    def crearVideojuego():
        return JuegoRPG
    
    def crearVideojuego():
        return JuegoPlataforma
    
    def crearVideojuego():
        return JuegoShooter
    
class FabricaConsola(FabricaVideojuegos):
    def crearVideojuego():
        return JuegoRPG
    
    def crearVideojuego():
        return JuegoPlataforma
    
    def crearVideojuego():
        return JuegoShooter
    
class Cliente:
    def __init__(self, FabricaVideojuegos):
        fabrica = FabricaVideojuegos
        self.fabrica = fabrica

    def obtenerNombreVideojuego(self):
        Videojuego = self.fabrica.crearVideojuego()
        return Videojuego.obtenerNombre()


