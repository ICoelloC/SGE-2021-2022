from coordinador_patrulla import CoordinadorPatrulla
from factoria_delincuente import FactoriaDelincuente
import utilidades as ut


class FactoriaCoordinadorPatrulla:

    @staticmethod
    def crear_coordinador(id_patrulla):
        id_coordinador = input("Id del coordinador: ")
        nombre = input("Nombre del coordinador: ")
        n_placa = input("Número de placa: ")
        coordinador = CoordinadorPatrulla(id_coordinador, nombre, n_placa, id_patrulla)
        coordinador.delincuentes = FactoriaCoordinadorPatrulla.crear_delincuentes()
        return coordinador

    @staticmethod
    def crear_delincuentes():
        n = ut.pedir_entero("Número de delincuentes: ")
        return [FactoriaDelincuente.crear_delincuente() for _ in range(n)]
