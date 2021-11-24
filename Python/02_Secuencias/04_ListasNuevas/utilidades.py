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
    numero = pedir_entero('Número de palabras de la lista: ')

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


def borrar_repetidos(lista):
    for i in range(len(lista)-1, -1, -1):
        if lista[i] in lista[:i]:
            del(lista[i])
    return lista


def elementos_comunes(lista1, lista2):
    return [i for i in lista1 if i in lista2]


def elementos_solo_una_lista(lista1, lista2):
    return [i for i in lista1 if i not in lista2]
