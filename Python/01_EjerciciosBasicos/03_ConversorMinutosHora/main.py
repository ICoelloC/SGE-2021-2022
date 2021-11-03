import utilidades

mnts = utilidades.pedir_entero('Ingrese los minutos: ')
horas, minutos = utilidades.conversion_horas(mnts)
print(horas,'horas y',minutos,'minutos')
