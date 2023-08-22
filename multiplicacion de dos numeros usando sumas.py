def taller_1_punto_4():
    num = int(input("ingrese el primer numero"))
    num2 = int(input("ingrese el segundo numero"))

    suma = 0
    contador = 1

    while contador <= num2:
        suma = suma + num
        contador = contador + 1

    print("la multiplicacion de", num, "x", num2, "es igual a", suma)
taller_1_punto_4()