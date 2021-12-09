from dinosaurio import Dinosaurio
from constantes import CARNIVORO, ENERGIA_ATACAR, DIR_IZQDA, DIR_DCHA


class Cazador(Dinosaurio):

    def __init__(self, id, energia, pos_x, manada, bipedo, aldea):
        super().__init__(id, energia, pos_x, manada, CARNIVORO, bipedo, aldea)

    def atacar(self, presa):
        if not self.vivo:
            raise ValueError("No puede atacar. Está muerto")
        if self.energia < ENERGIA_ATACAR:
            raise ValueError("No puede atacar. Energía insuficiente")
        distancia = self.pos_x - presa.pos_x
        energia_necesaria = abs(distancia) * 2 + ENERGIA_ATACAR
        if self.energia < energia_necesaria:
            raise ValueError("No puede atacar. Energía insuficiente. Necesita: " +energia_necesaria + ", Tiene: " + self.energia)
        if distancia < 0:
            self.desplazar(abs(distancia), DIR_IZQDA)
        else:
            self.desplazar(abs(distancia), DIR_DCHA)
        self.energia -= energia_necesaria
        presa.recibir_ataque(self)

    def recibir_ataque(self, depredador, prob_vivir):
        super().recibir_ataque(depredador, prob_vivir)
