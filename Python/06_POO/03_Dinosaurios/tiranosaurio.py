from cazador import Cazador
from constantes import POSIB_PRESA_SOLITARIO, ENERGIA_TREX

class Rex(Cazador):
    POSIB_ATAQUE = 60
    def __init__(self, id, energia, pos_x, aldea):
        super().__init__(id, energia, pos_x, False, True, aldea)

    def desplazar(self, distancia, direccion):
        super().desplazar(distancia, direccion, ENERGIA_TREX)

    def recibir_ataque(self, depredador):
        super().recibir_ataque(depredador, POSIB_PRESA_SOLITARIO)

    def elegir_accion(self):
        return super().elegir_accion(self.POSIB_ATAQUE)