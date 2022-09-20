from zooAnimales.animal import Animal

class Anfibio(Animal):

    _listado = None
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

        # Agrego el animal creado
        if Anfibio._listado is None:
            Anfibio._listado = []
            Anfibio._listado.append(self)
        else:
            Anfibio._listado.append(self)
    
    def movimiento(self):
        return "saltar"
    
    # Métodos set
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    # Métodos get
    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
    