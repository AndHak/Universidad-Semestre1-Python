#Se tiene una cantidad de dada de numeros, sacar el producto del fibonacci mayor con el primo mayor
# con sumas y hallar las tabla de multiplicar del los multiplos de 3 entre el fibonacci menor ingresado y el producto
#y encontrar el factorial de la resta del primo mayor con el fibonacci menor

cantidad = int(input("Cantidad de numero"))
contador = 1
contador_primos = 0
contador_fibonacci = 0
while contador <= cantidad:
    num = int(input("Ingrese un numero"))
    divisores_primos = 0
    condicion_primos = 1
    while condicion_primos <= num:
        if num % condicion_primos == 0:
            divisores_primos = divisores_primos + 1
        condicion_primos = condicion_primos + 1
    if divisores_primos == 2:
        contador_primos = contador_primos + 1
        if contador_primos == 1:
            primo_menor = num
            primo_mayor = num
        else:
            if num>primo_mayor:
                primo_mayor = num
            if num<primo_menor:
                primo_menor = num
    num1 = 0
    num2 = 1
    secuencia = 0
    while secuencia <= num:
        secuencia = num1 + num2
        num1 = num2
        num2 = secuencia
        if secuencia == num:
            contador_fibonacci = contador_fibonacci + 1
            if contador_fibonacci == 1:
                fibonacci_mayor = num
                fibonacci_menor = num
            else:
                if num>fibonacci_mayor:
                    fibonacci_mayor = num
                if num<fibonacci_menor:
                    fibonacci_menor = num
    contador = contador + 1

print(fibonacci_mayor, fibonacci_menor)
print(primo_mayor, primo_menor)
#al parecer funciona bien, ahora el producto de fibonacci mayor con el primo mayor con sumas

producto = 0
condicion = 1

if fibonacci_mayor<primo_mayor:
    while condicion <= primo_mayor:
        producto = producto + fibonacci_mayor
        condicion = condicion + 1
else:
    if primo_mayor<fibonacci_mayor:
        while condicion <= fibonacci_mayor:
            producto = producto + primo_mayor
            condicion = condicion + 1

print(producto)
#al parecer funciona bien ahora hallar las tabla de multiplicar del los multiplos de 3 entre el fibonacci menor ingresado y el producto

calculo_fibonacci_resta = fibonacci_menor

while fibonacci_menor <= producto:
    if fibonacci_menor % 3 == 0:
        multiplicador = 1
        resultado = 0
        print("tabla del", fibonacci_menor)
        while multiplicador <= 10:
            resultado = fibonacci_menor * multiplicador
            print(fibonacci_menor, "x", multiplicador, "=", resultado)
            multiplicador = multiplicador + 1
    fibonacci_menor = fibonacci_menor + 1

#y encontrar el factorial de la resta del primo mayor con el fibonacci menor

resta = primo_mayor - calculo_fibonacci_resta
print(primo_mayor, "-", calculo_fibonacci_resta)
print("=", resta)
condicion_factorial = 1
resultado_factorial = 1
while condicion_factorial <= resta:
    resultado_factorial = resultado_factorial * condicion_factorial
    condicion_factorial = condicion_factorial + 1
print("el factorial de", resta, "es:")
print(resultado_factorial)
        
