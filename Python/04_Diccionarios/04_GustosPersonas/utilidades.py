def pedir_cadena(mensaje):
    valido = False
    while not valido:
        cadena = input(mensaje)
        if cadena != "":
            valido = True
        else:
            print("Error, formato no valido")
    return cadena


def generar_diccionario_gustos():
    gustos = {}
    nombre = pedir_cadena("Nombre: ")
    while nombre != "*":
        gusto = pedir_cadena("Gusto: ")
        lista_gustos = gustos.setdefault(nombre, [gusto])
        if lista_gustos != [gusto]:
            gustos[nombre].append(gusto)
        nombre = pedir_cadena("Nombre: ")
    return gustos
