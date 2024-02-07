from abc import ABC, abstractmethod

# Abstract Factory para crear juegos
class VideojuegoFactory(ABC):
    @abstractmethod
    def crearJuegoPlataforma(self):
        pass
    
    @abstractmethod
    def crearJuegoRPG(self):
        pass
    
    @abstractmethod
    def crearJuegoShooter(self):
        pass

# Concrete Factory para PC
class PcFactory(VideojuegoFactory):
    def crearJuegoPlataforma(self):
        return PC_Plataforma()
    
    def crearJuegoRPG(self):
        return PC_RPG()
    
    def crearJuegoShooter(self):
        return PC_Shotter()

# Concrete Factory para Consola
class ConsolaFactory(VideojuegoFactory):
    def crearJuegoPlataforma(self):
        return Consola_Plataforma()
    
    def crearJuegoRPG(self):
        return Consola_RPG()
    
    def crearJuegoShooter(self):
        return Consola_Shotter()

# Abstract Products
class JuegoPlataforma(ABC):
    @abstractmethod
    def obtenerNombre(self):
        pass
    
    @abstractmethod
    def obtenerAnio(self):
        pass
    
    @abstractmethod
    def obtenerEmpresa(self):
        pass

class JuegoRPG(ABC):
    @abstractmethod
    def obtenerNombre(self):
        pass
    
    @abstractmethod
    def obtenerAnio(self):
        pass
    
    @abstractmethod
    def obtenerEmpresa(self):
        pass

class JuegoShooter(ABC):
    @abstractmethod
    def obtenerNombre(self):
        pass
    
    @abstractmethod
    def obtenerAnio(self):
        pass
    
    @abstractmethod
    def obtenerEmpresa(self):
        pass

# Concrete Products para PC
class PC_Plataforma(JuegoPlataforma):
    def obtenerNombre(self):
        return "Super Mario Bros."
    
    def obtenerAnio(self):
        return 1985
    
    def obtenerEmpresa(self):
        return "Nintendo"
    
class PC_RPG(JuegoRPG):
    def obtenerNombre(self):
        return "Elden Ring"
    
    def obtenerAnio(self):
        return 2022
    
    def obtenerEmpresa(self):
        return "FromSoftware"
    
class PC_Shotter(JuegoShooter):
    def obtenerNombre(self):
        return "Call of Duty: Black Ops 2"
    
    def obtenerAnio(self):
        return 2012
    
    def obtenerEmpresa(self):
        return "Treyarch"

# Concrete Products para Consola
class Consola_Plataforma(JuegoPlataforma):
    def obtenerNombre(self):
        return "Super Mario Bros."
    
    def obtenerAnio(self):
        return 1985
    
    def obtenerEmpresa(self):
        return "Nintendo"
    
class Consola_RPG(JuegoRPG):
    def obtenerNombre(self):
        return "Elden Ring"
    
    def obtenerAnio(self):
        return 2022
    
    def obtenerEmpresa(self):
        return "FromSoftware"
    
class Consola_Shotter(JuegoShooter):
    def obtenerNombre(self):
        return "Call of Duty: Black Ops 2"
    
    def obtenerAnio(self):
        return 2012
    
    def obtenerEmpresa(self):
        return "Treyarch"

# Cliente que utiliza la fábrica para obtener juegos
class Cliente:
    def __init__(self, fabrica):
        self.fabrica = fabrica

    def obtenerDatosJuegos(self):
        juego_plataforma = self.fabrica.crearJuegoPlataforma()
        juego_rpg = self.fabrica.crearJuegoRPG()
        juego_shooter = self.fabrica.crearJuegoShooter()
        return (juego_plataforma.obtenerNombre(), juego_plataforma.obtenerAnio(), juego_plataforma.obtenerEmpresa()), \
               (juego_rpg.obtenerNombre(), juego_rpg.obtenerAnio(), juego_rpg.obtenerEmpresa()), \
               (juego_shooter.obtenerNombre(), juego_shooter.obtenerAnio(), juego_shooter.obtenerEmpresa())

# Crear instancias de cliente y fábricas con diferentes tipos de juegos
cliente_pc = Cliente(PcFactory())
cliente_consola = Cliente(ConsolaFactory())

# Obtener datos de juegos de diferentes tipos
plataforma_pc, rpg_pc, shooter_pc = cliente_pc.obtenerDatosJuegos()
plataforma_consola, rpg_consola, shooter_consola = cliente_consola.obtenerDatosJuegos()

# Mostrar los datos de los juegos
print("Juegos para PC:")
print("Plataforma:", plataforma_pc)
print("RPG:", rpg_pc)
print("Shooter:", shooter_pc)

print("\nJuegos para Consola:")
print("Plataforma:", plataforma_consola)
print("RPG:", rpg_consola)
print("Shooter:", shooter_consola)
