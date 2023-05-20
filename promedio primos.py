#fibonacci mayor y el primo menor y el promedio de los pares entre estos dos numeros
cantidad = int(input("cuantos numeros va a ingresar"))
contador = 1
contador_de_fibonacci = 0
contador_de_primos = 0
while contador <= cantidad:
    num = int(input("ingrese un numero"))
    secuencia = 0
    num1 = 0
    num2 = 1
    generador = 1
    condicion = 1
    divisores_primos = 0
    while condicion<=num:
        if num % condicion == 0:
            divisores_primos = divisores_primos + 1
        condicion = condicion + 1
    if divisores_primos == 2:
        contador_de_primos = contador_de_primos + 1
        if contador_de_primos == 1:
            primo_menor = num
        else:
            if num<primo_menor:
                primo_menor = num
    #sacar el primo menor funciona bien ahora sacar el mayor fibonacci
    while secuencia < num:
        secuencia = num1 + num2
        num1 = num2
        num2 = secuencia
    if secuencia == num:
        contador_de_fibonacci = contador_de_fibonacci + 1
        if contador_de_fibonacci == 1:
            fibonacci_mayor = num
        else:
            if num>fibonacci_mayor:
                fibonacci_mayor = num
    #sacar el fibonacci mayor funciona bien ahora a sacar el promedio de los pares entre estos dos numeros
    contador = contador + 1

print("el promedio de los pares entre", primo_menor, "y", fibonacci_mayor, "=")

contador_pares = 0
suma = 0

while primo_menor <= fibonacci_mayor:
    if primo_menor % 2 == 0:
        suma = suma + primo_menor
        contador_pares = contador_pares + 1
    primo_menor = primo_menor + 1

promedio = suma/contador_pares

print(promedio)
print("porque", suma, "/", contador_pares, "=", promedio)



