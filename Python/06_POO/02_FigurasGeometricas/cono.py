from circunferencia import Circunferencia
import math


class Cono:
    def __init__(self, radio, generatriz):
        self.circunferencia = Circunferencia(radio)
        self.generatriz = generatriz

    @property
    def circunferencia(self):
        return self.__circunferencia

    @circunferencia.setter
    def circunferencia(self, circunferencia):
        self.__circunferencia = circunferencia

    @property
    def generatriz(self):
        return self.__generatriz

    @generatriz.setter
    def generatriz(self, generatriz):
        self.__generatriz = generatriz

    def area(self):
        return self.circunferencia.area() * math.pi * self.circunferencia.radio * self.generatriz

    def perimetro(self):
        return self.circunferencia.perimetro() + self.generatriz * 2

    def __str__(self):
        clase = type(self).__name__
        msg = '{0} de radio {1} y generatriz {2}'
        return msg.format(clase, self.circunferencia.radio, self.generatriz)
