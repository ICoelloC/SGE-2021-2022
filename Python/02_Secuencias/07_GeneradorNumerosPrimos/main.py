import utilidades

v_max = utilidades.pedir_entero("Introduce el rango maximo para generar numeros primos: ")
lista = utilidades.generador_primos(v_max)
print(lista)