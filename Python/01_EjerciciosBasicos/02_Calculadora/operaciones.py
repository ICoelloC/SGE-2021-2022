import utilidades

msg1 = "Primer valor: "
msg2 = "Segundo valor: "


def sumar():

    num1 = utilidades.pedir_entero(msg1)
    num2 = utilidades.pedir_entero(msg2)
    return num1+num2


def restar():
    num1 = utilidades.pedir_entero(msg1)
    num2 = utilidades.pedir_entero(msg2)
    return num1 - num2


def multiplicar():
    num1 = utilidades.pedir_entero(msg1)
    num2 = utilidades.pedir_entero(msg2)
    return num1 * num2


def dividir():
    num2 = 0
    num1 = utilidades.pedir_entero(msg1)
    while num2 == 0:
        num2 = utilidades.pedir_entero(msg2)
    return num1 / num2


def potencia():
    base = utilidades.pedir_entero("Introduce la base: ")
    exp = utilidades.pedir_entero("Introduce el exponente: ")
    return base ** exp
