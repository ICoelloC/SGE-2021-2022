from policia import Policia
from jefe_patrulla import JefePatrulla


class Patrulla:
    def __init__(self, id_patrulla, jefe, policias):
        if len(policias) <= 4:
            raise ValueError("La patrulla debe tener al menos 5 policias")
        self.id_patrulla = id_patrulla
        self.jefe = jefe
        self.policias = policias

    @property
    def id_patrulla(self):
        return self._id_patrulla

    @id_patrulla.setter
    def id_patrulla(self, id_patrulla):
        self._id_patrulla = id_patrulla

    @property
    def jefe(self):
        return self._jefe

    @jefe.setter
    def jefe(self, jefe):
        self._jefe = jefe

    @property
    def policias(self):
        return self._policias

    @policias.setter
    def policias(self, policias):
        self._policias = policias

    def add_policia(self, policia):
        self.policias.append(policia)

    def ver_registro(self):
        return self.jefe.ver_registro()
