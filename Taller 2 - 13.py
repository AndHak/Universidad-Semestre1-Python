#13.	Se tienen dos vectores con datos numéricos formar un vector con la unión de los Fibonacci sin repetidos.
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




