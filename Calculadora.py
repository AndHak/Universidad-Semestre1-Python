repetir = "si"

while repetir.lower() == "si":

    print("Calculadora")
    print("")
    print("1. Suma")
    suma = 0
    print("2. Resta")
    resta = 0
    print("3. Multiplicacion")
    multiplicacion = 1
    print("4. Division")
    division = 0
    print("5. Potenciacion")
    potenciacion = 1
    print("6. Radicación")
    radicacion = 0
    print("7. Modulo")
    modulo = 0
    print("8. Factorial")
    factorial = 0
    print("9. Mayor y menor")
    mayor = 0
    menor = 0
    print("10. Promedio")
    promedio = 0
    print("11. Moda")
    moda = []

    print("")

    operacion = int(input("Que operación desea realizar? "))

    contador = 1

    if operacion == 1:
        cantidad = int(input("Cuantos numeros va a sumar? "))
        while contador <= cantidad:
            num = int(input("Ingrese un número: "))
            suma += num
            contador += 1
        print("La suma total es: ", suma)

    elif operacion == 2:
        cantidad = int(input("Cuantos numeros va a restar? "))
        while contador <= cantidad:
            num = int(input("Ingrese un número: "))
            if contador == 1:
                resta = num
            else:
                resta -= num
            contador += 1
        print("La resta total es: ", resta)

    elif operacion == 3:
        cantidad = int(input("Cuantos numeros va a multiplicar? "))
        while contador <= cantidad:
            num = int(input("Ingrese un número: "))
            multiplicacion *= num
            contador += 1
        print("La multiplicacion total es: ", multiplicacion)

    elif operacion == 4:
        cantidad = int(input("Cuantos numeros va a dividir? "))
        while contador <= cantidad:
            num = int(input("Ingrese un número: "))
            if contador == 1:
                division = num
            else:
                division /= num
            contador += 1
        print("La division total es: ", division)

    elif operacion == 5:
        cantidad = int(input("Cuantos numeros va a calcular su potencia? "))
        while contador <= cantidad:
            print("")
            num = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese la potencia: "))
            potenciacion = num ** num2
            print("")
            print(num, "elevado a la", num2, "es igual a", potenciacion)
            contador += 1

    elif operacion == 6:
        cantidad = int(input("Cuantos numeros va a calcular su raiz? "))
        while contador <= cantidad:
            print("")
            num = int(input("Ingrese el radicando: "))
            num2 = int(input("Ingrese el indice: "))
            radicacion = num ** (1/num2)
            print("")
            print("La raiz", num2, "de", num, "=", radicacion)
            contador += 1

    elif operacion == 7:
        print("Usted ha elegido modulo, puede escoger entre las siguientes opciones")
        print("")
        print("1. Determinar si es un numero par")
        print("2. Determinar si es un numero impar")
        print("3. Determinar si es un numero primo")
        print("4. Determinar si esta en la secuencia de fibonacci")
        print("5. Determinar si es multiplo de algun numero")
        print("6. Minimo como un multiplo (m.c.m)")
        print("7. Maximo como un divisor (M.C.D)")
        print("8. Numero total de divisores")

        operacion_modulo = int(input("Cual es el metodo que desea emplear? "))

        if operacion_modulo == 1:
            cantidad = int(input("Cuantos numeros desea calcular? "))
            while contador <= cantidad:
                num = int(input("Ingrese un número: "))
                if num % 2 == 0:
                    print("El", num, "es un numero par")
                else:
                    print("El", num, "no es un numero par")
                contador += 1

        elif operacion_modulo == 2:
            cantidad = int(input("Cuantos numeros desea calcular? "))
            while contador <= cantidad:
                num = int(input("Ingrese un número: "))
                if num % 2 == 1:
                    print("El", num, "es un numero impar")
                else:
                    print("El", num, "no es un numero impar")
                contador += 1

        elif operacion_modulo == 3:
            cantidad = int(input("Cuantos numeros desea calcular? "))
            while contador <= cantidad:
                num = int(input("Ingrese un número: "))
                condicion = 1
                divisores = 0
                while condicion <= num:
                    if num % condicion == 0:
                        divisores += 1
                    condicion += 1
                if divisores <= 2:
                    print("El", num, "es un numero primo")
                else:
                    print("El", num, "No es un numero primo")
                contador += 1

        elif operacion_modulo == 4:
            cantidad = int(input("Cuantos numeros desea calcular? "))
            while contador <= cantidad:
                num = int(input("Ingrese un número: "))
                num1 = 0
                num2 = 1
                secuencia = 0
                while secuencia <= num:
                    secuencia = num1 + num2
                    num1 = num2
                    num2 = secuencia
                    if secuencia == num:
                        print("El", num, "Es parte de la secuencia de fibonacci")
                    else:
                        print("El", num, "No hace parte de la secuencia de fibonacci")
                contador += 1

        elif operacion_modulo == 5:
            cantidad = int(input("Cuantos numeros desea calcular? "))
            while contador <= cantidad:
                num = int(input("Ingrese un número: "))
                condicion = 1
                divisores = 0
                print("el", num, "Es multiplo de: ")
                while condicion <= 9:
                    if num % condicion == 0:
                        divisores = condicion
                        print(divisores)
                    condicion += 1
                contador += 1
        
        elif operacion_modulo == 6:
            cantidad = int(input("Cuantos numeros desea calcular? "))
            mcm = 1
            while contador <= cantidad:
                num = int(input("Ingrese un número: "))
                a = mcm
                b = num
                while b != 0:
                    temp = b
                    b = a % b
                    a = temp
                mcm = (mcm * num) // a
                contador += 1
            print("El minimo como un multiplo de los numeros es:", mcm)

        elif operacion_modulo == 7:
            cantidad = int(input("Cuantos numeros desea calcular? "))
            mcd = 0
            while contador <= cantidad:
                num = int(input("Ingrese un número: "))
                a = mcd
                b = num
                while b != 0:
                    temp = b
                    b = a % b
                    a = temp
                mcd = a
                contador += 1
            print("El máximo común divisor de los números es:", mcd)
        
        elif operacion_modulo == 8:
            cantidad = int(input("Cuantos numeros desea calcular? "))
            while contador <= cantidad:
                num = int(input("Ingrese un número: "))
                condicion = 1
                divisores = 0
                print("los numeros que dividen al", num, "son: ")
                while condicion <= num:
                    if num % condicion == 0:
                        print(condicion)
                        divisores += 1
                    condicion += 1
                contador += 1

    elif operacion == 8:
        cantidad = int(input("Cuantos numeros desea calcular? "))
        while contador <= cantidad:
            num = int(input("Ingrese un número: "))        
            condicion = 1
            resultado = 1
            while condicion <= num:
                resultado *= condicion
                condicion += 1
            print("El factorial de", num, "es:", resultado)
            contador += 1
        
    elif operacion == 9:
        cantidad = int(input("Cuantos numeros desea calcular? "))
        contador_mayor = 0
        while contador <= cantidad:
            num = int(input("Ingrese un número: "))
            if contador == 1:
                contador_mayor += 1
                if contador_mayor == 1:
                    menor = num
                    mayor = num
            else:
                if num < menor:
                    menor = num
                if num > mayor:
                    mayor = num
            contador += 1
        print("El número mayor es", mayor)
        print("El número menor es", menor)

    elif operacion == 10:
        cantidad = int(input("Cuantos numeros desea calcular? "))
        suma = 0
        promedio = 0
        contador_promedio = 0
        while contador <= cantidad:
            num = int(input("Ingrese un número: "))
            suma += num
            contador_promedio += 1
            contador += 1
        promedio = suma / contador_promedio
        print("El promedio es:", promedio)

    elif operacion == 11:
        cantidad = int(input("¿Cuántos números desea calcular? "))
        lista_numeros = []
        repeticiones = {}
        moda = []
        max_repeticiones = 0

        while contador <= cantidad:
            num = int(input("Ingrese un número: "))
            lista_numeros.append(num)
            contador += 1

        for numero in lista_numeros:
            if numero in repeticiones:
                repeticiones[numero] += 1
            else:
                repeticiones[numero] = 1

        for numero, cantidad in repeticiones.items():
            if cantidad > max_repeticiones:
                max_repeticiones = cantidad

        for numero, cantidad in repeticiones.items():
            if cantidad == max_repeticiones:
                moda.append(numero)

        print("La moda es:", moda)

    print("")

    repetir = input("Desea realizar otra operacion? (si/no): ")

print("Gracias por utilizar la calculadora")