print("Hello world")
num = 1
contador = 1

while contador <= 10:
    print("tabla del", contador)
    while num <= 10:
        resultado = num * contador
        print(num,"x", contador, "=", resultado)
        num = num + 1
    contador = contador + 1
    num = 1
