def pedir_entero(mensaje):
    valido = False
    while not valido:
        try:
            numero = int(input(mensaje))
            valido = True
        except ValueError:
            print("Error. Debe introducir un número entero.")
    return numero


def son_iguales(lista, lista2):
    return lista == lista2
