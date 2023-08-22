"""3.	Una empresa de servicios públicos desea calcular el valor de una factura de servicio de agua, teniendo en cuenta lo siguiente
Se tiene el código del usuario, consumo mensual en  metros cúbicos, el valor del metro cúbico, el estrato y se realiza el calculo de acuerdo a la siguiente consideración:
Con respecto al estrato  
Si el usuario es del estrato 1  descuento del 40%
Estrato 2 		descuento del 30%
Estrato 3 		descuento del 15%
Estrato 4		no tiene descuento
Estrato 5 y 6 		Incremento en la factura del 20%
Para todos los anteriores si el consumo en metros cúbicos es mayor a 10, sobre al valor anterior se incrementa el  10%,
"""

def taller1_3():
    codigos = []
    estratos = []
    i = -1
    while True:
        pregunta = input("Desea calcular el valor de su factura S/N: ")
        try:
            if pregunta.lower() == "n":
                return taller1_3
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
taller1_3()
