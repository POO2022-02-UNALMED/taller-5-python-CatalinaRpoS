from zooAnimales.animal import Animal

class Mamifero(Animal):

    _listado = None
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas

        # Agrego el animal creado
        if Mamifero._listado is None:
            Mamifero._listado = []
            Mamifero._listado.append(self)
        else:
            Mamifero._listado.append(self)
    
    # Métodos set
    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def setPatas(self, patas):
        self._patas = patas

    # Métodos get
    def isPelaje(self):
        return self._pelaje

    def getPatas(self):
        return self._patas

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)
    