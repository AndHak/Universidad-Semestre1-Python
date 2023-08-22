#2.	Se tiene un vector con datos numéricos eliminar los números pares.
def taller_2_punto_2():
    cantidad = int(input("Cantidad de numeros"))
    numeros = []
    vector_final = []
    contador = 1
    while contador <= cantidad:
        num = int(input("Ingrese un numero"))
        numeros.append(num)
        contador += 1

    for n in numeros:
        if n % 2 != 0:
            vector_final.append(n)

    print(vector_final)
taller_2_punto_2()