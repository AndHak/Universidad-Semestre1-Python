#Suma del segundo y tercer fibonacci y determinar si es un numero primo
print("")
cantidad = int(input("Cantidad de numeros que va a ingresar"))
contador = 1
contador_de_fibonacci = 0
while contador <= cantidad:
    num = int(input("ingrese un numero: "))
    num1 = 0
    num2 = 1
    secuencia = 0
    while secuencia <= num:
        secuencia = num1 + num2
        num1 = num2
        num2 = secuencia
        if secuencia == num:
            contador_de_fibonacci = contador_de_fibonacci + 1
            if contador_de_fibonacci == 2:
                fibo2 = num
            else:
                if contador_de_fibonacci == 3:
                    fibo3 = num
    contador = contador + 1
divisores_exactos = 0
suma = 0
suma = fibo2 + fibo3
condicion = 1
while condicion <= suma:
    if suma % condicion == 0:
        divisores_exactos = divisores_exactos + 1
    condicion = condicion + 1
if divisores_exactos == 2:
    print(suma, "es un numero primo")
else:
    print(suma, "No es un numero primo")