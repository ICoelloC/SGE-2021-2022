from fact_jefe_patrulla import FactoriaJefePatrulla as fjp
from fact_policia import FactoriaPolicia as fp
from patrulla import Patrulla
import utilidades as ut


class FactoriaPatrulla:
    def crear_patrulla(self):
        id_patrulla = ut.pedir_entero("Id de la patrulla: ")
        jefe = fjp.crear_coordinador(id_patrulla)
        correcto = False
        while not correcto:
            try:
                policias = self.crear_ciberpolicias(id_patrulla)
                p = Patrulla(id_patrulla, jefe, policias)
                correcto = True
            except ValueError:
                print("Debes introducir al menos 5 ciberpolicías")
        return p

    def crear_policias(self, id):
        num_polis = ut.pedir_entero("Número de ciberpolicías: ")
        return [fp.crear_policia(id) for _ in range(num_polis)]