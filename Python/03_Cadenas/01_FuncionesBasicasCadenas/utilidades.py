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


def iniciales(cadena):
    lista = cadena.split(" ")
    return "".join(palabra[0] for palabra in lista)



def capitalizar(cadena):
    lista = cadena.split(" ")
    return "".join(palabra.capitalize() + " " for palabra in lista)



def palabras_comienzan_a(cadena):
    lista = cadena.split(" ")
    return "".join(
        palabra + " "
        for palabra in lista
        if palabra.startswith("a") or palabra.startswith("A")
    )
