from punto import Punto


class Triangulo:
    def __init__(self, punto1_x = -1, punto1_y = 4, punto2_x = 2, punto2_y = 0, punto3_x = 6, punto3_y = -3):
        self.punto1 = Punto(punto1_x, punto1_y)
        self.punto2 = Punto(punto2_x, punto2_y)
        self.punto3 = Punto(punto3_x, punto3_y)

    @property
    def punto1_x(self):
        return self.punto1.x

    @punto1_x.setter
    def punto1_x(self, valor):
        self.punto1.x = valor

    @property
    def punto1_y(self):
        return self.punto1.y

    @punto1_y.setter
    def punto1_y(self, valor):
        self.punto1.y = valor

    @property
    def punto2_x(self):
        return self.punto2.x

    @punto2_x.setter
    def punto2_x(self, valor):
        self.punto2.x = valor

    @property
    def punto2_y(self):
        return self.punto2.y

    @punto2_y.setter
    def punto2_y(self, valor):
        self.punto2.y = valor

    @property
    def punto3_x(self):
        return self.punto3.x

    @punto3_x.setter
    def punto3_x(self, valor):
        self.punto3.x = valor

    @property
    def punto3_y(self):
        return self.punto3.y

    @punto3_y.setter
    def punto3_y(self, valor):
        self.punto3.y = valor

    def calcular_perimetro(self):
        return self.punto1.distancia(self.punto2) + self.punto2.distancia(self.punto3) + self.punto3.distancia(self.punto1)

    def calcular_area(self):
        s = self.calcular_perimetro() / 2
        return (s * (s - self.punto1.distancia(self.punto2)) * (s - self.punto2.distancia(self.punto3)) * (s - self.punto3.distancia(self.punto1))) ** 0.5

    def __str__(self):
        clase = type(self).__name__
        msg = '{0}\n' \
              '\tPunto 1: \n\t\tX: {1}, Y: {2}\n' \
              '\tPunto 2: \n\t\tX: {3}, Y: {4}\n' \
              '\tPunto 3: \n\t\tX: {5}, Y: {6}\n' \
              '\tPerímetro: {7}\n' \
              '\tÁrea: {8}\n'
        return msg.format(clase, self.punto1.x, self.punto1.y, self.punto2.x, self.punto2.y, self.punto3.x,
                          self.punto3.y, self.calcular_perimetro(), self.calcular_area())
