import utilidades

numero = utilidades.pedir_entero('Introduce un número: ')

if utilidades.es_primo(numero):
    print(numero, 'es primo')
else:
    print(numero, 'no es primo')
