print("Calculadora para saber si es multiplo de 5")

n1 = int(input("ingrese el primer numero"))
n2 = int(input("ingrese el segundo numero"))
n3 = int(input("ingrese el tercer numero"))

m5 = False
if n1 % 5 == 0:
    print(n1,"es multiplo de 5")
    m5 = True
if n2 % 5 == 0:
    print(n2,"es multiplo de 5")
    m5 = True
if n3 % 5 == 0:
    print(n3,"es multiplo de 5")
    m5 = True

if not m5:
    print("no hay ningun multiplo de 5")            