from delincuente import Delincuente
import utilidades as ut


class FactoriaDelincuente:
    def crear_delincuente(self):
        id_delincuente = ut.pedir_entero("Id del delincuente: ")
        nombre = input("Nombre del delincuente: ")
        num_delitos = ut.pedir_entero("Num delitos: ")
        delitos = [input("Delito: ") for _ in range(num_delitos)]
        return Delincuente(id_delincuente, nombre, delitos)
