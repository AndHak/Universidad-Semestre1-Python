cantidad = int(input("Cantidad de números: "))
fibonaccis = []

for _ in range(cantidad):
    num = int(input("Ingrese un número: "))
    num1 = 0
    num2 = 1
    secuencia = 0

    while secuencia < num:
        secuencia = num1 + num2
        num1 = num2
        num2 = secuencia

        if secuencia == num:
            fibonaccis.append(num)
            break

fibonaccis = sorted(fibonaccis)

print("Los números de Fibonacci encontrados son:", fibonaccis)
print("El número de Fibonacci más pequeño es:", fibonaccis[0])
print("El número de Fibonacci más grande es:", fibonaccis[-1])

