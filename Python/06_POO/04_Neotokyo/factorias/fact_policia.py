from policia import Policia
import utilidades as ut

class FactoriaPolicia:
    def crear_policia(self, id_pat):
        id_poli = ut.pedir_entero("Id policía: ")
        nombre = input("Nombre policía: ")
        num_placa = ut.pedir_entero("Num placa: ")
        return Policia(id_poli, nombre, num_placa, id_pat)
