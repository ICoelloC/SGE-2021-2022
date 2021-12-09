from dinosaurio import Dinosaurio
from constantes import HERBIVORO, POSIB_PRESA_MANADA, ENERGIA_TRICE


class Triceraptops(Dinosaurio):
    POSIB_ATAQUE = 0

    def __init__(self, id, energia, pos_x, aldea):
        super().__init__(id, energia, pos_x, True, HERBIVORO, False, aldea)

    def desplazar(self, distancia, direccion):
        super().desplazar(distancia, direccion, ENERGIA_TRICE)

    def recibir_ataque(self, depredador):
        super().recibir_ataque(depredador, POSIB_PRESA_MANADA)

    def elegir_accion(self):
        return super().elegir_accion(self.POSIB_ATAQUE)
