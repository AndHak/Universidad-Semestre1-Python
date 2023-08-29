cantidad_datos=int(input("digite la cantidad de datos->"))
cp=0
suma_factorial_primos=0
for i in range(cantidad_datos):
    num=int(input("Digite dato->"))
    r=2
    cd=0
    while r < num:
        if num % r==0:
            cd+=1
        r+=1  
    if cd==0:
        primo=num
        cp+=1
        z=1
        for j in range(1, num + 1):
            z *= j
        suma_factorial_primos += z
        
promedio=suma_factorial_primos/cp if cp > 0 else 0
if cp>0:
    print("el promedio de los factoriales de los primos es", promedio)
else:
    print("no hay primos")