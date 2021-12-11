from delincuente import Delincuente
import utilidades as ut


class FactoriaDelincuente:

    @staticmethod
    def crear_delincuente():
        """Crea un delincuente"""
        id_delincuente = input("Id del delincuente: ")
        nombre = input("Nombre del delincuente: ")
        n = ut.pedir_entero("Número de delitos: ")
        delitos = [input("Delito: ") for _ in range(n)]
        return Delincuente(id_delincuente, nombre, delitos)
