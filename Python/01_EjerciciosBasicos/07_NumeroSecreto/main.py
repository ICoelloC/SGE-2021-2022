import os
import utilidades
import random

intentos = 1
numero_secreto = utilidades.pedir_entero('Introduce el número secreto: ')
utilidades.borrar_pantalla()
adivinado = False

while not adivinado:
    numero = random.uniform(1,100)
    if (numero != numero_secreto):
        intentos += 1
        if (numero > numero_secreto):
            print('El número es menor')
        else:
            print('El número es mayor')
        print('Intentalo de nuevo')
    else:
        adivinado = True
        print('Enhorabuena has adivinado el número secreto (%d) en %d intentos' % (numero_secreto, intentos))
