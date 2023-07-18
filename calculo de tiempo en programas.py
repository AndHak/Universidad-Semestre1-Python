import time
suma = 0
inicio = time.time()
for i in range(1,1000001):
    suma += i
final = time.time()
print(suma)
print(final-inicio)


inicio2 = time.time()
suma2 = 0
num = 1
while num <= 1000000:
    suma2 += num
    num += 1
final2 = time.time()
print(suma2)
print(final2-inicio2)