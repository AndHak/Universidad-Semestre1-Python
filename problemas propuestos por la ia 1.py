#Dada una lista de números enteros, debes encontrar el par de números en la lista cuya suma sea la más grande de todos los posibles pares.
#Luego, debes calcular el producto de esos dos números y mostrar el resultado obtenido.
cantidad = int(input("Ingrese la cantidad de números: "))

# Variables para almacenar el par y el producto con la suma máxima
max_suma = float('-inf')
max_par = ()
max_producto = 0

# Variables de control
i = 0
j = i + 1

# Recorremos la lista para encontrar el par con la suma más grande
while i < cantidad - 1:
    num_i = int(input("Ingrese un número: "))
    j = i + 1

    while j < cantidad:
        num_j = int(input("Ingrese otro número: "))

        suma = num_i + num_j
        if suma > max_suma:
            max_suma = suma
            max_par = (num_i, num_j)
            max_producto = num_i * num_j
        
        j = j + 1
    
    i = i + 1

# Mostramos el resultado
print("El par con la suma más grande es:", max_par)
print("El producto de los números del par es:", max_producto)

