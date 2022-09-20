from zooAnimales.animal import Animal

class Pez(Animal):

    _listado = None
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

        # Agrego el animal creado
        if Pez._listado is None:
            Pez._listado = []
            Pez._listado.append(self)
        else:
            Pez._listado.append(self)
    
    def movimiento(self):
        return "nadar"
    
    # Métodos set
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    # Métodos get
    def getColorEscamas(self):
        return self._colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)
    