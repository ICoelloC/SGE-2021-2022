from jefe_patrulla import JefePatrulla
from fact_delincuente import FactDelincuente as fd
import utilidades as ut


class FactoriaJefePatrulla:
    def crear_jefe(self, id_pat):
        id_jefe = ut.pedir_entero("Id del jefe de patrulla: ")
        nombre = input("Nombre del coordinador: ")
        n_placa = ut.pedir_entero("Número de placa: ")
        jefe = JefePatrulla(id_jefe, nombre, n_placa, id_pat)
        jefe.delincuentes = self.registrar_delincuentes()
        return jefe

    def registrar_delincuentes(self):
        num_del = ut.pedir_entero("Número de delincuentes: ")
        return [fd.crear_delincuente() for _ in range(num_del)]
