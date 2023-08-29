def menu_inicio():
    while True:
        respuesta = int(input("""Escoja un menu:
            1. Taller 1
            2. Taller 2
            3. Taller 3                
            4. Evaluación 1
            5. Evaluación 2
            6. Salir
                              :    """))
        if respuesta == 1:
            respuesta_taller_1 = int(input("""Qué Punto desea ver a continuación:  
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
                                        26. Determinar triangulo equilatero, escaleno o isóceles
                                           
                                           :   """))
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
                def taller_1_punto_10():
                    cantidad = int(input("Digite la cantidad de datos: "))
                    sum_factoriales_fibonacci = 0
                    contador_fibonacci = 0

                    def factorial(n):
                        if n == 0 or n == 1:
                            return 1
                        else:
                            return n * factorial(n - 1)

                    a = 0
                    b = 1

                    for i in range(cantidad):
                        num = int(input("Digite un dato: "))
                        
                        p = 0
                        cdivisores = 0
                        while p <= num:
                            if num % p == 0:
                                cdivisores += 1
                            p += 1
                            
                        if cdivisores == 2:
                            while b <= num:
                                if b == num:
                                    contador_fibonacci += 1
                                    sum_factoriales_fibonacci += factorial(num)
                                c = a + b
                                a = b
                                b = c

                    if contador_fibonacci == 0:
                        print("No se encontraron números Fibonacci en los datos ingresados.")
                    else:
                        print(f"La suma de los factoriales de los números Fibonacci es: {sum_factoriales_fibonacci}")

                taller_1_punto_10()
            if respuesta_taller_1 == 11:
                def taller_1_punto_11():
                    cantidad_datos=int(input("digite la cantidad de datos->"))
                    cp=0
                    suma_factorial_primos=0
                    for i in range(cantidad_datos):
                        num=int(input("Digite dato->"))
                        r=2
                        cd=0
                        while r < num:
                            if num % r==0:
                                cd+=1
                            r+=1  
                        if cd==0:
                            primo=num
                            cp+=1
                            z=1
                            for j in range(1, num + 1):
                                z *= j
                            suma_factorial_primos += z
                            
                    promedio=suma_factorial_primos/cp if cp > 0 else 0
                    if cp>0:
                        print("el promedio de los factoriales de los primos es", promedio)
                    else:
                        print("no hay primos")
                taller_1_punto_11()
            if respuesta_taller_1 == 12:
                def taller_1_punto_12():
                    cd = int(input("Digite la cantidad de datos"))
                    sum_factorial_primos = 0
                    sum_factorial_fib = 0
                    cp = 0
                    cf = 0

                    for i in range(cd):
                        num = int(input("digite el dato->"))
                        div = 0
                        con = 1
                        
                        while con <= num:
                            if num % con == 0:
                                div += 1
                            con += 1
                            
                        if div == 2:
                            cp += 1
                            z = 1
                            temp_num = num
                            while temp_num > 0:
                                z *= temp_num
                                temp_num -= 1
                            sum_factorial_primos += z
                        else:
                            a = 0
                            b = 1
                            c = 0
                            while c < num:
                                c = a + b
                                a = b
                                b = c
                            if c == num:
                                cf += 1
                                s = 1
                                temp_num = num
                                while temp_num > 0:
                                    s *= temp_num
                                    temp_num -= 1
                                sum_factorial_fib += s

                    if cp > 0:
                        prom_primos = sum_factorial_primos / cp
                    else:
                        prom_primos = 0
                        print("No hay numeros primos")
                        
                    if cf > 0:
                        prom_fib = sum_factorial_fib / cf
                    else:
                        prom_fib = 0
                        print("No hay numeros fibonaccis")

                    if prom_fib > 0 and prom_primos > 0:
                        if prom_fib > prom_primos:
                            print(f"El promedio de los factoriales de los números Fibonacci es {prom_fib}, siendo mayor que el promedio de los factoriales de los números primos que es {prom_primos}")
                        else:
                            print(f"El promedio de los factoriales de los números primos es {prom_primos}, siendo mayor que el promedio de los factoriales de los números Fibonacci que es {prom_fib}")

                taller_1_punto_12()
            if respuesta_taller_1 == 13:
                def taller_1_punto_13():
                    #Se tiene una cantidad de números dada donde hay varios primos determinar 
                    #las tablas de multiplicar que están entre el primo menor y primo mayor.
                    cantidad=int(input("Digite la cantidad de datos->"))
                    contadorp=0
                    pmayor=0
                    pmenor=0
                    for r in range(cantidad):
                        num=int(input("Digite un dato->"))
                        cdivisores=0
                        i=1
                        while i<=num:
                            if num%i==0:
                                cdivisores+=1
                            i+=1
                        if cdivisores==2:
                            contadorp+=1
                            if contadorp==1:
                                pmenor=num
                                pmayor=num
                            else:
                                if num<pmenor:
                                    pmenor=num
                                elif num>pmayor:
                                    pmayor=num
                            
                    if contadorp<2:
                        print("no hay los suficientes numeros primos")
                    else:
                        for p in range(pmenor, pmayor+1):
                            print(f"Tabla de multiplicar para {p}:")
                            contador_tablas=1 
                            while contador_tablas<10:
                                tabla=p*contador_tablas
                                print(f"{p} x {contador_tablas} = {tabla}")
                                contador_tablas+=1
                taller_1_punto_13()
            if respuesta_taller_1 == 14:
                def taller_1_punto_14():
                    #Se tiene una cantidad de números dada donde hay varios números Fibonacci, obtener los Fibonacci 1, 3, 4 
                    # (de acuerdo al orden de entrada) y mostrar el menor y el mayor de ellos.
                    cantidad=int(input("Digite la canntidad de datos->"))
                    contadorf=0
                    for i in range(cantidad):
                        num=int(input("digite un dato->"))
                        a=0
                        b=1
                        c=0
                        while c<num:
                            c=a+b
                            a=b
                            b=c
                        if c==num:
                            contadorf+=1
                            if contadorf==1:
                                primerf=num
                            if contadorf==3:
                                tercerf=num
                            if contadorf==4:
                                cuartof=num
                    if primerf>tercerf:
                        if primerf>cuartof:
                            print(f"el mayor fibonacci es el primero=={primerf}")
                            if tercerf<cuartof:
                                print(f"el menor fibonacci es el tercero=={tercerf}")

                            else:  
                                print(f"el menor fibonacci es el cuarto=={cuartof}")  
                        else:
                            print(f"el mayor fibonacci es el cuarto=={cuartof}")
                            if tercerf<primerf:
                                print(f"el menor fibonacci es el tercero=={tercerf}")

                            else:  
                                print(f"el menor fibonacci es el primero=={primerf}")
                    else:
                        if tercerf>cuartof:
                            print(f"el mayor fibonacci es el tercero=={tercerf}")
                            if cuartof<primerf:
                                print(f"el menor fibonacci es el cuarto=={cuartof}")

                            else:  
                                print(f"el menor fibonacci es el primero=={primerf}")
                        else: 
                            print(f"el mayor fibonacci es el cuarto=={cuartof}")
                            if tercerf<primerf:
                                print(f"el menor fibonacci es el tercero=={tercerf}")

                            else:  
                                print(f"el menor fibonacci es el primero=={primerf}")
                        
                taller_1_punto_14()
            if respuesta_taller_1 == 15:
                def taller_1_punto_15():
                    #-	Se tiene una cantidad de números dada donde hay varios números Primos, obtener los primos  2, 3, 4  
                    # (de acuerdo al orden de entrada) y mostrarlos en forma ascendente, sin utilizar condiciones compuestas.
                    cantidad = int(input("Digite la cantidad de datos, en la cual deben haber minimo 4 primos y por ende la cantidad de numeros debe ser mayor a 4 -> "))
                    contadorp = 0
                    segundop = 0
                    tercerp = 0
                    cuartop = 0

                    for i in range(cantidad):
                        num = int(input("Digite un dato -> "))
                        a = 1
                        divisores = 0
                        
                        while a <= num:
                            if num % a == 0:
                                divisores += 1
                            a += 1
                        
                        if divisores == 2:
                            contadorp += 1
                            
                            if contadorp == 2:
                                segundop = num
                            elif contadorp == 3:
                                tercerp = num
                            elif contadorp == 4:
                                cuartop = num

                    if segundop > tercerp:
                        if segundop > cuartop:
                            print(f"El mayor primo es el segundo -> {segundop}")
                            
                            if tercerp < cuartop:
                                print(f"El primo del medio es el cuarto -> {cuartop}")
                                print(f"El menor primo es el tercero -> {tercerp}")
                            else:
                                print(f"El primo del medio es el tercero -> {tercerp}")
                                print(f"El menor primo es el cuarto -> {cuartop}")
                        else:
                            print(f"El mayor primo es el cuarto -> {cuartop}")
                            
                            if tercerp < segundop:
                                print(f"El primo del medio es el segundo -> {segundop}")
                                print(f"El menor primo es el tercero -> {tercerp}")
                            else:
                                print(f"El primo del medio es el tercero -> {tercerp}")
                                print(f"El menor primo es el segundo -> {segundop}")
                    else:
                        if tercerp > cuartop:
                            print(f"El mayor primo es el tercero -> {tercerp}")
                            
                            if cuartop < segundop:
                                print(f"El primo del medio es el segundo -> {segundop}")
                                print(f"El menor primo es el cuarto -> {cuartop}")
                            else:
                                print(f"El primo del medio es el cuarto -> {cuartop}")
                                print(f"El menor primo es el segundo -> {segundop}")
                        else:
                            print(f"El mayor primo es el cuarto -> {cuartop}")
                            
                            if tercerp < segundop:
                                print(f"El primo del medio es el segundo -> {segundop}")
                                print(f"El menor primo es el tercero -> {tercerp}")
                            else:
                                print(f"El primo del medio es el tercero -> {tercerp}")
                                print(f"El menor primo es el segundo -> {segundop}")
                taller_1_punto_15()
            if respuesta_taller_1 == 16:
                def taller_1_punto_16():
                    # Se tiene una cantidad de números dada donde hay varios primos determinar 
                    # si el primo 2 y el primo 3 de acuerdo al orden de entrada si son consecutivos.
                    # Son consecutivos si entre los dos no hay otro número primo
                    cantidad=int(input("Digite la cantidad de datos, debe contener al menos 3 primos"))
                    primo2=primo3=0
                    cantidad_primos=0
                    consecutivo=True
                    contador=1
                    while contador<=cantidad:
                        num=int(input(f"digite el dato{contador}->"))
                        divisores=0
                        z=1
                        while z<num:
                            if num%z==0:
                                divisores+=1
                            z+=1
                        if divisores==2:
                            cantidad_primos+=1
                            if cantidad_primos==2:
                                primo2=num
                            elif cantidad_primos==3:
                                primo3=num
                        contador+=1
                    print("segundo primo", primo2)
                    print("tercer primo", primo3)
                taller_1_punto_16()
            if respuesta_taller_1 == 17:
                def taller_1_punto_17():
                    cantidad = int(input("Digite la cantidad de números: "))
                    datos = []

                    for i in range(cantidad):
                        num = int(input("Digite un número: "))
                        datos.append(num)

                    num_buscado = int(input("Digite el número a buscar: "))
                    ubicacion = -1

                    for i, num in enumerate(datos):
                        if num == num_buscado:
                            ubicacion = i
                            break

                    if ubicacion != -1:
                        print(f"El número {num_buscado} se encuentra en la ubicación {ubicacion}.")
                    else:
                        print(f"El número {num_buscado} no se encuentra en la lista.")
                taller_1_punto_17()
            if respuesta_taller_1 == 18:
                def taller_1_punto_18():
                    cantidad = int(input("Digite la cantidad de números: "))
                    pmayor = 0
                    p_encontrado = False
                    f_menor = float('inf')

                    for i in range(cantidad):
                        numero = int(input("Digite un número: "))
                        
                        cdivisores = 0
                        for divisor in range(1, numero + 1):
                            if numero % divisor == 0:
                                cdivisores += 1
                                
                        if cdivisores == 2:  # Es un número primo
                            if not p_encontrado or numero > pmayor:
                                pmayor = numero
                                p_encontrado = True
                            
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= numero:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 = secuencia
                            if secuencia == numero:
                                f_menor = min(f_menor, numero)

                    if p_encontrado and f_menor != float('inf'):
                        multiplicacion = pmayor * f_menor
                        print(f"La multiplicación del primo mayor ({pmayor}) por el Fibonacci menor ({f_menor}) es: {multiplicacion}")
                    else:
                        print("No se encontró el primo mayor o el Fibonacci menor.")

                taller_1_punto_18()
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
                def taller_1_punto_21():
                    #Hallar el factorial de un número con sumas

                    num = int(input("Ingrese un número: "))
                    factorial = 1
                    contador = 1
                    suma = 0

                    while contador <= num:
                        temp = factorial
                        suma = 0
                        while temp > 0:
                            suma += contador
                            temp -= 1
                        factorial = suma
                        contador += 1

                    print("El factorial de", num, "es:", factorial)
                taller_1_punto_21()
            if respuesta_taller_1 == 22:
                def taller_1_punto_22():
                    cantidad = int(input("Digite la cantidad de números: "))
                    contador_pares = 0
                    suma_pares = 0
                    pmayor = 0
                    p_encontrado = False
                    f_menor = float('inf')

                    for i in range(cantidad):
                        numero = int(input("Digite un número: "))
                        
                        cdivisores = 0
                        for divisor in range(1, numero + 1):
                            if numero % divisor == 0:
                                cdivisores += 1
                                
                        if cdivisores == 2:  # Es un número primo
                            if not p_encontrado or numero > pmayor:
                                pmayor = numero
                                p_encontrado = True
                            
                        a = 0
                        b = 1
                        while b <= numero:
                            if b == numero:
                                f_menor = min(f_menor, numero)
                            c = a + b
                            a = b
                            b = c

                    for num in range(pmayor + 1, f_menor):
                        if num % 2 == 0:  # Verifica si el número es par
                            contador_pares += 1
                            suma_pares += num

                    if contador_pares > 0:
                        promedio_pares = suma_pares / contador_pares
                        print(f"El promedio de los números pares entre el primo mayor ({pmayor}) y el Fibonacci menor ({f_menor}) es: {promedio_pares}")
                    else:
                        print("No hay números pares entre el primo mayor y el Fibonacci menor.")
                taller_1_punto_22()
            if respuesta_taller_1 == 23:
                def taller_1_punto_23():
                    cantidad = int(input("Digite la cantidad de números: "))
                    contador_impares = 0
                    suma_factoriales_impares = 0
                    pmayor = 0
                    p_encontrado = False
                    f_menor = float('inf')

                    def factorial(n):
                        if n == 0 or n == 1:
                            return 1
                        else:
                            resultado = 1
                            for i in range(2, n + 1):
                                resultado *= i
                            return resultado

                    for i in range(cantidad):
                        numero = int(input("Digite un número: "))
                        es_fibonacci = False
                        
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= numero:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 = secuencia
                            if secuencia == numero:
                                es_fibonacci = True
                        
                        if es_fibonacci:
                            if not p_encontrado or numero > pmayor:
                                pmayor = numero
                                p_encontrado = True
                            
                        es_primo = True
                        if numero > 1:
                            for divisor in range(2, numero):
                                if numero % divisor == 0:
                                    es_primo = False
                                    break

                        if es_fibonacci or es_primo:
                            f_menor = min(f_menor, numero)

                    for num in range(pmayor + 1, f_menor):
                        if num % 2 != 0:  # Verifica si el número es impar
                            contador_impares += 1
                            suma_factoriales_impares += factorial(num)

                    if contador_impares > 0:
                        promedio_impares = suma_factoriales_impares / contador_impares
                        print(f"El promedio de los factoriales de los números impares entre el primo mayor ({pmayor}) y el Fibonacci menor ({f_menor}) es: {promedio_impares}")
                    else:
                        print("No hay números impares entre el primo mayor y el Fibonacci menor.")
                taller_1_punto_23()
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
                def taller_1_punto_25():  
                    segundo_primo = None
                    contador_segundo_primo = 0
                    contador_primos = 0

                    while True:
                        num = input("Ingresa un número, 'c' para terminar")
                        if num.lower() == "c":
                            break
                        else:
                            num = int(num)
                            divisores = 0
                            condicion = 1
                            while condicion <= num:
                                if num % condicion == 0:
                                    divisores += 1
                                condicion += 1
                            if divisores == 2:
                                contador_primos += 1
                                if contador_primos == 2:
                                    segundo_primo = num
                                elif num == segundo_primo:
                                    contador_segundo_primo += 1
                    print(f"El segundo primo ({segundo_primo}) se repitió {contador_segundo_primo} veces más.")
                taller_1_punto_25()
            if respuesta_taller_1 == 26:
                def taller_1_punto_26():
                    lado1 = int(input("Ingrese el lado 1 del triángulo: "))
                    lado2 = int(input("Ingrese el lado 2 del triángulo: "))
                    lado3 = int(input("Ingrese el lado 3 del triángulo: "))

                    if lado1 == lado2 == lado3:
                        print("El triángulo es equilátero.")
                    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
                        print("El triángulo es escaleno.")
                    else:
                        print("El triángulo es isósceles.")
                taller_1_punto_26()
        if respuesta == 2:
            respuesta_taller_2 = int(input("""Qué Punto desea ver a continuación:  
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
                                        18. Segundo, tecer fibonacci y sus posiciones, remplazarlas
                                           
                                           :   """))
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
            respuesta_taller_3 = int(input("""Escoja el punto que desea ver acontinuación: 
                                        
                                            1.	Se tiene una matriz con datos numéricos repetidos, determinar los datos que más se repiten.

                                            2.	Se tiene una matriz con datos numéricos determinar el mayor, menor y promedio de cada columna.

                                            3.	Se tiene una matriz con datos numéricos, intercambiar las filas donde se encuentre el mayor y el menor de la matriz.

                                            4.	Se tiene una matriz con datos numéricos, intercambiar las columnas donde se encuentra el primo mayor y el primo menor.

                                            5.	Se tienen dos matrices con datos numéricos, formar un vector con los Fibonacci comunes de las dos matrices sin repetidos.

                                            6.	Se tienen dos matrices con datos numéricos, formar un vector con los primos que están en los dos matrices sin repetidos.

                                            7.	Se tiene una matriz cuadrada con datos numéricos, formar un vector con los primos que se encuentran en la diagonal principal y la diagonal secundaria.

                                            8.	Se tiene una matriz cuadrada con datos numéricos, Comparar el promedio de los números pares que están sobre la diagonal principal,
                                                con el promedio de los impares de los datos que están bajo la diagonal principal.

                                            9.	Se tiene una matriz con datos numéricos, donde hay varios primos, determinar si el segundo primo encontrado al recorrer la matriz
                                                por columnas es consecutivo con el cuarto primo encontrado.

                                            10.	Ordenar las columnas pares ascendentemente y las columnas impares descendentemente

                                            11.	Se tienen dos matrices ordenadas ascendentemente, obtener un vector ordenado ascendentemente con la mezcla de los dos anteriores. (ordenamiento por mezcla).

                                            12.	Intercambiar las filas de una matriz de acuerdo al orden ascendente de los promedios de cada fila

                                            13.	Se tiene una matriz cuadrada de orden N realizar lo siguiente
                                            -	Hallar el promedio de la diagonal principal y el promedio de la diagonal secundaria
                                            -	Ordenar ascendentemente la diagonal principal
                                            -	Hallar el promedio de los pares que están encima de la diagonal principal y de los impares de la diagonal secundaria
                                            -	Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con el Fi0bonacci mayor.
                                            -	Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.

                                            14.	Se tienen dos matrices con datos numéricos y se solicita;
                                            -	Formar un vector con los elementos comunes de las dos matrices sin repetidos
                                            -	Formar un vector con los primos comunes de las dos matrices sin repetidos
                                            -	Formar un vector con los primos no comunes de las dos matrices sin repetidos

                                            15.	Se tiene una matriz con datos numéricos repetidos, formar un vector con aquellos contadores de datos que se repiten y que sean números Fibonacci, sin repetidos

                                            16.	Se tiene una matriz con datos numéricos y se solicita
                                            -	Intercambia la primera columna con la última
                                            -	Obtener el mayor, menor y promedio de cada columna
                                            -	Ordenar las filas pares ascendentemente y las filas impares descendentemente
                                            -	Ordenar la matriz descendentemente
                                            -	Intercambiar las filas de una matriz de acuerdo al orden ascendente de los promedios de cada fila
                                            -	Intercambiar las filas donde se encuentre el mayor y el menor de la matriz
                                            -	Intercambiar la fila donde se encuentre el Fibonacci 2 con la fila donde se encuentra el  Fibonacci 4.
                                            -	Intercambiar las filas donde se encuentre el primo mayor y el Fibonacci menor
                                            -	Determinar si el primo 2 y el primo 4 según el recorrido por filas de la matriz, son consecutivos, es decir, no hay un número primo entre los dos 


                                            17.	Se tiene una matriz cuadrada de orden N realizar lo siguiente
                                            -	Hallar el promedio de la diagonal principal y el promedio de la diagonal secundaria
                                            -	Ordenar ascendentemente la diagonal principal
                                            -	Hallar el promedio de los pares que están encima de la diagonal principal y de los impares de la diagonal secundaria
                                            -	Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con el Fibonacci mayor.
                                            -	Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.

                                            18.	Se tienen dos matrices con datos numéricos y se solicita;
                                            -	Formar un vector con los elementos comunes de las dos matrices sin repetidos
                                            -	Formar un vector con los primos comunes de las dos matrices sin repetidos
                                            -	Formar un vector con los primos no comunes de las dos matrices sin repetidos

                                            19.	Se tiene una matriz con datos numéricos repetidos, formar un vector con aquellos contadores de datos que se repiten y que sean números Fibonacci, sin repetidos
                                                
                                                    :   """))      
            if respuesta_taller_3 == 1:
                def taller_3_punto_1():
                    import random

                    matriz1 = []

                    filas = random.randint(2,8)
                    columnas = random.randint(2,8)

                    for fila in range(filas):
                        fila_actual = []
                        for elemento in range(columnas):
                            numero_random = random.randint(1,10)
                            fila_actual.append(numero_random)
                        matriz1.append(fila_actual)
                    print("")
                    for fila in matriz1:
                        print(fila)

                    def contar_repeticiones(matriz):
                        repeticiones = {}
                        for fila in range(filas):
                            for elemento in matriz[fila]:
                                if elemento in repeticiones:
                                    repeticiones[elemento] += 1
                                else:
                                    repeticiones[elemento] = 1
                        return repeticiones

                    matriz = contar_repeticiones(matriz1)

                    max_repeticiones = 0
                    numero_mas_repeticiones = None

                    min_repeticiones = float("inf")
                    numero_menos_repeticiones = None

                    for numero, repeticiones in matriz.items():
                        if repeticiones > max_repeticiones:
                            max_repeticiones = repeticiones
                            numero_mas_repeticiones = numero
                        if repeticiones < min_repeticiones:
                            min_repeticiones = repeticiones
                            numero_menos_repeticiones = numero
                        print(f"Numero: {numero}    Repeticiones: {repeticiones}" )

                    print(f"\nEl numero que mas se repite es: {numero_mas_repeticiones} con {max_repeticiones} repeticones")
                    print(f"\nEl numero que menos se repite es: {numero_menos_repeticiones} con {min_repeticiones} repeticiones")

                taller_3_punto_1()
            if respuesta_taller_3 == 2:
                def taller_3_punto_2():
                    import random

                    filas = random.randint(3, 8)
                    columnas = random.randint(3, 8)
                    matriz = []

                    for fila in range(filas):
                        fila_actual = []
                        for elemento in range(columnas):
                            numero_random = random.randint(1, 20)
                            fila_actual.append(numero_random)
                        matriz.append(fila_actual)

                    for fila in matriz:
                        print(fila)

                    numero_mayor = 0
                    numero_menor = float("inf")

                    #Para recorrer la matriz
                    for fila in matriz:
                        for numero in fila:
                            if numero > numero_mayor:
                                numero_mayor = numero
                            if numero < numero_menor:
                                numero_menor = numero

                    print(f"Numero menor de toda la matriz: {numero_menor}")
                    print(f"Numero mayor de toda la matriz: {numero_mayor}")

                    #Para recorrer columnas
                    for i in range(columnas):
                        numero_mayor_columna = 0
                        numero_menor_columna = float("inf")
                        suma = 0
                        contador = 0
                        for j in range(filas):
                            numero = matriz[j][i]
                            suma += numero
                            contador += 1
                            if numero > numero_mayor_columna:
                                numero_mayor_columna = numero
                            if numero < numero_menor_columna:
                                numero_menor_columna = numero
                        promedio = suma/contador
                        print(f"Promedio: {promedio:.2f}")
                        print(f"El número menor de la columna {i+1} es el número: {numero_menor_columna}")
                        print(f"El número mayor de la columna {i+1} es el número: {numero_mayor_columna}")
                taller_3_punto_2()
            if respuesta_taller_3 == 3:
                def taller_3_punto_3():
                    import random

                    filas = random.randint(2,8)
                    columnas = random.randint(2,8)
                    matriz = []

                    for i in range(filas):
                        fila_actual = []
                        for j in range(columnas):
                            numero_random = random.randint(1,50)
                            fila_actual.append(numero_random)
                        matriz.append(fila_actual)

                    for fila in matriz:
                        print(fila)

                    mayor = 0
                    menor = float("inf")

                    for i, fila in enumerate(matriz):
                        for numero in fila:
                            if numero > mayor:
                                mayor = numero
                                posicion_mayor = i
                            if numero < menor:
                                menor = numero
                                posicion_menor = i

                    print(f"Menor: {menor}  fila: {posicion_menor+1}")
                    print(f"Mayor: {mayor}  fila: {posicion_mayor+1}")

                    #cambiar filas
                    matriz[posicion_mayor], matriz[posicion_menor] = matriz[posicion_menor], matriz[posicion_mayor]
                    for fila in matriz:
                        print(fila)

                taller_3_punto_3()
            if respuesta_taller_3 == 4:
                def taller_3_punto_4():
                    import random

                    filas = random.randint(3,10)
                    columnas = random.randint(3,10)
                    matriz = []

                    for i in range(filas):
                        fila_actual = []
                        for j in range(columnas):
                            numero_random = random.randint(1,50)
                            fila_actual.append(numero_random)
                        matriz.append(fila_actual)

                    for fila in matriz:
                        print(fila)

                    primo_menor = float("inf")
                    primo_mayor = 0

                    for i in range(columnas):
                        for j in range(filas):
                            numero = matriz[j][i]
                            condicion = 1
                            divisores = 0
                            es_primo = False
                            while condicion <= numero:
                                if numero % condicion == 0:
                                    divisores += 1
                                condicion += 1
                            if divisores == 2:
                                es_primo = True
                                if es_primo:
                                    if numero > primo_mayor:
                                        primo_mayor = numero
                                        posicion_primo_mayor = i
                                    if numero < primo_menor:
                                        primo_menor = numero
                                        posicion_primo_menor = i

                    print(f"Primo mayor: {primo_mayor}   posicion columna: {posicion_primo_mayor+1}")
                    print(f"Primo menor: {primo_menor}   posicion columna: {posicion_primo_menor+1}")

                    # Intercambiar columnas
                    for columna in matriz:
                        columna[posicion_primo_mayor], columna[posicion_primo_menor] = columna[posicion_primo_menor], columna[posicion_primo_mayor]

                    print("Matriz después del intercambio:")
                    for fila in matriz:
                        print(fila)

                taller_3_punto_4()
            if respuesta_taller_3 == 5:
                def taller_3_punto_5():
                    import random

                    matriz1 = []
                    matriz2 = []
                    fila = random.randint(3,10)
                    columna = random.randint(3,10)

                    for i in range(fila):
                        fila_actual = []
                        for j in range(columna):
                            fila_actual.append(random.randint(1,50))
                        matriz1.append(fila_actual)

                    for i in range(fila):
                        fila_actual = []
                        for j in range(columna):
                            fila_actual.append(random.randint(1,50))
                        matriz2.append(fila_actual)

                    def imprimir_matriz(matriz):
                        for fila in matriz:
                            print(" ".join("{:3}".format(num) for num in fila))

                    print("Matriz 1:")
                    imprimir_matriz(matriz1)

                    print("\nMatriz 2:")
                    imprimir_matriz(matriz2)

                    #Formar vector con fibonaccis comunes sin repetidos

                    fibonaccis_comunes_sin_repetidos = []

                    def es_fibonacci(numero):
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= numero:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 = secuencia
                            if secuencia == numero:
                                return True
                        return False

                    for fila in matriz1:
                        for numero in fila:
                            if es_fibonacci(numero):
                                es_comun = False
                                for fila2 in matriz2:
                                    if numero in fila2:
                                        es_comun = True
                                        break
                                if es_comun and numero not in fibonaccis_comunes_sin_repetidos:
                                    fibonaccis_comunes_sin_repetidos.append(numero)

                    print(f"Fibonaccis comunes en las dos matrices: {fibonaccis_comunes_sin_repetidos}")
                taller_3_punto_5()
            if respuesta_taller_3 == 6:
                def taller_3_punto_6():
                    
                    import random

                    filas = random.randint(2,10)
                    columnas = random.randint(2,10)
                    matriz1 = []
                    matriz2 = []

                    for fila in range(filas):
                        fila_actual = []
                        for columna in range(columnas):
                            fila_actual.append(random.randint(1,50))
                        matriz1.append(fila_actual)

                    for fila in range(filas):
                        fila_actual = []
                        for columna in range(columnas):
                            fila_actual.append(random.randint(1,50))
                        matriz2.append(fila_actual)

                    print("")
                    for fila in matriz1:
                        print(" ".join("{:3}".format(num) for num in fila))

                    print("\n")
                    for fila in matriz2:
                        print(" ".join("{:3}".format(num) for num in fila))

                    def es_primo(numero):
                        divisores = 0
                        condicion = 1
                        while condicion <= numero:
                            if numero % condicion == 0:
                                divisores += 1
                            condicion += 1
                        if divisores == 2:
                            return True
                        return False

                    primos_en_ambas_matrices_sin_repetidos = []
                    primos_comunes_sin_repetidos = []

                    for fila in matriz1:
                        for numero in fila:
                            if es_primo(numero) and numero not in primos_en_ambas_matrices_sin_repetidos:
                                primos_en_ambas_matrices_sin_repetidos.append(numero)

                    for fila in matriz2:
                        for numero in fila:
                            if es_primo(numero) and numero not in primos_en_ambas_matrices_sin_repetidos:
                                primos_en_ambas_matrices_sin_repetidos.append(numero)

                    print(f"Primos encontrados en ambas matrices: {primos_en_ambas_matrices_sin_repetidos}")

                    for fila in matriz1:
                        for numero in fila:
                            if es_primo(numero):
                                es_comun = False
                                for fila2 in matriz2:
                                    if numero in fila2:
                                        es_comun = True
                                        break
                                if es_comun and numero not in primos_comunes_sin_repetidos:
                                    primos_comunes_sin_repetidos.append(numero)

                    print(f"Primos comunes sin repetidos: {primos_comunes_sin_repetidos}")

                taller_3_punto_6()
            if respuesta_taller_3 == 7:
                def taller_3_punto_7():
                    #Se tiene una matriz cuadrada con datos numéricos, formar un vector con los primos que se encuentran en la diagonal principal y la diagonal secundaria
                    import random

                    filas_y_columnas = random.randint(2,10)
                    matriz = []

                    for fila in range(filas_y_columnas):
                        fila_actual = []
                        for columna in range(filas_y_columnas):
                            fila_actual.append(random.randint(1,50))
                        matriz.append(fila_actual)

                    for fila in matriz:
                        print(" ".join("{:3}".format(num) for num in fila))

                    def es_primo(numero):
                        condicion = 1
                        divisores = 0
                        while condicion <= numero:
                            if numero % condicion == 0:
                                divisores += 1
                            condicion += 1
                        if divisores == 2:
                            return True
                        return False

                    #para diagonal primaria, buscar primos
                    primos = []
                    for i in range(filas_y_columnas):
                        if es_primo(matriz[i][i]):
                            primos.append(matriz[i][i])
                        if es_primo(matriz[i][-i - 1]):
                            primos.append(matriz[i][-i - 1])

                    print(f"primos en la diagonal primaria y secundaria: {primos}")
                taller_3_punto_7()
            if respuesta_taller_3 == 8:
                def taller_3_punto_8():
                    import random

                    filas_y_columas = random.randint(2,10)
                    matriz = []

                    for fila in range(filas_y_columas):
                        fila_actual = []
                        for columna in range(filas_y_columas):
                            fila_actual.append(random.randint(1,50))
                        matriz.append(fila_actual)

                    for fila in matriz:
                        print(" ".join("{:3}".format(num) for num in fila))

                    def es_par(numero):
                        if numero % 2 == 0:
                            return True
                        return False

                    def es_impar(numero):
                        if numero % 2 != 0:
                            return True
                        return False

                    #Promedio de pares diagonal principal
                    suma_pares = 0
                    contador_pares = 0
                    promedio_pares = 0
                    for i in range(filas_y_columas):
                        if es_par(matriz[i][i]):
                            suma_pares += matriz[i][i]
                            contador_pares += 1
                    promedio_pares = suma_pares/contador_pares
                    print(f"El promedio de los pares de la diagonal principal es: {suma_pares} / {contador_pares} = {promedio_pares:.2f}")


                    #promedio de impares diagonal bajo diagonal principal
                    suma_impares = 0
                    contador_impares = 0
                    promedio_impares = 0
                    for i in range(filas_y_columas):
                        if i < filas_y_columas - 1: #Aqui es importante no considerar una ultima fila y columna que no existe porque vamos a recorrer los elementos bajo la diagonal principal con i+1
                            if es_impar(matriz[i+1][i]): #si no ponemos la condicion anterior se saldra del rango
                                suma_impares += matriz[i+1][i]
                                contador_impares += 1
                    promedio_impares = suma_impares/contador_impares

                    print(f"El promedio de los impares diagonal bajo diagonal principal es: {suma_impares} / {contador_impares} = {promedio_impares:.2f}")

                    if promedio_pares > promedio_impares:
                        print(f"El promedio de los pares: {promedio_pares} es mayor que el promedio de los impares: {promedio_impares}")
                    elif promedio_impares > promedio_pares:
                        print(f"El promedio de los pares: {promedio_pares} es menor que el promedio de los impares: {promedio_impares}")
                    else:
                        print(f"El promedio de los pares: {promedio_pares} es igual que el promedio de los impares: {promedio_impares}")
                taller_3_punto_8()
            if respuesta_taller_3 == 9:
                def taller_3_punto_9():
                    import random

                    filas = random.randint(5,10)
                    columnas = random.randint(5,10)
                    matriz = []

                    for fila in range(filas):
                        fila_actual = []
                        for columa in range(columnas):
                            fila_actual.append(random.randint(1,50))
                        matriz.append(fila_actual)

                    for fila in matriz:
                        print(" ".join("{:3}".format(num) for num in fila))

                    def es_primo(numero):
                        condicion = 1
                        divisores = 0
                        while condicion <= numero:
                            if numero % condicion == 0:
                                divisores += 1
                            condicion += 1
                        if divisores == 2:
                            return True
                        return False

                    contador_primos = 0
                    for i in range(columnas):
                        for j in range(filas):
                            numero = matriz[j][i]
                            if es_primo(numero):
                                contador_primos += 1
                                if contador_primos == 2:
                                    segundo_primo = numero
                                if contador_primos == 4:
                                    cuarto_primo = numero
                                    break

                    print(f"Segundo primo encontrado: {segundo_primo}")
                    print(f"Cuarto primo encontrado: {cuarto_primo}")
                            
                    #Determinar si es consecutivo

                    es_consecutivo = True
                    if segundo_primo < cuarto_primo:
                        analizador = segundo_primo + 1
                        while analizador < cuarto_primo:
                            divisores = 0
                            condicion = 1
                            while condicion <= analizador: 
                                if analizador % condicion == 0:
                                    divisores += 1
                                condicion += 1
                            if divisores == 2:
                                es_consecutivo = False
                                break
                            analizador += 1
                        if es_consecutivo:
                            print(f"El primo: {cuarto_primo} es consecutivo del {segundo_primo}")
                        else:
                            print(f"El primo: {segundo_primo} y el {cuarto_primo} no son consecutivos")
                    else:
                        print(f"El primo: {segundo_primo} y el {cuarto_primo} no son consecutivos")  
                taller_3_punto_9()
            if respuesta_taller_3 == 10:
                def taller_3_punto_10():
                    #Ordenar las columnas pares ascendentemente y las columnas impares descendentemente

                    import random

                    filas = random.randint(5, 10)
                    columnas = random.randint(5, 10)
                    matriz = []

                    for fila in range(filas):
                        fila_actual = []
                        for columna in range(columnas):
                            fila_actual.append(random.randint(1, 20))
                        matriz.append(fila_actual)

                    print("\nMatriz original")
                    for fila in matriz:
                        print(" ".join("{:4}".format(num) for num in fila))

                    for i in range(columnas):
                        if i % 2 == 0:
                            for j in range(filas - 1):
                                for k in range(j + 1, filas):
                                    if matriz[j][i] > matriz[k][i]:
                                        matriz[j][i], matriz[k][i] = matriz[k][i], matriz[j][i]
                        else:
                            for j in range(filas - 1):
                                for k in range(j + 1, filas):
                                    if matriz[j][i] < matriz[k][i]:
                                        matriz[j][i], matriz[k][i] = matriz[k][i], matriz[j][i]

                    print("\nMatriz ordenada")
                    for fila in matriz:
                        print(" ".join("{:4}".format(num) for num in fila))

                taller_3_punto_10()
            if respuesta_taller_3 == 11:
                def taller_3_punto_11():
                    #Se tienen dos matrices ordenadas ascendentemente, obtener un vector ordenado ascendentemente con la mezcla de los dos anteriores. (ordenamiento por mezcla).

                    import random

                    def mezclar(vector1, vector2):
                        resultado = []
                        i = j = 0

                        while i < len(vector1) and j < len(vector2):
                            if vector1[i] < vector2[j]:
                                resultado.append(vector1[i])
                                i += 1
                            else:
                                resultado.append(vector2[j])
                                j += 1

                        resultado.extend(vector1[i:])
                        resultado.extend(vector2[j:])
                        return resultado

                    def ordenar_mezcla(vector):
                        if len(vector) <= 1:
                            return vector

                        medio = len(vector) // 2
                        izquierda = vector[:medio]
                        derecha = vector[medio:]

                        izquierda = ordenar_mezcla(izquierda)
                        derecha = ordenar_mezcla(derecha)

                        return mezclar(izquierda, derecha)

                    matriz1 = []
                    matriz2 = []
                    dimensiones = random.randint(3, 6)

                    for i in range(dimensiones):
                        fila_actual = []
                        for j in range(dimensiones):
                            fila_actual.append(random.randint(1, 50))
                        matriz1.append(fila_actual)

                    for i in range(dimensiones):
                        fila_actual = []
                        for j in range(dimensiones):
                            fila_actual.append(random.randint(1, 50))
                        matriz2.append(fila_actual)

                    def mostrar_matriz(matriz):
                        for fila in matriz:
                            print(" ".join("{:4}".format(n) for n in fila))

                    print("\nMatriz 1")
                    mostrar_matriz(matriz1)

                    print("\nMatriz 2")
                    mostrar_matriz(matriz2)

                    # Convertir matrices en listas planas para ordenarlas
                    vector1 = [numero for fila in matriz1 for numero in fila]
                    vector2 = [numero for fila in matriz2 for numero in fila]

                    vector1_ordenado = ordenar_mezcla(vector1)
                    vector2_ordenado = ordenar_mezcla(vector2)

                    print("\nVector 1 ordenado:")
                    print(vector1_ordenado)

                    print("\nVector 2 ordenado:")
                    print(vector2_ordenado)

                    # Combinar y ordenar los dos vectores utilizando el método de mezcla
                    resultado_combinado = mezclar(vector1_ordenado, vector2_ordenado)
                    print("\nResultado combinado y ordenado:")
                    print(resultado_combinado)

                taller_3_punto_11()
            if respuesta_taller_3 == 12:
                def taller_3_punto_12():
                    #12.	Intercambiar las filas de una matriz de acuerdo al orden ascendente de los promedios de cada fila
                    import random

                    filas = random.randint(5,10)
                    columnas = random.randint(5,10)
                    matriz = []

                    for fila in range(filas):
                        fila_actual = []
                        for columna in range(columnas):
                            fila_actual.append(random.randint(1,50))
                        matriz.append(fila_actual)

                    promedios = []
                    for i in range(filas):
                        suma = 0
                        promedio = 0
                        contador = 0
                        for j in range(columnas):
                            suma += matriz[i][j]
                            contador += 1
                        promedio = suma/contador
                        promedios.append(promedio)

                    print("\nMatriz con promedios desordenada")
                    for i, fila in enumerate(matriz):
                        print(" ".join("{:4}".format(num) for num in fila),f" Promedio fila: {promedios[i]:.2f}")

                    #Matriz ordenada respecto a los promedios

                    for i in range(len(promedios)):
                        for j in range(len(promedios)-i-1):
                            if promedios[j] > promedios[j+1]:
                                promedios[j], promedios[j+1] = promedios[j+1], promedios[j]
                                matriz[j], matriz[j+1] = matriz[j+1], matriz[j]

                    print("\nMatriz ordenada por promedios")
                    for i, fila in enumerate(matriz):
                        print(" ".join("{:4}".format(num) for num in fila),f" Promedio fila: {promedios[i]:.2f}")
                taller_3_punto_12()
            if respuesta_taller_3 == 13:
                def taller_3_punto_13():
                    #	Se tiene una matriz cuadrada de orden N realizar lo siguiente
                    #    -	Hallar el promedio de la diagonal principal y el promedio de la diagonal secundaria
                    #    -	Ordenar ascendentemente la diagonal principal
                    #    -	Hallar el promedio de los pares que están encima de la diagonal principal y de los impares de la diagonal secundaria
                    #    -	Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con el Fibonacci mayor.
                    #    -	Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.

                    import random

                    dimensiones = random.randint(5,10)
                    matriz = []
                    matriz2 = matriz

                    for fila in range(dimensiones):
                        fila_actual = []
                        for columna in range(dimensiones):
                            fila_actual.append(random.randint(1,50))
                        matriz.append(fila_actual)

                    print("\nMatriz original")
                    for fila in matriz:
                        print(" ".join("{:4}".format(num) for num in fila))

                    #promedio diagonal principal y secundaria

                    promedio_diagonal_primaria = 0
                    promedio_diagonal_secundaria = 0
                    suma_diagonal_primaria = 0
                    suma_diagonal_secundaria = 0
                    contador = 0
                    for i in range(dimensiones):
                        suma_diagonal_primaria += matriz[i][i]
                        suma_diagonal_secundaria += matriz[i][-i-1]
                        contador += 1

                    promedio_diagonal_primaria = suma_diagonal_primaria/contador
                    promedio_diagonal_secundaria = suma_diagonal_secundaria/contador


                    print(f"\nPromedio diagonal 1: {promedio_diagonal_primaria:.2f}")
                    print(f"Promedio diagonal 2: {promedio_diagonal_secundaria:.2f}")

                    #ordenar ascendentemente la diagonal principal

                    for i in range(dimensiones - 1):
                        for j in range(i + 1, dimensiones):
                            if matriz[i][i] > matriz[j][j]:
                                matriz[i][i], matriz[j][j] = matriz[j][j], matriz[i][i]

                    print("\nCon diagonal primaria ordenada")
                    for fila in matriz:
                        print(" ".join("{:4}".format(num) for num in fila))

                    #Promedio pares e impares diagonales

                    def es_par(numero):
                        if numero % 2 == 0:
                            return True
                        return False

                    def es_impar(numero):
                        if numero % 2 != 0:
                            return True
                        return False

                    promedio_pares_up_diagonal_primaria = 0
                    promedio_impares_diagonal_secundaria = 0
                    contador_pares = 0
                    contador_impares = 0
                    suma_pares_up_diagonal_primaria = 0
                    suma_impares_diagonal_secundaria = 0

                    for i in range(dimensiones):
                        if i < dimensiones - 1:
                            if es_par(matriz[i][i+1]):
                                suma_pares_up_diagonal_primaria += matriz[i][i+1]
                                contador_pares += 1
                    if suma_pares_up_diagonal_primaria == 0 and contador_pares == 0:
                        promedio_pares_up_diagonal_primaria = 0
                    else:
                        promedio_pares_up_diagonal_primaria = suma_pares_up_diagonal_primaria/contador_pares
                    print(f"\nEl promedio de los pares de up diagonal principal: {promedio_pares_up_diagonal_primaria:.2f}")

                    for i in range(dimensiones):
                        if es_impar(matriz[i][-i-1]):
                            suma_impares_diagonal_secundaria += matriz[i][-i-1]
                            contador_impares += 1
                    if suma_impares_diagonal_secundaria == 0 and contador_impares == 0:
                        promedio_impares_diagonal_secundaria = 0
                    else:
                        promedio_impares_diagonal_secundaria = suma_impares_diagonal_secundaria/contador_impares
                    print(f"El promedio de impares de la diagonal secundaria: {promedio_impares_diagonal_secundaria:.2f}")

                    #LLenar diagonal primaria con primo menor y secundaria con fibonacci mayor

                    def es_primo(numero):
                        condicion = 1
                        divisores = 0
                        while condicion <= numero:
                            if numero % condicion == 0:
                                divisores += 1
                            condicion += 1
                        if divisores == 2:
                            return True
                        return False

                    def es_fibonacci(numero):
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= numero:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 =secuencia
                            if secuencia == numero:
                                return True
                        return False

                    fibonacci_mayor = 0
                    contador_fibonaccis = 0
                    contador_primos = 0
                    primo_menor = float("inf")

                    for fila in matriz:
                        for numero in fila:
                            if es_fibonacci(numero):
                                contador_fibonaccis = 1
                                if contador_fibonaccis == 1:
                                    fibonacci_mayor = numero
                                else:
                                    if numero > fibonacci_mayor:
                                        fibonacci_mayor = numero
                            if es_primo(numero):
                                contador_primos += 1
                                if contador_primos == 1:
                                    primo_menor = numero
                                else:
                                    if numero < primo_menor:
                                        primo_menor = numero

                    print(f"\nEl fibonacci mayor de la matriz es: {fibonacci_mayor}")
                    print(f"El primo menor de la matriz es: {primo_menor}")

                    #Sustituir la diagonal primaria y secundaria por el primo menor y fibonacci mayor

                    for i in range(dimensiones):
                        matriz[i][i] = primo_menor
                        matriz[i][-i-1] = fibonacci_mayor

                    print("\nCon la diagonal primaria y secundaria sustituida")
                    for fila in matriz:
                        print(" ".join("{:4}".format(num) for num in fila))

                    #Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.

                    impar_menor = float("inf")
                    par_mayor = 0

                    for fila in matriz2:
                        for numero in fila:
                            if es_impar(numero):
                                if numero < impar_menor:
                                    impar_menor = numero
                            if es_par(numero):
                                if numero > par_mayor:
                                    par_mayor = numero

                    print(f"\nPar mayor: {par_mayor} Impar menor: {impar_menor}")

                    for fila in range(dimensiones):
                        for numero in range(dimensiones):
                            matriz[numero][fila] = impar_menor

                    for i in range(dimensiones):
                        for j in range(dimensiones):
                            if i == 0:
                                matriz[i][j] = par_mayor
                                matriz[j][i] = par_mayor
                            if i == dimensiones - 1:
                                matriz[i][j] = par_mayor
                                matriz[j][i] = par_mayor

                    #for fila in range(dimensiones):
                    #   for numero in range(dimensiones):
                    #        if fila == 0 or fila == dimensiones - 1 or numero == 0 or numero == dimensiones - 1:
                    #            matriz[fila][numero] = par_mayor
                    #        else:
                    #            matriz[fila][numero] = impar_menor

                    print("\nContorno e interno con par e impar")
                    for fila in matriz:
                        print(" ".join("{:4}".format(num) for num in fila))
                taller_3_punto_13()
            if respuesta_taller_3 == 14:
                def taller_3_punto_14():
                    #14.	Se tienen dos matrices con datos numéricos y se solicita;
                    #   -	Formar un vector con los elementos comunes de las dos matrices sin repetidos
                    #   -	Formar un vector con los primos comunes de las dos matrices sin repetidos
                    #   -	Formar un vector con los primos no comunes de las dos matrices sin repetidos

                    import random

                    matriz1 = []
                    matriz2 = []

                    for i in range(random.randint(3,5)):
                        fila_actual = []
                        for j in range(random.randint(3,5)):
                            fila_actual.append(random.randint(1,50))
                        matriz1.append(fila_actual)

                    for i in range(random.randint(3,5)):
                        fila_actual = []
                        for j in range(random.randint(3,5)):
                            fila_actual.append(random.randint(1,50))
                        matriz2.append(fila_actual)

                    print("\nMatriz 1")
                    for i in matriz1:
                        print(" ".join("{:4}".format(num) for num in i))

                    print("\nMatriz 2")
                    for i in matriz2:
                        print(" ".join("{:4}".format(num) for num in i))

                    primos_comunes = []
                    numeros_comunes = []
                    primos_no_comunes = []

                    def es_primo(numero):
                        condicion = 1
                        divisores = 0
                        while condicion <= numero:
                            if numero % condicion == 0:
                                divisores += 1
                            condicion += 1
                        if divisores == 2:
                            return True
                        return False

                    #    -	Formar un vector con los elementos comunes de las dos matrices sin repetidos y primos comunes

                    for fila in matriz1:
                        for i in fila:
                            for fila2 in matriz2:
                                if i in fila2 and i not in numeros_comunes:
                                    numeros_comunes.append(i)
                            if es_primo(i):     
                                for fila2 in matriz2:
                                    if i in fila2 and i not in primos_comunes:
                                        primos_comunes.append(i)

                    # Formar un vector con los primos no comunes de las dos matrices sin repetidos

                    for fila in matriz1:
                        for i in fila:
                            if es_primo(i):
                                primo_no_comun = True
                                for fila2 in matriz2:
                                    if i in fila2:
                                        primo_no_comun = False
                                        break
                                if primo_no_comun and i not in primos_no_comunes:
                                    primos_no_comunes.append(i)

                    for fila2 in matriz2:
                        for j in fila2:
                            if es_primo(j):
                                primo_no_comun = True
                                for fila in matriz1:
                                    if j in fila:
                                        primo_no_comun = False
                                        break
                                if primo_no_comun and j not in primos_no_comunes:
                                    primos_no_comunes.append(j)

                    print(f"\nNúmeros comunes en las dos matrices: {numeros_comunes}")
                    print(f"Primos comunes en las dos matricez: {primos_comunes}")
                    print(f"Primos no comunes en ambas matrices: {primos_no_comunes}")

                taller_3_punto_14()
            if respuesta_taller_3 == 15:
                def taller_3_punto_15():
                    import random
                    matriz = []
                    dimensiones = random.randint(5,10)

                    for fila in range(dimensiones):
                        fila_actual = []
                        for columna in range(dimensiones):
                            fila_actual.append(random.randint(1,50))
                        matriz.append(fila_actual)

                    for fila in matriz:
                        print(" ".join("{:4}".format(n) for n in fila))

                    def es_fibonacci(numero):
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= numero:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 = secuencia
                            if secuencia == numero:
                                return True
                        return False

                    print("")

                    def contar_repeticiones(matriz):
                        repeticiones = {}
                        for fila in range(dimensiones):
                            for numero in matriz[fila]:
                                if numero in repeticiones:
                                    repeticiones[numero] += 1
                                else:
                                    repeticiones[numero] = 1
                        return repeticiones
                    matriz = contar_repeticiones(matriz)
                    contadores_fibonaccis = []
                    for numero, repeticiones in matriz.items():
                        if es_fibonacci(numero):
                            if repeticiones > 1 and repeticiones not in contadores_fibonaccis:
                                contadores_fibonaccis.append(repeticiones)
                            print(f"Numero: {numero}  Repeticiones:  {repeticiones}")

                    print(f"\nContadores de numeros fibonacci que se repiten en la matriz\n {contadores_fibonaccis}")

                taller_3_punto_15()
            if respuesta_taller_3 == 16:
                def taller_3_punto_16():
                    import random
                    matriz = []
                    dimensiones = random.randint(5,10)

                    for fila in range(dimensiones):
                        fila_actual = []
                        for columna in range(dimensiones):
                            fila_actual.append(random.randint(1,50))
                        matriz.append(fila_actual)

                    print("\nMatriz Original")
                    for fila in matriz:
                        print(" ".join("{:4}".format(n) for n in fila))

                    for i in range(dimensiones):
                        for j in range(dimensiones):
                            if i == 0:
                                matriz[j][i], matriz[j][-i-1] = matriz[j][-i-1], matriz[j][i]

                    print("\nCambiar primera con ultima columna")
                    for fila in matriz:
                        print(" ".join("{:4}".format(n) for n in fila))
                    print("")
                    contador_mayor_menor = 0
                    for i in range(dimensiones):
                        promedio_columna = 0
                        suma_columna = 0
                        contador_columna = 0
                        for j in range(dimensiones):
                            suma_columna += matriz[j][i]
                            contador_columna += 1
                            contador_mayor_menor += 1
                            if contador_mayor_menor == 1:
                                numero_mayor = matriz[j][i]
                                numero_menor = matriz[j][i]
                            else:
                                if numero_mayor < matriz[j][i]:
                                    numero_mayor = matriz[j][i]
                                if numero_menor > matriz[j][i]:
                                    numero_menor = matriz[j][i]
                        promedio_columna = suma_columna/contador_columna
                        print(f"Promedio de la columna {i+1}: {promedio_columna:.2f}")
                    print(f"\nNumero mayor: {numero_mayor}  Numero menor: {numero_menor}")

                    #-	Ordenar las filas pares ascendentemente y las filas impares descendentemente

                    for i in range(dimensiones):
                        if i % 2 == 0 and i < dimensiones - 1:
                            for j in range(dimensiones - 1):
                                for k in range(j + 1, dimensiones):
                                    if matriz[i][j] < matriz[i][k]:
                                        matriz[i][j], matriz[i][k] = matriz[i][k], matriz[i][j]
                        else:
                            for j in range(dimensiones - 1):
                                for k in range(j + 1, dimensiones):
                                    if matriz[i][j] > matriz[i][k]:
                                        matriz[i][j], matriz[i][k] = matriz[i][k], matriz[i][j]

                    print("\nFilas pares e impares ordenadas")
                    for fila in matriz:
                        print(" ".join("{:4}".format(n) for n in fila))

                    #-	Ordenar la matriz descendentemente

                    for i in range(dimensiones * dimensiones):
                        for j in range(dimensiones * dimensiones - i - 1):
                            fila_actual = j // dimensiones
                            columna_actual = j % dimensiones
                            siguiente_fila = (j+1) // dimensiones
                            siguiente_columna = (j+1) % dimensiones
                            if matriz[fila_actual][columna_actual] > matriz[siguiente_fila][siguiente_columna]:
                                matriz[fila_actual][columna_actual], matriz[siguiente_fila][siguiente_columna] = matriz[siguiente_fila][siguiente_columna], matriz[fila_actual][columna_actual]

                    print("\nMatriz ordenada ascendentemente")
                    for fila in matriz:
                        print(" ".join("{:4}".format(n) for n in fila))

                    #-	Intercambiar las filas de la matriz de acuerdo al orden ascendente de los promedios de cada fila

                    promedios_fila = []
                    for i in range(dimensiones):
                        suma_fila = 0
                        contador_fila = 0
                        promedio_fila = 0
                        for j in range(dimensiones):
                            suma_fila += matriz[i][j]
                            contador_fila += 1
                        promedio_fila = suma_fila/contador_fila
                        promedios_fila.append(promedio_fila)

                    for i in range(len(promedios_fila)):
                        for j in range(len(promedios_fila)- i - 1):
                            if promedios_fila[j] < promedios_fila[j+1]:
                                promedios_fila[j], promedios_fila[j+1] = promedios_fila[j+1], promedios_fila[j]
                                matriz[j], matriz[j+1] = matriz[j+1], matriz[j]

                    print("\nMatriz ordenada con promedios")
                    for i, fila in enumerate(matriz):
                        print(" ".join("{:4}".format(n) for n in fila),f"  Promedio fila {i+1}: {promedios_fila[i]:.2f}")

                    #-	Intercambiar las filas donde se encuentre el mayor y el menor de la matriz

                    contador_mayor_menor = 0
                    for i, fila in enumerate(matriz):
                        for numero in fila:
                            contador_mayor_menor += 1
                            if contador_mayor_menor == 1:
                                numero_mayor = numero
                                posicion_numero_mayor = i
                                numero_menor = numero
                                posicion_numero_menor = i
                            else:
                                if numero_mayor < numero:
                                    numero_mayor = numero
                                    posicion_numero_mayor = i
                                if numero_menor > numero:
                                    numero_menor = numero
                                    posicion_numero_menor = i

                    matriz[posicion_numero_mayor], matriz[posicion_numero_menor] = matriz[posicion_numero_menor], matriz[posicion_numero_mayor]

                    print("\nMatriz con filas numero mayor y menor cambiadas")
                    for fila in matriz:
                        print(" ".join("{:4}".format(n) for n in fila))

                    #-	Intercambiar la fila donde se encuentre el Fibonacci 2 con la fila donde se encuentra el  Fibonacci 4.

                    def es_fibonacci(numero):
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= numero:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 = secuencia
                            if secuencia == numero:
                                return True
                        return False

                    fibonacci_mayor = 0
                    fibonacci_menor = float("inf")
                    for i, fila in enumerate(matriz):
                        for numero in fila:
                            if es_fibonacci(numero):
                                if numero > fibonacci_mayor:
                                    fibonacci_mayor = numero
                                    posicion_fibonacci_mayor = i
                                if numero < fibonacci_menor:
                                    fibonacci_menor = numero
                                    posicion_fibonacci_menor = i

                    matriz[posicion_fibonacci_mayor], matriz[posicion_fibonacci_menor] = matriz[posicion_fibonacci_menor], matriz[posicion_fibonacci_mayor]

                    print(f"\nCon fila fibonacci mayor: {fibonacci_mayor} y menor: {fibonacci_menor} cambiadas")
                    for fila in matriz:
                        print(" ".join("{:4}".format(n) for n in fila))

                    #-	Intercambiar las filas donde se encuentre el primo mayor y el Fibonacci menor

                    def es_primo(numero):
                        condicion = 1
                        divisores = 0
                        while condicion <= numero:
                            if numero % condicion == 0:
                                divisores += 1
                            condicion += 1
                        if divisores == 2:
                            return True
                        return False

                    primo_mayor = 0
                    fibonacci_menor = float("inf")

                    for i, fila in enumerate(matriz):
                        for numero in fila:
                            if es_primo(numero):
                                if numero > primo_mayor:
                                    primo_mayor = numero
                                    posicion_primo_mayor = i
                            if es_fibonacci(numero):
                                if numero < fibonacci_menor:
                                    fibonacci_menor = numero
                                    posicion_fibonacci_menor = i

                    matriz[posicion_fibonacci_menor], matriz[posicion_primo_mayor] = matriz[posicion_primo_mayor], matriz[posicion_fibonacci_menor]

                    print(f"\nCon fila fibonacci menor: {fibonacci_menor} con primo mayor: {primo_mayor} cambiadas")
                    for fila in matriz:
                        print(" ".join("{:4}".format(n) for n in fila))

                    #-	Determinar si el primo 2 y el primo 4 según el recorrido por filas de la matriz, son consecutivos, es decir, no hay un número primo entre los dos

                    contador_primos = 0
                    for i in range(dimensiones):
                        for j in range(dimensiones):
                            if es_primo(matriz[i][j]):
                                contador_primos += 1
                                if contador_primos == 2:
                                    segundo_primo = matriz[i][j]
                                if contador_primos == 4:
                                    cuarto_primo = matriz[i][j]
                                    break

                    if segundo_primo < cuarto_primo:
                        es_consecutivo = True
                        contador = segundo_primo + 1
                        while contador < cuarto_primo:
                            condicion = 1
                            divisores = 0
                            while condicion <= contador:
                                if contador % condicion == 0:
                                    divisores += 1
                                condicion += 1
                            if divisores == 2:
                                es_consecutivo = False
                                break
                            contador += 1
                        if es_consecutivo:
                            print(f"El primo: {cuarto_primo} si es consecutivo del segundo primo: {segundo_primo}")
                    else:
                        print(f"El primo: {cuarto_primo} no es consecutivo del segundo primo: {segundo_primo}")

                taller_3_punto_16()
            if respuesta_taller_3 == 17:
                def taller_3_punto_17():
                    #17.	Se tiene una matriz cuadrada de orden N realizar lo siguiente
                    #-	Hallar el promedio de la diagonal principal y el promedio de la diagonal secundaria
                    #-	Ordenar ascendentemente la diagonal principal
                    #-	Hallar el promedio de los pares que están encima de la diagonal principal y de los impares de la diagonal secundaria
                    #-	Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con el Fibonacci mayor.
                    #-	Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.

                    import random

                    matriz = []
                    dimensiones = random.randint(5,10)

                    for i in range(dimensiones):
                        fila_actual = []
                        for j in range(dimensiones):
                            fila_actual.append(random.randint(1,100))
                        matriz.append(fila_actual)

                    def mostrar_matriz(matriz):
                        for fila in matriz:
                            print(" ".join("{:4}".format(n) for n in fila))

                    print("\nMatriz original")
                    mostrar_matriz(matriz)

                    #-	Hallar el promedio de la diagonal principal y el promedio de la diagonal secundaria

                    suma_diagonal_principal = 0
                    contador_diagonal_princiapal = 0
                    promedio_diagonal_principal = 0
                    suma_diagonal_secundaria = 0
                    contador_diagonal_secundaria = 0
                    promedio_diagonal_secundaria = 0

                    for i in range(dimensiones):
                        suma_diagonal_principal += matriz[i][i]
                        contador_diagonal_princiapal += 1
                        suma_diagonal_secundaria += matriz[i][-i-1]
                        contador_diagonal_secundaria += 1

                    promedio_diagonal_principal = suma_diagonal_principal/contador_diagonal_princiapal
                    promedio_diagonal_secundaria = suma_diagonal_secundaria/contador_diagonal_secundaria

                    print(f"\nPromedio diagonal principal: {promedio_diagonal_principal:.2f}\nPromedio diagonal secundaria: {promedio_diagonal_secundaria:.2f}")

                    for i in range(dimensiones - 1):
                        for j in range(i+1, dimensiones):
                            if matriz[i][i] > matriz[j][j]:
                                matriz[i][i], matriz[j][j] = matriz[j][j], matriz[i][i]

                    print("\nCon diagonal principal ordenada ascendentemente")
                    mostrar_matriz(matriz)

                    #-	Hallar el promedio de los pares que están encima de la diagonal principal y de los impares de la diagonal secundaria

                    suma_pares_up_diagonal_principal = 0
                    contador_pares_up_diagonal_princiapal = 0
                    promedio_pares_up_diagonal_principal = 0
                    promedio_impares_diagonal_secundaria = 0
                    contador_impares_diagonal_secundaria = 0
                    suma_impares_diagonal_secundaria = 0

                    def es_par(numero):
                        if numero % 2 == 0:
                            return True
                        return False
                    def es_impar(numero):
                        if numero % 2 != 0:
                            return True
                        return False

                    for i in range(dimensiones):
                        if i < dimensiones - 1:
                            if es_par(matriz[i][i+1]):
                                suma_pares_up_diagonal_principal += matriz[i][i+1]
                                contador_pares_up_diagonal_princiapal += 1
                        if es_impar(matriz[i][-i-1]):
                            suma_impares_diagonal_secundaria += matriz[i][-i-1]
                            contador_impares_diagonal_secundaria += 1
                    if suma_pares_up_diagonal_principal == 0:
                        print("No hay numeros pares en la diagonal superior de la diagonal principal")
                    else:
                        promedio_pares_up_diagonal_principal = suma_pares_up_diagonal_principal/contador_pares_up_diagonal_princiapal
                        print(f"\nPromedio pares up diagonal 1: {promedio_pares_up_diagonal_principal:.2f}")
                    if suma_impares_diagonal_secundaria == 0:
                        print("No hay numeros impares en la diagonal secundaria")
                    else:
                        promedio_impares_diagonal_secundaria = suma_impares_diagonal_secundaria/contador_impares_diagonal_secundaria
                        print(f"Promedio impares diagonal 2: {promedio_impares_diagonal_secundaria:.2f}")

                    def es_primo(numero):
                        divisores = 0
                        condicion = 1
                        while condicion <= numero:
                            if numero % condicion == 0:
                                divisores += 1
                            condicion += 1
                        if divisores == 2:
                            return True
                        return False

                    def es_fibonacci(numero):
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= numero:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 = secuencia
                            if secuencia == numero:
                                return True
                        return False

                    fibonacci_mayor = 0
                    primo_menor = float("inf")
                    par_mayor = 0
                    impar_menor = float("inf")

                    for fila in matriz:
                        for numero in fila:
                            if es_fibonacci(numero):
                                if numero > fibonacci_mayor:
                                    fibonacci_mayor = numero
                            if es_primo(numero):
                                if numero < primo_menor:
                                    primo_menor = numero
                            if es_par(numero):
                                if numero > par_mayor:
                                    par_mayor = numero
                            if es_impar(numero):
                                if numero < impar_menor:
                                    impar_menor = numero

                    #-	Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con el Fibonacci mayor.

                    for i in range(dimensiones):
                        matriz[i][i] = primo_menor
                        matriz[i][-i-1] = fibonacci_mayor

                    print(f"\nMatriz con diagonal principal primo menor: {primo_menor}")
                    print(f"y diagonal secundaria fibonacci mayor: {fibonacci_mayor}")
                    mostrar_matriz(matriz)

                    #-	Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.

                    for i in range(dimensiones):
                        for j in range(dimensiones):
                            if i == 0 or i == dimensiones - 1 or j == 0 or j == dimensiones - 1:
                                matriz[i][j] = par_mayor
                            else:
                                matriz[i][j] = impar_menor

                    print(f"\nMatriz con contorno par mayor: {par_mayor}")
                    print(f"y su interior con el impar menor: {impar_menor}")
                    mostrar_matriz(matriz)
                taller_3_punto_17()
            if respuesta_taller_3 == 18:
                def taller_3_punto_18():
                    #18.	Se tienen dos matrices con datos numéricos y se solicita;
                    #-	Formar un vector con los elementos comunes de las dos matrices sin repetidos
                    #-	Formar un vector con los primos comunes de las dos matrices sin repetidos
                    #-	Formar un vector con los primos no comunes de las dos matrices sin repetidos

                    import random
                    matriz1 = []
                    matriz2 = []

                    def llenar_matriz(matriz):
                        dimensiones = random.randint(5,6)
                        for fila in range(dimensiones):
                            fila_actual = []
                            for columna in range(dimensiones):
                                fila_actual.append(random.randint(1,50))
                            matriz.append(fila_actual)

                    def mostrar_matriz(matriz):
                        for fila in matriz:
                            print(" ".join("{:4}".format(n) for n in fila))

                    llenar_matriz(matriz1)
                    llenar_matriz(matriz2)
                    print("\nMatriz 1")
                    mostrar_matriz(matriz1)
                    print("\nMatriz 2")
                    mostrar_matriz(matriz2)

                    def es_primo(numero):
                        condicion = 1
                        divisores = 0
                        while condicion <= numero:
                            if numero % condicion == 0:
                                divisores += 1
                            condicion += 1
                        if divisores == 2:
                            return True
                        return False

                    numeros_comunes = []
                    primos_comunes = []

                    for fila in matriz1:
                        for numero in fila:
                            if es_primo(numero):
                                for fila2 in matriz2:
                                    if numero in fila and numero not in primos_comunes:
                                        primos_comunes.append(numero)
                            for fila2 in matriz2:
                                if numero in fila and numero not in numeros_comunes:
                                    numeros_comunes.append(numero)

                    print(f"\nNumeros comunes: {sorted(numeros_comunes)}")
                    print(f"Primos comunes: {sorted(primos_comunes)}")

                    primos_no_comunes = []

                    for fila in matriz1:
                        for numero in fila:
                            if es_primo(numero):
                                es_comun = True
                                for fila2 in matriz2:
                                    if numero in fila2:
                                        es_comun = False
                                        break
                                if es_comun and numero not in primos_no_comunes:
                                    primos_no_comunes.append(numero)
                    for fila2 in matriz2:
                        for numero in fila2:
                            if es_primo(numero):
                                es_comun = True
                                for fila in matriz1:
                                    if numero in fila:
                                        es_comun = False
                                        break
                                if es_comun and numero not in primos_no_comunes:
                                    primos_no_comunes.append(numero)

                    print(f"Primos no comunes en las matricez: {sorted(primos_no_comunes)}")
                taller_3_punto_18()
            if respuesta_taller_3 == 19:
                def taller_3_punto_19():
                    #19.	Se tiene una matriz con datos numéricos repetidos,
                    # formar un vector con aquellos contadores de datos que se repiten y que sean números Fibonacci, sin repetidos

                    import random

                    matriz = []
                    dimensiones = random.randint(5,10)

                    for i in range(dimensiones):
                        fila_actual = []
                        for j in range(dimensiones):
                            fila_actual.append(random.randint(1,50))
                        matriz.append(fila_actual)

                    print("\nMatriz Original")
                    for fila in matriz:
                        print(" ".join("{:4}".format(n) for n in fila))

                    def es_fibonacci(numero):
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= numero:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 = secuencia
                            if secuencia == numero:
                                return True
                        return False
                    todoscontadores = []
                    contadores = []
                    repeticiones = {}
                    print("")
                    for fila in matriz:
                        for numero in fila:
                            if es_fibonacci(numero):
                                if numero in repeticiones:
                                    repeticiones[numero] += 1
                                else:
                                    repeticiones[numero] = 1

                    for numero, repeticion in repeticiones.items():
                        print(f"Numero: {numero}  Repeticiones: {repeticion}")
                        if repeticion > 1:
                            todoscontadores.append(repeticion)
                        if repeticion > 1 and repeticion not in contadores:
                            contadores.append(repeticion)

                    print(f"\nTodos los contadores de fibonaccis que se repiten: {todoscontadores}")
                    print(f"Contadores de fibonaccis que se repiten sin repetidos: {contadores}")

                taller_3_punto_19()
        if respuesta == 4:
            respuesta_evaluacion_1 = int(input("""Escoja un punto
                                            
                                            UNIVERSIDAD DE NARIÑO
                                            FACULTAD DE INGENIERIA
                                            INGENIERÍA DE SISTEMAS
                                            PROGRAMACION DE COMPUTADORES
                                            EVALUACIÓN 1  24%
                                            
                                            1.   Se tiene una cantidad de números dada, determinar el primo mayor, el Fibonacci menor,
                                            el par menor y realizar la multiplicación de ellos con sumas.25%
                                            2.   Se tiene una cantidad de números dada donde hay varios números que se repiten.
                                            Encontrar el número de veces que se repite el segundo Fibonacci (en orden de entrada)
                                            y determinar si este contador es un número primo. 25%
                                            3.   Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de
                                            triángulos, determinar cuántos triángulos equiláteros, escalenos e isósceles se encuentran
                                            en estos y si la suma de los perímetros de los triángulos equiláteros, es un número Fibonacci. 25%
                                            4.	Se tiene una cantidad de números dada, encontrar los tres primeros Fibonacci de acuerdo
                                            al orden de entrada y determinar el promedio de los números pares
                                            que están entre el mayor y el menor de estos Fibonacci. 25%"""))
            if respuesta_evaluacion_1 == 1:
                def evaluacion_1_punto_1():
                    cantidad=int(input("Cantidad de numeros->"))
                    contador=1
                    primos=0
                    fibonaccis=0
                    pares=0
                    while contador<=cantidad:
                        num=int(input("Ingrese el número->"))
                        condicion=1
                        divisores=0
                        while condicion<=num:
                            if num & condicion == 0:
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
                    resultado=0
                    while condicion<=primo_mayor:
                        suma2+=suma
                        condicion+=1
                    resultado=suma2
                    print("La multiplicación con sumas es: ", resultado)
                evaluacion_1_punto_1()
            if respuesta_evaluacion_1 == 2:
                def evaluacion_1_punto_2():
                    cantidad = int(input("Ingrese la cantidad de números: "))
                    contador = 1
                    repeticiones = 0
                    fibonaccis = 0
                    segundo = 0

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
                                fibonaccis += 1
                                if fibonaccis == 2:
                                    segundo = num
                                else: 
                                    if num == segundo:
                                        repeticiones += 1
                        contador += 1

                    se_repite = repeticiones + 1
                    condicion = 1
                    divisores = 0
                    while condicion <= se_repite:
                        if se_repite % condicion == 0:
                            divisores += 1
                        condicion += 1

                    if divisores == 2:
                        print("El número de veces en el que se repite el segundo Fibonacci es un número primo.")
                    else:
                        print("El número de veces en el que se repite el segundo Fibonacci no es un número primo.")

                evaluacion_1_punto_2()
            if respuesta_evaluacion_1 == 3:
                def evaluacion_1_punto_3():
                    cantidad = int(input("Ingrese la cantidad de triángulos: "))
                    contador = 1
                    equilateros = 0
                    isoceles = 0
                    escalenos = 0
                    suma_equilateros = 0
                    
                    while contador <= cantidad:
                        lado1 = int(input("Ingrese el lado 1: "))
                        lado2 = int(input("Ingrese el lado 2: "))
                        lado3 = int(input("Ingrese el lado 3: "))
                        
                        if lado1 == lado2 == lado3:
                            equilateros += 1
                            suma_equilateros += lado1 + lado2 + lado3
                        elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
                            escalenos += 1
                        else:
                            isoceles += 1
                        
                        contador += 1

                    num1 = 0
                    num2 = 1
                    secuencia = 0
                    es_fibonacci = False
                    
                    while secuencia <= suma_equilateros:
                        secuencia = num1 + num2
                        num1 = num2
                        num2 = secuencia
                        if secuencia == suma_equilateros:
                            es_fibonacci = True
                    
                    if es_fibonacci:
                        print("La suma de los perímetros de los triángulos equiláteros es un número Fibonacci.")
                    else:
                        print("La suma de los perímetros de los triángulos equiláteros no es un número Fibonacci.")
                evaluacion_1_punto_3()
            if respuesta_evaluacion_1 == 4:
                def evaluacion_1_punto_4():
                    cantidad = int(input("Ingrese la cantidad de números: "))
                    contador = 1
                    contador_fibonacci = 0
                    primero = None
                    segundo = None
                    tercero = None

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
                                contador_fibonacci += 1
                                if contador_fibonacci == 1:
                                    primero = num
                                elif contador_fibonacci == 2:
                                    segundo = num
                                elif contador_fibonacci == 3:
                                    tercero = num
                                contador += 1

                    mayor = primero
                    menor = primero

                    if segundo > mayor:
                        mayor = segundo
                    if tercero > mayor:
                        mayor = tercero

                    if segundo < menor:
                        menor = segundo
                    if tercero < menor:
                        menor = tercero

                    contador_pares = 0
                    suma = 0
                    num = menor

                    while num <= mayor:
                        if num % 2 == 0:
                            suma += num
                            contador_pares += 1
                        num += 1

                    if contador_pares > 0:
                        promedio = suma / contador_pares
                        print("El promedio entre el Fibonacci mayor y el Fibonacci menor, solo de los pares entre estos 2 números es:", promedio)
                    else:
                        print("No hay números pares entre el Fibonacci mayor y el Fibonacci menor.")
            evaluacion_1_punto_4()
        if respuesta == 5:
            respuesta_evaluacion_2 = int(input("""Escoja un punto
                                            
                                            UNIVERSIDAD DE NARIÑO
                                            FACULTAD DE INGENIERIA
                                            INGENIERÍA DE SISTEMAS
                                            PROGRAMACION DE COMPUTADORES
                                            EVALUACIÓN 2  24%
                                            
                                                1.	Se tiene varios datos numéricos repetidos y agrupados  donde el último dato es un -5,
                                                realizar los siguiente, hallar la multiplicación con sumas, de la cantidad de datos del grupo
                                                que más se repite por la cantidad de datos del grupo que menos se repite

                                                2.	Se tienen dos vectores con datos numéricos donde hay varios repetidos, formar dos vectores asi:
                                                Vector 1 con la unión de solo números Fibonacci sin repetidos, sin tener en cuenta aquellos Fibonacci que sean comunes.
                                                Vector 2 con los múltiplos de 3 comunes, que no sean múltiplos de 5

                                                3.	Se tienen dos vectores con datos numéricos, donde el tercer Fibonacci del vector uno determina
                                                la cantidad de datos a tener en cuenta en el vector dos, formando dos rangos un rango con la cantidad
                                                de datos que establece el Fibonacci y el rango dos con el resto, ordenar el primer rango en orden
                                                ascendente y el segundo en orden descendente 
                                                """))
            if respuesta_evaluacion_2 == 1:
                def evaluacion_2_punto_1():
                    repeticiones = {}
                    max_repeticiones = 0
                    min_repeticiones = 0
                    def rompimiento_de_control():
                        numeros = []
                        while True:
                            try:
                                num = input("Ingrese un número: ")
                                if num == "-5":
                                    return numeros
                                else:
                                    numeros.append(int(num))
                            except ValueError:
                                print("Ingrese un valor valido")
                    numeros = rompimiento_de_control()
                    for n in numeros:
                        if n in repeticiones:
                            repeticiones[n] += 1
                        else:
                            repeticiones[n] = 1
                    max_repeticiones = max(repeticiones.values())
                    min_repeticiones = min(repeticiones.values())
                    resultado = 0
                    contador = 1
                    suma = 0
                    while contador <= max_repeticiones:
                        suma += min_repeticiones
                        contador += 1
                    resultado = suma
                    print(f"{min_repeticiones}x{max_repeticiones}={resultado}")
                evaluacion_2_punto_1()
            if respuesta_evaluacion_2 == 2:
                def evaluacion_2_punto_2():
                    import random
                    numeros1 = []
                    numeros2 = []
                    for n in range(20):
                        num = random.randint(1, 35)
                        numeros1.append(num)
                    for n in range(20):
                        num = random.randint(1, 35)
                        numeros2.append(num)
                    fibonaccis = []
                    print(numeros1)
                    print(numeros2)
                    for n in numeros1 + numeros2:
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= n:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 = secuencia
                            if secuencia == n and ((n in numeros1 and n not in numeros2) or (n in numeros2 and n not in numeros1)):
                                fibonaccis.append(n)
                    vector1 = []
                    for n in fibonaccis:
                        if n not in vector1:
                            vector1.append(n)
                    vector2 = []
                    for n in numeros1 + numeros2:
                        if n % 3 == 0 and n % 5 != 0 and ((n in numeros1 and n not in numeros2) or (n in numeros2 and n not in numeros1)):
                            vector2.append(n)
                    print("Vector 1:", vector1)
                    print("Vector 2:", vector2)
                evaluacion_2_punto_2()
            if respuesta_evaluacion_2 == 3:
                def evaluacion_2_punto_3():
                    import random
                    numeros1 = []
                    numeros2 = []
                    for n in range(20):
                        num = random.randint(1, 35)
                        numeros1.append(num)

                    for n in range(20):
                        num = random.randint(1, 35)
                        numeros2.append(num)

                    contador_fibonaccis = 0
                    posicion_tercer_fibonacci = 0

                    for indice, f in enumerate(numeros1):
                        num1 = 0
                        num2 = 1
                        secuencia = 0
                        while secuencia <= f:
                            secuencia = num1 + num2
                            num1 = num2
                            num2 = secuencia
                            if secuencia == f:
                                contador_fibonaccis += 1
                                if contador_fibonaccis == 3:
                                    tercer_fibonacci = f
                                    posicion_tercer_fibonacci = indice

                    for i in range(posicion_tercer_fibonacci):
                        for j in range(posicion_tercer_fibonacci):
                            if numeros2[j] > numeros2[j+1]:
                                numeros2[j], numeros2[j+1] = numeros2[j+1], numeros2[j]

                    for i in range(posicion_tercer_fibonacci, len(numeros2)-1):
                        for j in range(posicion_tercer_fibonacci, len(numeros2)-1):
                            if numeros2[j] < numeros2[j+1]:
                                numeros2[j], numeros2[j+1] = numeros2[j+1], numeros2[j]

                    print(numeros2)
                    
                evaluacion_2_punto_3()
        if respuesta == 6:
            print("Hasta Luego")
            break
menu_inicio()