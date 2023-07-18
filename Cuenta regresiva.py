import time

inicio = time.time()
for i in range(11):
    print((10-i))
    time.sleep(1)
final = time.time()
print(final-inicio)