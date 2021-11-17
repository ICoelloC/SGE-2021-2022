import utilidades

lista = ['Iván', 'Mario', 'Alonso', 'Almudena', 'Antonio Javier', 'Almudena','Álvaro', 'Chema', 'David', 'David', 'Christian', 'José Antonio']
print(lista)


cadena = input("Nombre a buscar:")
utilidades.is_in_lista(lista, cadena)

cadena = input("Dime un nombre para contar sus apariciones:")
apariciones = lista.count(cadena)
print(cadena, 'aparece', apariciones, 'veces')

valor_a_sutituir = input("Dime un nombre para sustituirlo de la cadena:")
valor_sustitutivo = input("Dime un nuevo nombre para sustituir el anterior: ")


lista = utilidades.sustituir_valor(lista, apariciones, valor_a_sutituir, valor_sustitutivo)

print(lista)
