#17.	Se tienen un vector con datos numéricos donde hay varios números Fibonacci
#hallar el promedio de los múltiplos de tres, que están entre el segundo y tercer Fibonacci del vector.

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