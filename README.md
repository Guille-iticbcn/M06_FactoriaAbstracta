# M06_FactoriaAbstracta

Abstract Factory (FabricaVideojuegos): Define una interfaz para crear familias de productos relacionados (en este caso, videojuegos). Declara un método abstracto crearVideojuego() que devuelve un objeto de tipo Videojuego.

Concrete Factories (FabricaPC y FabricaConsola): Implementan los métodos de la fábrica abstracta para producir instancias concretas de los productos. Cada fábrica produce un tipo específico de videojuego (RPG ,Shooter o Plataforma) según el contexto (PC o Consola).

Concrete Products (JuegoRPG y JuegoShooter, JuegoPlataforma): Son las implementaciones concretas de los productos individuales. Cada uno proporciona una implementación específica del método obtenerNombre(), etc.

Abstract Product (Videojuego): Define la interfaz para los productos individuales (en este caso, los videojuegos). Videojuego es una clase abstracta que declara un método obtenerNombre() para obtener el nombre del tipo de videojuego. 

Cliente (Cliente): Utiliza la interfaz de la fábrica abstracta para interactuar con los productos sin conocer las implementaciones concretas. En este caso, el cliente solicita un videojuego a la fábrica y luego obtiene el nombre del juego a través del producto devuelto.












