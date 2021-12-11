from factoria_coordinador_patrulla import FactoriaCoordinadorPatrulla
from factoria_policia import FactoriaPolicia
from patrulla import Patrulla
import utilidades as ut


class FactoriaPatrulla:

    @staticmethod
    def crear_patrulla():
        id_patrulla = input("Id de la patrulla: ")
        coordinador = FactoriaCoordinadorPatrulla.crear_coordinador(id_patrulla)
        correcto = False
        while not correcto:
            try:
                ciberpolicias = FactoriaPatrulla.crear_ciberpolicias(id_patrulla)
                p = Patrulla(id_patrulla, coordinador, ciberpolicias)
                correcto = True
            except ValueError:
                print("Debes introducir al menos 4 ciberpolicías")
        return p

    @staticmethod
    def crear_ciberpolicias(id_poli):
        num_policias = ut.pedir_entero("Número de ciberpolicías: ")
        return [FactoriaPolicia.crear_policia(id_poli) for _ in range(num_policias)]
