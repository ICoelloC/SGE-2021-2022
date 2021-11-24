import utilidades

anio = utilidades.pedir_entero('Introduce el año: ')

if utilidades.es_bisiesto(anio):
    print(anio,'es bisiesto')
else:
    print(anio,'no es bisiesto')
