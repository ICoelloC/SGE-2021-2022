from persona import Persona


class Delincuente(Persona):
    def __init__(self, id_persona, nombre, delitos):
        super().__init__(id_persona, nombre)
        self.delitos = delitos

    @property
    def delitos(self):
        return self.__delitos

    @delitos.setter
    def delitos(self, delitos):
        self.__delitos = delitos

    def add_delito(self, delito):
        self.delitos.append(delito)

    def get_dict(self):
        return {
            "id_persona": self.id_persona,
            "nombre": self.nombre,
            "delitos": self.delitos
        }
