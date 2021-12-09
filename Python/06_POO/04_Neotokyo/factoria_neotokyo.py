import utilidades as ut
from patrulla import Patrulla
from policia import Policia
from jefe_patrulla import JefePatrulla
from delincuente import Delincuente


def crear_delincuente():
    id_delincuente = ut.pedir_entero("Id del delincuente: ")
    nombre = input("Nombre del delincuente: ")
    num_delitos = ut.pedir_entero("Num delitos: ")
    delitos = [input("Delito: ") for _ in range(num_delitos)]
    return Delincuente(id_delincuente, nombre, delitos)


def crear_jefe(id_pat):
    id_jefe = ut.pedir_entero("Id del jefe de patrulla: ")
    nombre = input("Nombre del coordinador: ")
    n_placa = ut.pedir_entero("Número de placa: ")
    jefe = JefePatrulla(id_jefe, nombre, n_placa, id_pat)
    jefe.delincuentes = registrar_delincuentes()
    return jefe


def registrar_delincuentes():
    num_del = ut.pedir_entero("Número de delincuentes: ")
    return [crear_delincuente() for _ in range(num_del)]


def crear_policia(id_pat):
    id_poli = ut.pedir_entero("Id policía: ")
    nombre = input("Nombre policía: ")
    num_placa = ut.pedir_entero("Num placa: ")
    return Policia(id_poli, nombre, num_placa, id_pat)


def crear_patrulla():
    id_patrulla = ut.pedir_entero("Id de la patrulla: ")
    jefe = crear_jefe(id_patrulla)
    correcto = False
    while not correcto:
        try:
            policias = crear_policia(id_patrulla)
            p = Patrulla(id_patrulla, jefe, policias)
            correcto = True
        except ValueError:
            print("Debes introducir al menos 5 policias")
    return p


def crear_policias(id):
    num_polis = ut.pedir_entero("Número de policias: ")
    return [crear_policia(id) for _ in range(num_polis)]
