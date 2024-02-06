from archivo import FabricaVideojuegos
from iJuegoPlataforma import JuegoPlataforma
from iJuegoRPG import JuegoRPG
from iJuegoShooter import JuegoShooter

#Factorias Concretas
class FabricaPC(FabricaVideojuegos):
    def crearVideojuego():
        return JuegoRPG
    
    def crearVideojuego():
        return JuegoPlataforma
    
    def crearVideojuego():
        return JuegoShooter