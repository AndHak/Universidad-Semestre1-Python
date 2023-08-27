
segundo_primo = None
contador_segundo_primo = 0
contador_primos = 0

while True:
    num = input("Ingresa un número, 'c' para terminar")
    if num.lower() == "c":
        break
    else:
        num = int(num)
        divisores = 0
        condicion = 1
        while condicion <= num:
            if num % condicion == 0:
                divisores += 1
            condicion += 1
        if divisores == 2:
            contador_primos += 1
            if contador_primos == 2:
                segundo_primo = num
            elif num == segundo_primo:
                contador_segundo_primo += 1
    
print(f"El segundo primo ({segundo_primo}) se repitió {contador_segundo_primo} veces más.")