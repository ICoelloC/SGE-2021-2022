from policia import Policia
from jefe_patrulla import JefePatrulla


class Patrulla:
    def __init__(self, id_patrulla, jefe, policias):
        self.id_patrulla = id_patrulla
        self.jefe = jefe
        self.policias = policias

    @property
    def id_patrulla(self):
        return self.__id_patrulla

    @id_patrulla.setter
    def id_patrulla(self, id_patrulla):
        self.__id_patrulla = id_patrulla

    @property
    def jefe(self):
        return self.__jefe

    @jefe.setter
    def jefe(self, jefe):
        self.__jefe = jefe

    @property
    def policias(self):
        return self.__policias

    @policias.setter
    def policias(self, policias):
        self.__policias = policias

    def add_policia(self, policia):
        self.policias.append(policia)

    def ver_registro(self):
        return self.jefe.ver_registro()
