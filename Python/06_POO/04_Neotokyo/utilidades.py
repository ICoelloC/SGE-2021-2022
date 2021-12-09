def pedir_entero(msg):
    correcto = False
    valor = 0
    while not correcto:
        try:
            valor = int(input(msg))
            correcto = True
        except ValueError:
            print("El valor de " + msg + " debe ser numérico entero")
    return valor
