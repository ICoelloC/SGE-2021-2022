import constantes as cte


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


def generar_lista_codigos(palabra):
    lista_codigos = []
    for caracter in palabra:
        if caracter.islower():
            caracter = caracter.upper()
        lista_codigos.append(cte.codigo[caracter])
    return lista_codigos


def generar_palabra(lista_morse):
    palabra = ""
    for cod in lista_morse:
        for key, valor in cte.codigo.items():
            if valor == cod:
                letra = key
        palabra += letra
    return palabra
