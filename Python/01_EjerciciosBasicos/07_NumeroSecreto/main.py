import os
import utilidades

intentos = 1
numero_secreto = utilidades.pedir_entero('Introduce el número secreto: ')
utilidades.borrarPantalla()
adivinado = False

while not adivinado:
    numero = utilidades.pedir_entero('Adivina el número: ')
    if (numero != numero_secreto):
        intentos += 1
        print('Intentalo de nuevo')
    else:
        adivinado = True
        print('Enhorabuena has adivinado el número secreto (%d) en %d intentos' % (numero_secreto, intentos))
