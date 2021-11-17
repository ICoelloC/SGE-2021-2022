
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

def crear_lista():
    numero = pedir_entero('Número de columnas: ')
    if numero < 1:
        print("Error. Debe ser un número >= 1")
        return -1
    else:
        lista = []
        for i in range(numero):
            print("Palabra ", str(i + 1) + ": ", end="")
            palabra = input()
            lista.append(palabra)
        return lista

