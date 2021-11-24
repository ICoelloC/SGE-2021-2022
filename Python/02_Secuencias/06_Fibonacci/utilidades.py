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


def fibonacci(numero):
    if(numero == 0):
        return 0
    elif(numero == 1):
        return 1
    else:
        return (fibonacci(numero-2)+fibonacci(numero-1))
