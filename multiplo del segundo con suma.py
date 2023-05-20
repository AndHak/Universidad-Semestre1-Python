num = int(input("numero 1"))
num2 = int(input("numero 2"))
resta = num

while resta >= num2:
    resta = resta - num2
if resta == 0:
    print(num, "es multiplo de", num2)
else:
    print(num, "no es multiplo de", num2)
