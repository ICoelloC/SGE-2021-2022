class Poligono():
    def __init__(self, *args):
        self.lados = args
        self.n_lados = len(self.lados)

    @property
    def lados(self):
        return self.__lados

    @lados.setter
    def lados(self, lados):
        self.__lados = lados

    @property
    def n_lados(self):
        return self.__n_lados

    def __str__(self):
        clase = type(self).__name__
        msg = '{0} de {1} lados con longitudes {2}'
        return msg.format(clase, self.n_lados, self.lados)

    def perimetro(self):
        return sum(self.lados)
