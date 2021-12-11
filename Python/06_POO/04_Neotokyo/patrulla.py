class Patrulla:
    def __init__(self, n_patrulla, c_patrulla, c_policias):
        if len(c_policias) < 4:
            raise ValueError("El número de policías debe >= 4")
        self.coordinador_patrulla = c_patrulla
        self.ciberpolicias = c_policias
        self.id_patrulla = n_patrulla

    @property
    def coordinador_patrulla(self):
        return self.__coordinador_patrulla

    @coordinador_patrulla.setter
    def coordinador_patrulla(self, c_patrulla):
        self.__coordinador_patrulla = c_patrulla

    @property
    def ciberpolicias(self):
        return self.__ciberpolicias

    @ciberpolicias.setter
    def ciberpolicias(self, c_policias):
        self.__ciberpolicias = c_policias

    @property
    def id_patrulla(self):
        return self.__id_patrulla

    @id_patrulla.setter
    def id_patrulla(self, n_patrulla):
        self.__id_patrulla = n_patrulla

    def get_registro(self):
        return self.coordinador_patrulla.get_registro()
