#Se tiene una cantidad dada de números, determinar si los Fibonacci 2, 3 y 4 de acuerdo al orden de entrada son consecutivos
#son consecutivos si la suma de dos de ellos es igual al tercero

cantidad = int(input("cantidad"))
contador = 1
contador_fibonacci = 0
while contador <= cantidad:
    num = int(input("ingrese un numero"))
    num1 = 0
    num2 = 1
    secuencia = 0
    while secuencia <= num:
        secuencia = num1 + num2
        num1 = num2
        num2 = secuencia
        if secuencia == num:
            contador_fibonacci += 1
            if contador_fibonacci == 2:
                segundo = num
            elif contador_fibonacci == 3:
                tercero = num
            if contador_fibonacci == 4:
                cuarto = num
    contador += 1

print("segundo numero", segundo)
print("tercer numero", tercero)
print("cuarto numero", cuarto)

if segundo + tercero == cuarto:
    print("son consecutivos")
else:
    print("son fibonacci pero no son consecutivos")