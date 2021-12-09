from factorias import FactroriaYacimiento
from constantes import *
import random


def elegir_presa(yac, dinosaurio):
    encontrado = False
    i = 0
    d = None
    while not encontrado and i < len(yac.dinosaurios):
        d = yac.dinosaurios[i]
        if dinosaurio.id != d.id and d.vivo:
            encontrado = True
        else:
            i += 1
    if not encontrado:
        d = None
    return d


def simular_dinosaurios(aldea):
    for dinosaurio in aldea.dinosaurios:
        if dinosaurio.vivo:
            opcion = dinosaurio.elegir_accion()
            if opcion == ATACAR:
                presa = elegir_presa(aldea, dinosaurio)
                if presa is not None:
                    print(dinosaurio.id + " ataca a " + presa.id)
                    dinosaurio.atacar(presa)
                else:
                    print(dinosaurio.id + " quiere atacar pero no hay presas.")
            elif opcion == COMER:
                print(dinosaurio.id + " come")
                dinosaurio.comer()
            elif opcion == DESPLAZARSE:
                dir = random.randint(0, 2)
                unidades = random.randint(1, 20)
                if dir == 0:  # Derecha
                    print(dinosaurio.id + " se desplaza " + str(unidades) + " metros a la derecha")
                    dinosaurio.desplazar(unidades, DIR_DCHA)
                else:
                    print(dinosaurio.id + " se desplaza " + str(unidades) + " metros a la izquierda")
                    dinosaurio.desplazar(unidades, DIR_IZQDA)


salir = False
yacimiento = FactroriaYacimiento.crear_mundo("Homer", 5, 2, 2)
while not salir or yacimiento.hay_cazadores():
    print(yacimiento)
    simular_dinosaurios(yacimiento)
    parar = input("Desea parar (S/N): ")
    if parar in ["S", "s"]:
        salir = True

print(yacimiento)
print("Fin Simulacion.")
