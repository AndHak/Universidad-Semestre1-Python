cantidad = int(input("Cantidad de numeros"))
Fibonaccis = []
contador = 1
while contador <= cantidad:
    num = int(input("Ingrese un numero"))
    num1 = 0
    num2 = 1
    secuencia = 0
    while secuencia <= num:
        secuencia = num1 + num2
        num1 = num2
        num2 = secuencia
        if secuencia == num:
            Fibonaccis.append(num)
    contador += 1

Fibonaccis = sorted(Fibonaccis)
for i in Fibonaccis:
    print("Los fibonaccis encontrads son:", Fibonaccis)

print("El fibonacci menor es: ", Fibonaccis[0], "Y el fibonacci mayor es: ", Fibonaccis[-1])