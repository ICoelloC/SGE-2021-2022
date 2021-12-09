class Persona:
    def __init__(self, id, nombre):
        self.nombre = nombre
        self.id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def __str__(self):
        clase = type(self).__name__
        msg = '{0} -> ID: {1}, Nombre: {2}'
        return msg.format(clase, self.id, self.nombre)
