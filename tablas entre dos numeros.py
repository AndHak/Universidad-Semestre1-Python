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