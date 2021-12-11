from persona import Persona


class Ciberpolicia(Persona):
    def __init__(self, id_persona, nombre, n_placa, id_patrulla):
        super().__init__(id_persona, nombre)
        self.n_placa = n_placa
        self.id_patrulla = id_patrulla

    @property
    def n_placa(self):
        return self.__n_placa

    @n_placa.setter
    def n_placa(self, n_placa):
        self.__n_placa = n_placa

    @property
    def id_patrulla(self):
        return self.__id_patrulla

    @id_patrulla.setter
    def id_patrulla(self, id_patrulla):
        self.__id_patrulla = id_patrulla

    def __str__(self):
        clase = type(self).__name__
        msg = super().__str__() + " {0} => Número de placa: {1}, Patrulla: {2}"
        return msg.format(clase, self.n_placa, self.id_patrulla)
