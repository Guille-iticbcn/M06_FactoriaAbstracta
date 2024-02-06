#Abstract Factory
class VideojuegoFactory:
    def createRPG(self):
        pass

    def createPlataforma(self):
        pass
    
    def createShotter(self):
        pass

#Concrete Factory para PC
class PcFactory(VideojuegoFactory):
    def createRPG(self):
        return 

    def createPlataforma(self):
        return
    
    def createShotter(self):
        return
    
#Concrete Factory para Consola
class ConsolaFactory(VideojuegoFactory):
    def createRPG(self):
        return
    
    def createPlataforma(self):
        return
    
    def createShotter(self):
        return
    
#Abstract Products
class RPG:
    def obtenerNombre(self, nombre):
        pass

class Plataforma:
    def obtenerNombre(self, nombre):
        pass

class Shotter:
    def obtenerNombre(self, nombre):
        pass

#Concrete Products para PC
class PC_RPG:
    def obtenerNombre(self, nombre):
        return nombre
    
class PC_Plataforma:
    def obtenerNombre(self, nombre):
        return nombre
    
class PC_Shotter:
    def obtenerNombre(self, nombre):
        return nombre

#Concrete Products para Consola
class Consola_RPG:
    def obtenerNombre(self, nombre):
        return nombre
    
class Consola_Plataforma:
    def obtenerNombre(self, nombre):
        return nombre
    
class Consola_Shotter:
    def obtenerNombre(self, nombre):
        return nombre
