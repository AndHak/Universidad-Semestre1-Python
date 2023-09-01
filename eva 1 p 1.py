def evaluacion_1_punto_1():
    cantidad=int(input("Cantidad de numeros->"))
    contador=1
    primos=0
    fibonaccis=0
    pares=0
    primo_mayor = 0
    while contador<=cantidad:
        num=int(input("Ingrese el número->"))
        condicion=1
        divisores=0
        while condicion<=num:
            if num % condicion == 0:
                divisores+=1
            condicion+=1
        if divisores==2:
            primos+=1
            if primos==1:
                primo_mayor=num
            else:
                if num>primo_mayor:
                    primo_mayor=num
        num1=0
        num2=1
        secuencia=0
        while secuencia<=num:
            secuencia = num1 + num2
            num1=num2
            num2=secuencia
            if secuencia == num:
                fibonaccis += 1
                if fibonaccis == 1:
                    fibonacci_menor=num
                else:
                    if num < fibonacci_menor:
                        fibonacci_menor=num
        if num % 2==0:
            pares+=1
            if pares == 1:
                par_menor=num
            else:
                if num<par_menor:
                    par_menor=num
        contador+=1
        
    #realizar la multiplicacion de ellos con sumas
        
    suma=0
    condicion=1
    suma2=0
    while condicion<=par_menor:
        suma += fibonacci_menor
        condicion+=1
    condicion=1
    resultado=suma
    while condicion<=primo_mayor:
        suma2+=resultado
        condicion+=1
    resultado=suma2
    print("La multiplicación con sumas es: ", resultado)
evaluacion_1_punto_1()