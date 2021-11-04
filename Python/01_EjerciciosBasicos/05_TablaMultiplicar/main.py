import utilidades

numero = utilidades.pedir_entero('Introduce un número: ')

for i in range(1, 11):
    print(numero, 'x', i, '=', (numero*i))
