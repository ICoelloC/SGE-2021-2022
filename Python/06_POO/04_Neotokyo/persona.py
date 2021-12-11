class Persona:
    def __init__(self, id_persona, nombre):
        self.id_persona = id_persona
        self.nombre = nombre

    @property
    def id_persona(self):
        return self.__id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self.__id_persona = id_persona

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => ID: {1}, Nombre: {2}"
        return msg.format(clase, self.id_persona, self.nombre)
