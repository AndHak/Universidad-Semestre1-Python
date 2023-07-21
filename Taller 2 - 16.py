#16.	Se tienen un vector con datos numéricos donde hay varios números Fibonacci
#formar un tercer vector con los números primos que están entre el Fibonacci mayor y el Fibonacci menor.

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






