#18.	Se tiene un vector con datos numéricos donde hay varios Fibonacci,
#encontrar el segundo y tercer Fibonacci y sus posiciones,
#reemplazar las posiciones comprendidas en estos dos valores con el factorial del Fibonacci menor de los dos.

numeros = [3, 21, 6, 4, 7, 9, 11, 12, 8, 10, 5]

contador_fibonacci = 0
segundo_fibonacci, tercer_fibonacci = None, None
posicion_segundo_fibonacci, posicion_tercer_fibonacci = None, None

for i in range(len(numeros)):
    n = numeros[i]
    es_fibonacci = False
    num1, num2 = 0, 1
    secuencia = 0
    while secuencia <= n:
        secuencia = num1 + num2
        num1, num2 = num2, secuencia
        if secuencia == n:
            contador_fibonacci += 1
            es_fibonacci = True
            if contador_fibonacci == 2:
                segundo_fibonacci = n
                posicion_segundo_fibonacci = i+1
            if contador_fibonacci == 3:
                tercer_fibonacci = n
                posicion_tercer_fibonacci = i+1


print("Segundo fibonacci:", segundo_fibonacci, "posición:", posicion_segundo_fibonacci)
print("Tercer fibonacci:", tercer_fibonacci, "posición:", posicion_tercer_fibonacci)
print(numeros)
