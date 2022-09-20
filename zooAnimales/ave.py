from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = None
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas

        # Agrego el animal creado
        if Ave._listado is None:
            Ave._listado = []
            Ave._listado.append(self)
        else:
            Ave._listado.append(self)
    
    def movimiento(self):
        return "volar"
    
    # Métodos set
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    # Métodos get
    def getColorPlumas(self):
        return self._colorPlumas

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    