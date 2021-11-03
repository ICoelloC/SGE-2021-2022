def pedir_entero(mensaje):
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input(mensaje))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


def es_primo(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        return all(numero % i != 0 for i in range(2, numero))
