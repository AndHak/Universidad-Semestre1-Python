nombres = []
identificaciones = []

tamaño = 3

for i in range(tamaño):
    print("ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificacion = input("Identificacion: ")

    nombres.append(nombre)
    identificaciones.append(identificacion)

for i in range(tamaño):
    print("Los datos de la persona", i + 1)
    print("Nombre: ", nombres[i])
    print("identificacion: ", identificaciones[i])
