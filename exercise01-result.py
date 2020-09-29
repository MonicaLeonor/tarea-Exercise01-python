# Lista sin elementos
lista = []

# Pedir datos por pantalla al usuario
print("Introduza los datos, para parar introduzca 0 en todas las opciones")
cliente = input("Nombre cliente: ")
producto = input("Nombre producto: ")
costo = float(input("Costo ($0.00): "))

# Creacion del diccionario y llenado de la lista con el diccionario
registro = dict(cliente=cliente, producto=producto, costo=costo)
lista.append(registro)

# Bucle que permite introducir la cantidad de datos deseados
while cliente and producto and costo != 0:
    print("Introduza los datos, para parar introduzca 0 en todas las opciones")
    cliente = input("Nombre cliente: ")
    producto = input("Nombre producto: ")
    costo = float(input("Costo ($0.00): "))

    registro = dict(cliente=cliente, producto=producto, costo=costo)
    lista.append(registro)

# Imprimir por pantalla el costo total hasta el momento
costoTotal = sum(element["costo"] for element in lista)
print("El costo total hasta el momento es de $" + str(costoTotal) + " dolares")
