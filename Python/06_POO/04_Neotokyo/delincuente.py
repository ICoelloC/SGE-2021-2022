from persona import Persona


class Delincuente(Persona):
    def __init__(self, id, nombre, delitos):
        super().__init__(id, nombre)
        self.delitos = delitos

    @property
    def delitos(self):
        return self.__delitos

    @delitos.setter
    def delitos(self, delitos):
        self.__delitos = delitos

    def add_delito(self, delito):
        self.__delitos.append(delito)

    def get_datos(self):
        return {'id': self.id, 'nombre': self.nombre, 'delitos': self.delitos}
