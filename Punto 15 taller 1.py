#-	Se tiene una cantidad de números dada donde hay varios números Primos, obtener los primos  2, 3, 4  
# (de acuerdo al orden de entrada) y mostrarlos en forma ascendente, sin utilizar condiciones compuestas.
cantidad = int(input("Digite la cantidad de datos, en la cual deben haber minimo 4 primos y por ende la cantidad de numeros debe ser mayor a 4 -> "))
contadorp = 0
segundop = 0
tercerp = 0
cuartop = 0

for i in range(cantidad):
    num = int(input("Digite un dato -> "))
    a = 1
    divisores = 0
    
    while a <= num:
        if num % a == 0:
            divisores += 1
        a += 1
    
    if divisores == 2:
        contadorp += 1
        
        if contadorp == 2:
            segundop = num
        elif contadorp == 3:
            tercerp = num
        elif contadorp == 4:
            cuartop = num

if segundop > tercerp:
    if segundop > cuartop:
        print(f"El mayor primo es el segundo -> {segundop}")
        
        if tercerp < cuartop:
            print(f"El primo del medio es el cuarto -> {cuartop}")
            print(f"El menor primo es el tercero -> {tercerp}")
        else:
            print(f"El primo del medio es el tercero -> {tercerp}")
            print(f"El menor primo es el cuarto -> {cuartop}")
    else:
        print(f"El mayor primo es el cuarto -> {cuartop}")
        
        if tercerp < segundop:
            print(f"El primo del medio es el segundo -> {segundop}")
            print(f"El menor primo es el tercero -> {tercerp}")
        else:
            print(f"El primo del medio es el tercero -> {tercerp}")
            print(f"El menor primo es el segundo -> {segundop}")
else:
    if tercerp > cuartop:
        print(f"El mayor primo es el tercero -> {tercerp}")
        
        if cuartop < segundop:
            print(f"El primo del medio es el segundo -> {segundop}")
            print(f"El menor primo es el cuarto -> {cuartop}")
        else:
            print(f"El primo del medio es el cuarto -> {cuartop}")
            print(f"El menor primo es el segundo -> {segundop}")
    else:
        print(f"El mayor primo es el cuarto -> {cuartop}")
        
        if tercerp < segundop:
            print(f"El primo del medio es el segundo -> {segundop}")
            print(f"El menor primo es el tercero -> {tercerp}")
        else:
            print(f"El primo del medio es el tercero -> {tercerp}")
            print(f"El menor primo es el segundo -> {segundop}")