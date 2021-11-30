import math


class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        self.__x = valor

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, valor):
        self.__y = valor

    def distancia(self, punto):
        return math.sqrt((self.x - punto.x) ** 2 + (self.y - punto.y) ** 2)
