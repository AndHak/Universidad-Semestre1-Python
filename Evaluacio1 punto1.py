#1.   Se tiene una cantidad de números dada, determinar el primo mayor, el Fibonacci menor,
#el par menor y realizar la multiplicación de ellos con sumas.25%
def punto1():
    import random
    numeros = []
    for i in range(20):
        num = random.randint(1, 100)
        numeros.append(num)
    print(numeros)
    contador_fibonaccis = 0
    contador_primos = 0
    contador_pares = 0
    for n in numeros:
        num1 = 0
        num2 = 1
        secuencia = 0
        while secuencia <= n:
            secuencia = num1 + num2
            num1 = num2
            num2 = secuencia
            if secuencia == n:
                contador_fibonaccis += 1
                if contador_fibonaccis == 1:  
                    fibonacci_menor = n
                else:
                    if n < fibonacci_menor:
                        fibonacci_menor = n
        divisores = 0
        condicion = 1
        while condicion <= n:
            if n % condicion == 0:
                divisores += 1
            condicion += 1
        if divisores == 2:
            contador_primos += 1
            if contador_primos == 1:
                primo_mayor = n
            else:
                if n > primo_mayor:
                    primo_mayor = n
        if n % 2 == 0:
            contador_pares += 1
            if contador_pares == 1:
                par_menor = n
            else:
                if n < par_menor:
                    par_menor = n
    producto_prueba = fibonacci_menor * par_menor * primo_mayor
    print(fibonacci_menor, "x", primo_mayor, "x", par_menor, "=", producto_prueba)
    suma = 0
    condicion = 1
    suma2 = 0
    while condicion <= par_menor:
        suma += fibonacci_menor
        condicion += 1
    condicion = 1
    while condicion <= primo_mayor:
        suma2 += suma
        condicion += 1
    resultado = suma2
    print("Resultado: ", resultado)
punto1()
