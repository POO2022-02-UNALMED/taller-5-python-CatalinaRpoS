class Zoologico:

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = None
    
    def agregarZonas(self, zona):
        if self._zonas is None:
            self._zonas = []
            self._zonas.append(zona)
        else:
            self._zonas.append(zona)
    
    def cantidadTotalAnimales(self):
        total = 0
        for zona in self._zonas:
            total += len(zona.getAnimales())
        return total
    
    # Métodos set
    def setNombre(self, nombre):
        self._nombre = nombre

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    
    # Métodos get
    def getNombre(self):
        return self._nombre

    def getUbicacion(self):
        return self._ubicacion
    
    def getZona(self):
        return self._zonas