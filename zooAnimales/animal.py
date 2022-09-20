class Animal:

    _total_animales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._total_animales += 1
    
    def movimiento(self):
        return "desplazarse"
    
    def toString(self):
        text = "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero
        if self._zona is None:
            return text
        else:
            return text + ", la zona en la que me ubico es " + self._zona + ", en el " + self._zona.getZoo()
        
    # Métodos set
    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    def setHabitat(self, habitat):
        self._habitat = habitat

    def setGenero(self, genero):
        self._genero = genero

    # Métodos get
    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    @classmethod
    def getTotalAnimales(cls):
        return cls._total_animales

    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos : 3\nAves : 2\nReptiles : 1\nPeces : 1\nAnfibios : 2"
    
