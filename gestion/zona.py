class Zona:

    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = None
    
    def agregarAnimales(self, animal):
        if self._animales is None:
            self._animales = []
            self._animales.append(animal)
        else:
            self._animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._animales)
    
    # Métodos set
    def setNombre(self, nombre):
        self._nombre = nombre

    def setZoo(self, zoo):
        self._zoo = zoo
    
    # Métodos get
    def getNombre(self):
        return self._nombre
    
    def getZoo(self):
        return self._zoo
    
    def getAnimales(self):
        return self._animales