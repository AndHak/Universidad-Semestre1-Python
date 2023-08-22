def menu_inicio():
    respuesta = int(input("""Escoja un menu:
          1. Taller 1
          2. Taller 2
          3. Evaluación 1
          4. Evaluación 2"""))
    if respuesta == 1:
        respuesta_taller_1 = int(input("""¿Qué Punto desea ver a continuación:  
                                       1. Área figuras geometricas y mayor y menor 
                                       2. Área figuras geometricas y ordenadas
                                       3. Factura de agua, servicios públicos
                                       4. Multiplicacion de dos numeros con sumas
                                       5. Multiplo de otro
                                       6. Primer numero multiplo del segundo
                                       7. Determinar un numero primo
                                       8. Tablas de multiplicar entre dos valores
                                       9. Primo menor y Fibonacci mayor
                                       10. Suma de factoriales fibonacci
                                       11. promedio factoriales de los numeros primos
                                       12. comparar promedio factoriales primos y fibonacci
                                       13. Tablas de multiplicar entre primo menor y mayor
                                       14. Fibonacci 1, 2 y 3, mayor y menor
                                       15. Primos 2, 3 y 4 y ordenados ascendentemente
                                       16. Primo 2 y 3 consecutivos
                                       17. Dato encontrado y su ubicación
                                       18. Multiplicación con sumas primo mayor y fibonacci menor
                                       19. Promedio pares entre primo mayor y fibonacci menor
                                       20. Potencia con sumas
                                       21. Factorial con sumas
                                       22. Promedio pares primo mayor y fibonacci menor
                                       23. Promedio factorial impares entre primo mayor y fibonacci menor
                                       24. Encontrar primo y fibonacci a la vez
                                       25. Veces que se repite el segundo primo
                                       26. Determinar triangulo equilatero, escaleno o isóceles"""))
        if respuesta_taller_1 == 1:
            #-	Realizar un programa que calcule el área de un triángulo, un rectángulo y un cuadrado, y muestre el área mayor y el área menor.
            def taller_1_punto_1():
                lado_cuadrado = int(input("¿Cuánto mide el lado del cuadrado? "))
                lado_rectangulo1 = int(input("¿Cuánto mide uno de los lados del rectángulo? "))
                lado_rectangulo2 = int(input("¿Cuánto mide el otro lado del rectángulo? "))
                base = int(input("¿Cuánto mide la base del triángulo? "))
                altura = int(input("¿Cuánto mide la altura del triángulo? "))

                area_cuadrado = lado_cuadrado * lado_cuadrado
                print("Área del cuadrado:", area_cuadrado)

                area_rectangulo = lado_rectangulo1 * lado_rectangulo2
                print("Área del rectángulo:", area_rectangulo)

                area_triangulo = (base * altura) / 2
                print("Área del triángulo:", area_triangulo)

                area_mayor = area_cuadrado
                area_menor = area_cuadrado

                if area_mayor < area_rectangulo:
                    area_mayor = area_rectangulo
                if area_mayor < area_triangulo:
                    area_mayor = area_rectangulo
                if area_menor > area_rectangulo:
                    area_menor = area_rectangulo
                if area_menor > area_triangulo:
                    area_menor = area_triangulo

                print("El área mayor es:", area_mayor)
                print("El área menor es:", area_menor)
            taller_1_punto_1()
        if respuesta_taller_1 == 2:
            # -	Realizar un programa que calcule el área de un triángulo, un rectángulo y un cuadrado, y muestre las áreas en orden ascendente
            def taller_1_punto_2():
                lado_cuadrado = int(input("¿Cuánto mide el lado del cuadrado? "))
                lado_rectangulo1 = int(input("¿Cuánto mide uno de los lados del rectángulo? "))
                lado_rectangulo2 = int(input("¿Cuánto mide el otro lado del rectángulo? "))
                base = int(input("¿Cuánto mide la base del triángulo? "))
                altura = int(input("¿Cuánto mide la altura del triángulo? "))

                area_cuadrado = lado_cuadrado * lado_cuadrado
                print("Área del cuadrado:", area_cuadrado)

                area_rectangulo = lado_rectangulo1 * lado_rectangulo2
                print("Área del rectángulo:", area_rectangulo)

                area_triangulo = (base * altura) / 2
                print("Área del triángulo:", area_triangulo)

                if area_triangulo < area_cuadrado:
                    if area_cuadrado < area_rectangulo:
                        print(area_triangulo, area_cuadrado, area_rectangulo)
                    else:
                        if area_rectangulo < area_triangulo:
                            print(area_rectangulo, area_triangulo, area_cuadrado)
                        else:
                            print(area_triangulo, area_rectangulo, area_cuadrado)
                else:
                    if area_cuadrado < area_triangulo:
                        if area_triangulo < area_rectangulo:
                            print(area_cuadrado, area_triangulo, area_rectangulo)
                        else:
                            if area_rectangulo < area_cuadrado:
                                print(area_rectangulo, area_cuadrado, area_triangulo)
                            else:
                                print(area_cuadrado, area_rectangulo, area_triangulo)
            taller_1_punto_2()
        if respuesta_taller_1 == 3:
            #3.	Una empresa de servicios públicos desea calcular el valor de una factura de servicio de agua, teniendo en cuenta lo siguiente
            #Se tiene el código del usuario, consumo mensual en  metros cúbicos, el valor del metro cúbico, el estrato y
            #Se realiza el calculo de acuerdo a la siguiente consideración: Con respecto al estrato  
            #Si el usuario es del estrato 1  descuento del 40%
            #Estrato 2 		descuento del 30%
            #Estrato 3 		descuento del 15%
            #Estrato 4		no tiene descuento
            #Estrato 5 y 6 		Incremento en la factura del 20%
            #Para todos los anteriores si el consumo en metros cúbicos es mayor a 10, sobre al valor anterior se incrementa el  10%,
            def taller_1_punto_3():
                codigos = []
                estratos = []
                i = -1
                while True:
                    pregunta = input("Desea calcular el valor de su factura S/N: ")
                    try:
                        if pregunta.lower() == "n":
                            return taller_1_punto_3
                        if pregunta.lower() == "s":
                            i += 1
                            cod = input("Ingrese el codigo de usuario: ")
                            codigos.append(cod)
                            print("""ESCOJA EL ESTRATO
                                1. Estrato 1
                                2. Estrato 2
                                3. Estrato 3
                                4. Estrato 4
                                5. Estrato 5
                                6. Estrato 6""")
                            estrato = input("Escoja el estrato: ")
                            estratos.append(estrato)
                            try:
                                estrato = int(estrato)
                                if 1 <= estrato <= 4:
                                    gasto = float(input("Gasto de agua en metros cubicos:  "))
                                    incremento = 0
                                    if gasto > 10:
                                        incremento = 0.1
                                        x = "Si"
                                    else:
                                        incremento = 0
                                        x = "No"
                                    gasto *= 13453
                                    descuento = 0
                                    if estrato == 1:
                                        descuento = 0.4
                                    elif estrato == 2:
                                        descuento = 0.3
                                    elif estrato == 3:
                                        descuento = 0.15
                                    else:
                                        descuento = 0
                                    incremento_gasto = gasto * incremento
                                    valor = gasto - (gasto * descuento) + incremento_gasto
                                    
                                    print(f"""FACTURA
                                        cod: {codigos[0]}
                                        estrato: {estratos[0]}
                                        descuento: {descuento * 100}%
                                        incremento: 10% {x}
                                        Incremento por gasto: ${incremento_gasto:.2f}
                                        Total a pagar:  ${valor:.2f}""")
                                    
                                elif estrato == 5 or estrato == 6:
                                    gasto = float(input("Gasto de agua en metros cubicos:  "))
                                    incremento = 0
                                    if gasto > 10:
                                        incremento = 0.1
                                        x = "Si"
                                    else:
                                        incremento = 0
                                        x = "No"
                                    gasto *= 13453
                                    descuento = 0.2
                                    incremento_gasto = gasto * incremento
                                    valor = gasto + (gasto * descuento) + incremento_gasto
                                    
                                    print(f"""FACTURA
                                        cod: {codigos[0]}
                                        estrato: {estratos[0]}
                                        descuento: {descuento * 100}%
                                        incremento: 10% {x}
                                        Incremento por gasto: ${incremento_gasto:.2f}
                                        Total a pagar:  ${valor:.2f}""")
                                else:
                                    print("Estrato no válido")
                            except ValueError:
                                print("Estrato no válido")
                    except ValueError:
                        print("Respuesta inválida")
            taller_1_punto_3()
        if respuesta_taller_1 == 4:
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
        if respuesta_taller_1 == 5:
            #-	Determinar si un número es múltiplo de otro sin utilizar el operador residuo.
            def taller_1_punto_5():
                num1 = int(input("ingrese el primer numero"))
                num2 = int(input("ingrese el segundo numero"))
                multiplo = False
                suma = 0
                while suma <= num2:
                    suma += num1
                    if suma == num2:
                        multiplo = True
                if multiplo:
                    print(num1, "es multiplo de", num2)
                else:
                    print("no es multiplo")
            taller_1_punto_5()
        if respuesta_taller_1 == 6:
            #-	Determinar si un número es múltiplo de otro sin utilizar el operador residuo.
            def taller_1_punto_5():
                num1 = int(input("ingrese el primer numero"))
                num2 = int(input("ingrese el segundo numero"))
                multiplo = False
                suma = 0
                while suma <= num2:
                    suma += num1
                    if suma == num2:
                        multiplo = True
                if multiplo:
                    print(num1, "es multiplo de", num2)
                else:
                    print("no es multiplo")
            taller_1_punto_5()
        if respuesta_taller_1 == 7:
            #7.	Determinar si un número es primo sin utilizar el operador residuo.
            def taller_1_punto_7():
                num1 = int(input("ingrese un numero"))
                primos = 0
                condicion = 1
                divisores = 0
                while condicion <= num1:
                    suma = 0
                    while suma <= num1:
                        suma += condicion
                        if suma == num1:
                            divisores += 1
                    condicion += 1
                if divisores == 2:
                    print(num1,"es primo")
                else:
                    print(num1,"no es primo")
            taller_1_punto_7()
        if respuesta_taller_1 == 8:
            def taller_1_punto_8():
                print("tabla de multiplicar entre dos numeros")
                num1 = int(input("numero uno"))
                num2 = int(input("numero dos"))
                multiplicador = 1
                contador = 1

                while num1 <= num2:
                    print("tabla del", contador)
                    while multiplicador <= 10:
                        resultado = num1 * multiplicador
                        print(num1,"x",multiplicador,"=", resultado)
                        multiplicador = multiplicador + 1
                    contador = contador + 1
                    num1 = num1 + 1
                    multiplicador = 1
            taller_1_punto_8()
        if respuesta_taller_1 == 9:
            def taller_1_punto_9():
                primo_menor = 0
                fibonacci_mayor = 0
                contador_primos = 0
                contador_fibonaccis = 0
                while True:
                    num = input('Presione "c" para terminar, ingrese un número: ')
                    if num == "c":
                        break
                    else:
                        num = int(num)
                        condicion = 1
                        divisores = 0
                        while condicion <= num:
                            if num % condicion == 0:
                                divisores += 1
                            condicion += 1
                        if divisores == 2:
                            contador_primos += 1
                            if contador_primos == 1:
                                primo_menor = num
                            else:
                                if num < primo_menor:
                                    primo_menor = num
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= num:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 = secuencia
                            
                            if secuencia == num:
                                contador_fibonaccis += 1
                                if contador_fibonaccis == 1:
                                    fibonacci_mayor = num
                                else:
                                    if num > fibonacci_mayor:
                                        fibonacci_mayor = num
                if contador_primos > 0:
                    print("El primo menor es:", primo_menor)
                else:
                    print("No se ingresaron números primos.")
                    
                if contador_fibonaccis > 0:
                    print("El Fibonacci mayor es:", fibonacci_mayor)
                else:
                    print("No se ingresaron números en la secuencia de Fibonacci.")
            taller_1_punto_9()
        if respuesta_taller_1 == 10:
        if respuesta_taller_1 == 11:
        if respuesta_taller_1 == 12:
        if respuesta_taller_1 == 13:
        if respuesta_taller_1 == 14:
        if respuesta_taller_1 == 15:
        if respuesta_taller_1 == 16:
        if respuesta_taller_1 == 17:
        if respuesta_taller_1 == 18:
        if respuesta_taller_1 == 19:
            #Se tiene una cantidad de números dada. Encontrar el promedio de los números pares que se encuentran entre el  primo mayor y el Fibonacci menor7
            def taller_1_punto_19():
                cantidad = int(input("ingrese la cantidad de numeros"))
                contador = 1
                primos = 0
                fibonaccis = 0

                while contador <= cantidad:
                    num = int(input("ingrese un numero"))
                    divisores = 0
                    condicion = 1
                    while condicion <= num:
                        if num % condicion == 0:
                            divisores += 1
                        condicion += 1
                    if divisores == 2:
                        primos += 1
                        if primos == 1:
                            mayor = num
                        else:
                            if num>mayor:
                                mayor=num
                    num1 = 0
                    num2 = 1
                    secuencia = 0
                    while secuencia <= num:
                        secuencia = num1 + num2
                        num1 = num2
                        num2 = secuencia
                        if secuencia == num:
                            fibonaccis += 1
                            if fibonaccis == 1:
                                menor = num
                            else:
                                if num<menor:
                                    menor=num
                    contador += 1
                print("primo mayor", mayor)
                print("fibnacci menor", menor)
                print("el promedio de los pares que estan entre", menor, "y", mayor, "es:")
                pares = 0
                suma = 0
                while menor < mayor:
                    if menor % 2 == 0:
                        pares += 1
                        suma += menor
                    menor += 1
                promedio = suma/pares
                print("=",promedio)
            taller_1_punto_19()
        if respuesta_taller_1 == 20:
            #Hallar la potencia de dos números con sumas
            def taller_1_punto_20():
                num1 = int(input("Ingrese un número: "))
                num2 = int(input("Elevado a la potencia: "))
                potencia = 1
                contador = 1
                while contador <= num2:
                    suma = 0
                    condicion = 1
                    while condicion <= num1:
                        suma += potencia
                        condicion += 1
                    potencia = suma
                    contador += 1
                print("El resultado de", num1, "elevado a la potencia", num2, "es:", potencia)
            taller_1_punto_20()
        if respuesta_taller_1 == 21:
        if respuesta_taller_1 == 22:
        if respuesta_taller_1 == 23:
        if respuesta_taller_1 == 24:
            #Se tiene una cantidad de números dada. Encontrar el promedio de los números que son Fibonacci y primos a la vez
            def taller_1_punto_24():
                cantidad = int(input("cantidad de numeros"))
                contador = 1
                fibonaccis_y_primos = 0
                suma_ambos = 0
                while contador <= cantidad:
                    num = int(input("ingrese un numero"))
                    condicion = 1
                    divisores = 0
                    while condicion <= num:
                        if num % condicion == 0:
                            divisores  += 1
                        condicion += 1
                    if divisores == 2:
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= num:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 = secuencia
                            if secuencia == num:
                                suma_ambos += num
                                fibonaccis_y_primos += 1
                    contador += 1
                promedio_total = suma_ambos/fibonaccis_y_primos
                print("promedio total de primos y fibonaccis de los numeros ingresados es", promedio_total)
            taller_1_punto_24()
        if respuesta_taller_1 == 25:
        if respuesta_taller_1 == 26:
    if respuesta == 2:
        respuesta_taller_2 = int(input("""¿Qué Punto desea ver a continuación:  
                                       1. Primo que más se repite
                                       2. Eliminar los numeros pares
                                       3. Eliminar primos y fibonaccis
                                       4. Insertar datos en un vector ordenado
                                       5. Ordenar ascendentemente
                                       6. Primos y fibonacci ordenados
                                       7. Ordenar posiciones pares e impares
                                       8. Mitad de un vector en orden ascendente y descendente
                                       9. Ordenar pares y primos
                                       10. Mostrar repeticiones
                                       11. Multiplos de 3 y rangos correspondientes
                                       12. Vector con primos comunes sin repetidos
                                       13. Vector con fibonaccis comunes sin repetidos
                                       14. Formar un tecer vector que quede ordenado
                                       15. Formar un tercer vector que quede ordenado solo con pares
                                       16. Vector con primos entre fibonacci mayor y menor
                                       17. Promedio multiplos de 3 entre segundo y tercer fibonacci
                                       18. Segundo, tecer fibonacci y sus posiciones, remplazarlas"""))
        if respuesta_taller_2 == 1:
            #1.	Se tiene un vector con datos numéricos repetidos, determinar cuál es el primo que más se repite.
            def taller_2_punto_1():
                cantidad = int(input("Cantidad de números: "))
                numeros = []
                archivo = []
                repetidos = []
                primos_repetidos = []
                
                contador = 1
                while contador <= cantidad:
                    num = int(input("Ingrese un número: "))
                    numeros.append(num)
                    contador += 1
                for n in numeros:
                    if n not in archivo:
                        archivo.append(n)
                    else:
                        repetidos.append(n)
                for n in repetidos:
                    condicion = 1
                    divisores = 0
                    while condicion <= n:
                        if n % condicion == 0:
                            divisores += 1
                        condicion += 1
                    if divisores == 2: 
                        primos_repetidos.append(n)
                if len(primos_repetidos) > 0:
                    print("Los primos que se repiten son:", primos_repetidos)
                else:
                    print("No hay primos repetidos")
            taller_2_punto_1()
        if respuesta_taller_2 == 2:
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
        if respuesta_taller_2 == 3:
            #3.	Se tiene un vector con datos numéricos eliminar los datos que sean primos y Fibonacci.
            numeros_no_fibonaccis_y_no_primos = []
            def taller_2_punto_3():
                while True:
                    try:
                        num = input('Presion "c" para terminar, Ingrese un numero:  ')
                        if num == "c":
                            return
                        else:
                            num = int(num)
                            num1 = 0
                            num2 = 1
                            secuencia = 0
                            fibonacci = False
                            while secuencia <= num:
                                secuencia = num1 + num2
                                num1 = num2
                                num2 = secuencia
                                if secuencia == num:
                                    fibonacci = True
                            condicion = 1
                            divisores = 0
                            primo = False
                            while condicion <= num:
                                if num % condicion == 0:
                                    divisores += 1
                                condicion += 1
                            if divisores == 2:
                                primo = True
                            if not primo and not fibonacci:
                                numeros_no_fibonaccis_y_no_primos.append(num)
                    except ValueError:
                        print('Valor invalido, Ingrese un valor valido')
            taller_2_punto_3()
            print("Los numeros que no son primos ni fibonaccis son:  ", numeros_no_fibonaccis_y_no_primos)
        if respuesta_taller_2 == 4:
            #4.	Se tiene un vector ordenado con datos numéricos, insertar varios datos en la posición que le corresponde
            array1 = [1, 3, 5, 7, 9]
            array2 = [2, 4, 6, 8, 10]
            array1 += array2
            lista = array1
            #BurbleSort
            def taller_2_punto_4():
                for i in range(len(lista)-1):
                    for j in range(len(lista)-1):
                        if lista[j] > lista[j+1]:
                            temporal = lista[j]    
                            lista[j] = lista[j+1]
                            lista[j+1] = temporal
                print(lista)
            taller_2_punto_4()
        if respuesta_taller_2 == 5:
            #5.	Leer una serie de datos numéricos y llenarlos en un vector de tal forma que vayan quedando ordenados ascendentemente
            def taller_2_punto_5():
                numeros = []
                while True:
                    num = input('Presione "c" para terminar, ingrese un número: ')
                    if num == "c":
                        break
                    else:
                        numeros.append(int(num))
                print("Números ingresados:", numeros)
                for i in range(len(numeros)-1):
                    for j in range(len(numeros)-i-1):
                        if numeros[j] > numeros[j+1]:
                            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
                print("Números ordenados ascendentemente:", numeros)
            taller_2_punto_5()
        if respuesta_taller_2 == 6:
            #6.	Leer una serie de datos numéricos y llenarlos en un vector los datos que sean primos y Fibonacci que vayan quedando ordenados descendentemente.
            def taller_2_punto_6():
                def numeros():
                    numeros = []
                    while True:
                        num = input('Precione "c" para terminar, Ingrese un numero')
                        if num == "c":
                            return numeros
                        try:
                            numeros.append(int(num))
                        except ValueError:
                            print('Ingrese un valor valido')
                numeros = numeros()

                def primos_y_fibonaccis():
                    primos_y_fibonaccis = []
                    for i in numeros:
                        es_primo = False
                        condicion = 1
                        divisores = 0
                        while condicion <= i:
                            if i % condicion == 0:
                                divisores += 1
                            condicion += 1
                        if divisores == 2:
                            es_primo = True
                        es_fibonacci = False
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= i:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 = secuencia
                            if secuencia == i:
                                es_fibonacci = True
                        if es_fibonacci or es_primo:
                            primos_y_fibonaccis.append(i)
                    return primos_y_fibonaccis
                    
                primos_y_fibonaccis = primos_y_fibonaccis()

                def particionado(primos_y_fibonaccis):
                    pivote = primos_y_fibonaccis[0]
                    menores = []
                    mayores = []
                    for i in range(1, len(primos_y_fibonaccis)):
                        if primos_y_fibonaccis[i] < pivote:
                            menores.append(primos_y_fibonaccis[i])
                        else:
                            mayores.append(primos_y_fibonaccis[i])
                    return menores, pivote, mayores

                def quicksort(primos_y_fibonaccis):
                    if len(primos_y_fibonaccis) < 2:
                        return primos_y_fibonaccis
                    menores, pivote, mayores = particionado(primos_y_fibonaccis)
                    return quicksort(mayores) + [pivote] + quicksort(menores)

                resultado = quicksort(primos_y_fibonaccis)
                print(resultado)
            taller_2_punto_6()
        if respuesta_taller_2 == 7:
            #7.	Se tiene un vector con datos numéricos, ordenar las posiciones pares en orden ascendente y las impares en orden descendente.
            def taller_2_punto_7():
                def ordenar_posiciones_pares_impares(vector):
                    # Función de ordenamiento de burbuja para las posiciones pares
                    def bubble_sort_pares(lista):
                        for i in range(len(lista)- 1):
                            for j in range(len(lista) - i - 1):
                                if lista[j] > lista[j + 1]:
                                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    # Función de ordenamiento de burbuja para las posiciones impares
                    def bubble_sort_impares(lista):
                        for i in range(len(lista)- 1):
                                for j in range(len(lista) - i - 1):
                                    if lista[j] < lista[j + 1]:
                                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    # Obtener los valores en posiciones pares e impares
                    pares = [vector[i] for i in range(len(vector)) if i % 2 == 0]
                    impares = [vector[i] for i in range(len(vector)) if i % 2 != 0]
                    # Ordenar los valores en posiciones pares e impares
                    bubble_sort_pares(pares)
                    bubble_sort_impares(impares)
                    # Construir el vector resultante manteniendo las posiciones pares e impares
                    vector_resultante = []
                    posiciones_pares = 0
                    posiciones_impares = 0
                    for i in range(len(vector)):
                        if i % 2 == 0:
                            vector_resultante.append(pares[posiciones_pares])
                            posiciones_pares += 1
                        else:
                            vector_resultante.append(impares[posiciones_impares])
                            posiciones_impares += 1
                    return vector_resultante
                #Prueba para probar si la funcion sirve
                numeros = [9, 2, 7, 4, 5, 6, 3, 8, 1, 10]
                vector_resultante = ordenar_posiciones_pares_impares(numeros)
                print(vector_resultante)  #[1, 10, 3, 8, 5, 6, 7, 4, 9, 2] Tiene que dar
            taller_2_punto_7()
        if respuesta_taller_2 == 8:
            #8.	Se tiene un vector con datos numéricos, ordenar la mitad del vector en orden ascendente y la otra mitad en orden descendente.
            def taller_2_punto_8():
                numeros = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
                def orden_ascendente_descendente(lista):
                    mitad = len(lista) // 2
                    # Ordenar la primera mitad en forma ascendente usando el algoritmo de burbuja
                    for i in range(mitad):
                        for j in range(mitad - 1):
                            if lista[j] > lista[j + 1]:
                                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    # Ordenar la segunda mitad en forma descendente usando el algoritmo de burbuja
                    for i in range(mitad, len(lista)):
                        for j in range(mitad, len(lista) - 1):
                            if lista[j] < lista[j + 1]:
                                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    return lista
                resultado = orden_ascendente_descendente(numeros)
                print(resultado)  # Resultado: [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
            taller_2_punto_8()
        if respuesta_taller_2 == 9:
            #9.	Se tiene un vector con datos numéricos, formar dos vectores uno con los números pares
            # #y otro con los números primos y ordenarlos ascendente y descendente respectivamente.
            def taller_2_punto_9():
                numeros = [2, 3, 5, 75, 59, 61, 67, 71, 89, 97, 11, 13, 17, 19, 23, 29, 31, 28, 6 , 7, 8, 99, 22, 24, 44, 66, 64, 75, 37, 41, 43, 47]
                pares = []
                primos = []
                for i in numeros:
                    condicion = 1
                    divisores = 0
                    while condicion <= i:
                        if i % condicion == 0:
                            divisores += 1
                        condicion += 1
                    if divisores == 2:
                        primos.append(i)
                    if i % 2 == 0:
                        pares.append(i)
                #Orden ascendente
                for i in range(len(primos)-1):
                    for j in range(len(primos)-i-1):
                        if primos[j] > primos[j+1]:
                            temporal = primos[j]
                            primos[j] = primos[j+1]
                            primos[j+1] = temporal
                print("primos", primos)
                for i in range(len(pares)-1):
                    for j in range(len(pares)-i-1):
                        if pares[j] > pares[j+1]:
                            temporal = pares[j]
                            pares[j] = pares[j+1]
                            pares[j+1] = temporal
                print("Pares", pares)
                #Orden descendente
                for i in range(len(primos)-1):
                    for j in range(len(primos)-i-1):
                        if primos[j] < primos[j+1]:
                            temporal = primos[j]
                            primos[j] = primos[j+1]
                            primos[j+1] = temporal
                print("primos", primos)
                for i in range(len(pares)-1):
                    for j in range(len(pares)-i-1):
                        if pares[j] < pares[j+1]:
                            temporal = pares[j]
                            pares[j] = pares[j+1]
                            pares[j+1] = temporal
                print("Pares", pares)
            taller_2_punto_9()
        if respuesta_taller_2 == 10:
            #10.	Se tiene un vector con datos numéricos ordenados y repetidos
            # #mostrar los números y las veces que se repiten utilizando el concepto de rompimiento de control.
            def taller_2_punto_10():
                import random
                numeros = [random.randint(1, 10) for n in range(20)]
                for i in range(len(numeros) - 1):
                    for j in range(len(numeros) - i - 1):
                        if numeros[j] > numeros[j + 1]:
                            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
                print(numeros)
                contador_actual = 1
                for i in range(1, len(numeros)):
                    if numeros[i] == numeros[i - 1]:
                        contador_actual += 1
                    else:
                        print(f"Número", numeros[i - 1], "Repeticiones:", contador_actual)
                        contador_actual = 1
                print(f"Número", numeros[-1], "Repeticiones:", contador_actual)
            taller_2_punto_10()
        if respuesta_taller_2 == 11:
            #11.	Se tienen dos vectores con datos numéricos, en el primer vector hay números múltiplos de tres
            # #que determinan la cantidad de datos de rangos correspondientes al vector dos,
            # #encontrar el mayor, el menor y el promedio de cada rango.
            def taller_2_punto_11():
                datos = []
                rango = []
                cantidad_rangos = int(input("Cantidad de rangos: "))
                cantidad_datos = int(input("Cantidad total de datos: "))          
                for i in range(cantidad_rangos):
                    rango_valor = int(input("Ingrese el valor del rango {}: ".format(i)))
                    rango.append(rango_valor)              
                for j in range(cantidad_datos):
                    dato_valor = int(input("Ingrese el dato {}: ".format(j)))
                    datos.append(dato_valor)               
                rango_actual = 0
                indice_datos = 0             
                while rango_actual < cantidad_rangos:
                    if rango[rango_actual] % 3 == 0:
                        limite_superior = indice_datos + rango[rango_actual]
                        max_valor = datos[indice_datos]
                        min_valor = datos[indice_datos]
                        suma = 0
                        contador = 0                       
                        while indice_datos < limite_superior:
                            contador += 1
                            suma += datos[indice_datos]
                            promedio = suma / contador
                            if datos[indice_datos] > max_valor:
                                max_valor = datos[indice_datos]
                            elif datos[indice_datos] < min_valor:
                                min_valor = datos[indice_datos]
                            indice_datos += 1
                        print("Rango", rango_actual, "Mayor:", max_valor, "Menor:", min_valor, "Promedio del rango:", promedio)
                    rango_actual += 1
            taller_2_punto_11()
        if respuesta_taller_2 == 12:
            #12.	Se tienen dos vectores con datos numéricos formar un vector con los primos comunes sin datos repetidos.
            def taller_2_punto_12():
                import random
                array1 = [random.randint(1, 100) for n in range(50)]
                array2 = [random.randint(1, 100) for n in range(50)]
                primos1 = []
                primos2 = []
                for i in array1:
                    condicion = 1
                    divisores = 0
                    while condicion <= i:
                        if i % condicion == 0:
                            divisores += 1
                        condicion += 1
                    if divisores == 2:
                        primos1.append(i)
                for i in array2:
                    condicion = 1
                    divisores = 0
                    while condicion <= i:
                        if i % condicion == 0:
                            divisores += 1
                        condicion += 1
                    if divisores == 2:
                        primos2.append(i)
                primos_comunes = [n for n in primos2 if n in primos2 and n in primos1]
                primos_comunes_sin_repetirse = []
                for i in primos_comunes:
                    if i not in primos_comunes_sin_repetirse:
                        primos_comunes_sin_repetirse.append(i)
                print('Primos comunes sin repetirse')
                print(primos_comunes_sin_repetirse)
            taller_2_punto_12()
        if respuesta_taller_2 == 13:
            #13.	Se tienen dos vectores con datos numéricos formar un vector con la unión de los Fibonacci sin repetidos.
            def taller_2_punto_13():
                import random
                array1 = []
                array2 = []
                for i in range(500):
                    num = random.randint(1,1000)
                    array1.append(num)
                for i in range(500):
                    num = random.randint(1,1000)
                    array2.append(num)
                #identificar fionaccis
                array3 = array1 + array2
                nummeros_fibonaccis = []
                for i in array3:
                    num1 = 0
                    num2 = 1
                    secuencia = 0
                    while secuencia <= i:
                        secuencia = num1 + num2
                        num1 = num2
                        num2 = secuencia
                        if secuencia == i:
                            nummeros_fibonaccis.append(i)
                for i in range(len(nummeros_fibonaccis)-1):
                    for j in range(len(nummeros_fibonaccis)-i-1):
                        if nummeros_fibonaccis[j] > nummeros_fibonaccis[j+1]:
                            temporal = nummeros_fibonaccis[j]
                            nummeros_fibonaccis[j] = nummeros_fibonaccis[j+1]
                            nummeros_fibonaccis[j+1] = temporal
                resultado = []
                for n in nummeros_fibonaccis:
                    if n not in resultado:
                        resultado.append(n)
                print(resultado)
            taller_2_punto_13()
        if respuesta_taller_2 == 14:
            #14.	Se tiene dos vectores con datos numéricos, el uno ordenado ascendentemente 
            #y el otro ordenado descendentemente, formar un tercer vector por mezcla
            #de tal forma que quede ordenado descendentemente.
            def taller_2_punto_14():
                #Random arrays
                import random
                numbers1 = []
                numbers2 = []
                for i in range(20):
                    num = random.randint(1,30)
                    numbers1.append(num)
                for i in range(20):
                    num = random.randint(1,30)
                    numbers2.append(num)
                print(numbers1)
                print(numbers2)
                #Formar QuickSort para llamar a las funciones
                #Particionado
                def particionado(vector):
                    pivote = vector[0]
                    menores = []
                    mayores = []
                    for i in range(1, len(vector)):
                        if vector[i] < pivote:
                            menores.append(vector[i])
                        else:
                            mayores.append(vector[i])
                    return menores, pivote, mayores
                #Definir Quicksort para ascendente y descedente
                def quicksort_ascendente(vector):
                    if len(vector) < 2:
                        return vector
                    menores, pivote, mayores = particionado(vector)
                    return quicksort_ascendente(menores) + [pivote] + quicksort_ascendente(mayores)
                #Quicksort descendente
                def quicksort_descendente(vector):
                    if len(vector) < 2:
                        return vector
                    menores, pivote, mayores = particionado(vector)
                    return quicksort_descendente(mayores) + [pivote] + quicksort_descendente(menores)
                #Una vez determinadas las respectivas funciones sera mas facil llamarlas para ordenar vectores, algo mas parecido a usar sort
                print('UNION DE LOS ANTERIORES VECTORES')
                numbers3 = numbers1 + numbers2
                print(numbers3)
                vector = numbers3
                resultado = quicksort_ascendente(vector)
                print('VECTOR ORDENADO DE FORMA ASCENDENTE')
                print(resultado)
                print('VECTOR ORDENADO DE FORMA DESCENDENTE')
                resultado = quicksort_descendente(vector)
                print(resultado)
            taller_2_punto_14()
        if respuesta_taller_2 == 15:
            #15.	Se tiene dos vectores con datos numéricos, el uno ordenado ascendentemente
            #y el otro ordenado descendentemente, formar un tercer vector por mezcla de tal forma que
            #quede ordenado descendentemente, solo con números pares.
            def taller_2_punto_15():
                #Random arrays
                import random
                numeros1 = []
                numeros2 = []
                for i in range(20):
                    num = random.randint(1,30)
                    numeros1.append(num)
                for i in range(20):
                    num = random.randint(1,30)
                    numeros2.append(num)
                print(numeros1)
                print(numeros2)
                #orden ascendente para uno using burblesort
                print('ORDENADOS')
                for i in range(len(numeros1)-1):
                    for j in range(len(numeros1)-i-1):
                        if numeros1[j] > numeros1[j+1]:
                            temporal = numeros1[j]
                            numeros1[j] = numeros1[j+1]
                            numeros1[j+1] = temporal
                print(numeros1)
                #orden descendente para otro using burblesort
                for i in range(len(numeros2)-1):
                    for j in range(len(numeros2)-i-1):
                        if numeros2[j] < numeros2[j+1]:
                            temporal = numeros2[j]
                            numeros2[j] = numeros2[j+1]
                            numeros2[j+1] = temporal
                print(numeros2)
                #Tercer vector de Pares con orden descendente
                print('ARRAY DE PARES CON ORDEN DESCENDENTE')
                vector = []
                for i in numeros1:
                    if i % 2 == 0:
                        vector.append(i)
                for i in numeros2:
                    if i % 2 == 0:
                        vector.append(i)
                #Ordenar vector usando QuickSort
                def particionado(vector):
                    pivote = vector[0]
                    menores = []
                    mayores = []
                    for i in range(1, len(vector)):
                        if vector[i] < pivote:
                            menores.append(vector[i])
                        else:
                            mayores.append(vector[i])
                    return menores, pivote, mayores
                def quicksort_descendente(vector):
                    if len(vector) < 2:
                        return vector
                    menores, pivote, mayores = particionado(vector)
                    return quicksort_descendente(mayores) + [pivote] + quicksort_descendente(menores)
                resultado = quicksort_descendente(vector)
                print(resultado)
                #Ordenar array using QuickSort
                print('ARRAY DE PARES CON ORDEN ASCENDENTE')
                def quicksort_ascendente(vector):
                    if len(vector) < 2:
                        return vector
                    menores, pivote, mayores = particionado(vector)
                    return quicksort_ascendente(menores) + [pivote] + quicksort_ascendente(mayores)
                resultado = quicksort_ascendente(vector)
                print(resultado)
            taller_2_punto_15()
        if respuesta_taller_2 == 16:
            #16.	Se tienen un vector con datos numéricos donde hay varios números Fibonacci
            #formar un tercer vector con los números primos que están entre el Fibonacci mayor y el Fibonacci menor.
            def taller_2_punto_16():
                import random
                numeros = [29, 5, 4, 7, 8, 21, 17, 19, 20, 23, 11, 13, 34, 39, 37]
                primos_entre = []
                mayor = 0
                menor = 0
                contador_fibonaccis = 0
                for i in numeros:
                    num1 = 0
                    num2 = 1
                    secuencia = 0
                    while secuencia <= i:
                        secuencia = num1 + num2
                        num1 = num2
                        num2 = secuencia
                        if secuencia == i:
                            contador_fibonaccis += 1
                            if contador_fibonaccis == 1:
                                mayor = i
                                menor = i
                            else:
                                if i < menor:
                                    menor = i
                                if i > mayor:
                                    mayor = i
                for i in range(menor+1, mayor):
                    if i in numeros:
                        condicion = 1
                        divisores = 0
                        while condicion <= i:
                            if i % condicion == 0:
                                divisores += 1
                            condicion += 1
                        if divisores == 2:
                            primos_entre.append(i)
                print("primos entre el fibonacci menor:", menor, "y el fibonacci mayor:", mayor)
                print(primos_entre)
            taller_2_punto_16()
        if respuesta_taller_2 == 17:
            #17.	Se tienen un vector con datos numéricos donde hay varios números Fibonacci
            #hallar el promedio de los múltiplos de tres, que están entre el segundo y tercer Fibonacci del vector.
            def taller_2_punto_17():
                numeros = [4, 3, 5, 13, 9, 6, 12, 21]
                contador = 0
                for i in numeros:
                    num1 = 0
                    num2 = 1
                    secuencia = 0
                    while secuencia <= i:
                        secuencia = num1 + num2
                        num1 = num2
                        num2 = secuencia
                        if secuencia == i:
                            contador += 1
                            if contador == 2:
                                segundo_fibonacci = i
                            if contador == 3:
                                tercer_fibonacci = i
                suma = 0
                contador = 0
                for i in numeros:
                    for i in range(segundo_fibonacci+1, tercer_fibonacci):
                        if i % 3 == 0:
                            suma += i
                            contador += 1
                promedio = suma/contador
                print(promedio)
            taller_2_punto_17()
        if respuesta_taller_2 == 18:
            #18.	Se tiene un vector con datos numéricos donde hay varios Fibonacci,
            #encontrar el segundo y tercer Fibonacci y sus posiciones,
            #reemplazar las posiciones comprendidas en estos dos valores con el factorial del Fibonacci menor de los dos.
            def taller_2_punto_18():
                numeros = [3, 21, 6, 4, 7, 9, 11, 12, 8, 10, 5]
                contador_fibonacci = 0
                segundo_fibonacci, tercer_fibonacci = None, None
                posicion_segundo_fibonacci, posicion_tercer_fibonacci = None, None
                for i in range(len(numeros)):
                    n = numeros[i]
                    num1, num2 = 0, 1
                    secuencia = 0
                    while secuencia <= n:
                        secuencia = num1 + num2
                        num1, num2 = num2, secuencia
                        if secuencia == n:
                            contador_fibonacci += 1
                            if contador_fibonacci == 2:
                                segundo_fibonacci = n
                                posicion_segundo_fibonacci = i+1
                            if contador_fibonacci == 3:
                                tercer_fibonacci = n
                                posicion_tercer_fibonacci = i+1
                print("Segundo fibonacci:", segundo_fibonacci, "posición:", posicion_segundo_fibonacci)
                print("Tercer fibonacci:", tercer_fibonacci, "posición:", posicion_tercer_fibonacci)
                print(numeros)
            taller_2_punto_18()
    if respuesta == 3:
    if respuesta == 4:
menu_inicio()