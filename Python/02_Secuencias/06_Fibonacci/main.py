import utilidades

limite = utilidades.pedir_entero("Limite  de la sucesión: ")

lista = [utilidades.fibonacci(i) for i in range(limite)]

print("Sucesión de Fibonacci hasta el número", limite, "-->", lista)
