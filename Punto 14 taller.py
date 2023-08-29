#Se tiene una cantidad de números dada donde hay varios números Fibonacci, obtener los Fibonacci 1, 3, 4 
# (de acuerdo al orden de entrada) y mostrar el menor y el mayor de ellos.
cantidad=int(input("Digite la canntidad de datos->"))
contadorf=0
for i in range(cantidad):
    num=int(input("digite un dato->"))
    a=0
    b=1
    c=0
    while c<num:
        c=a+b
        a=b
        b=c
    if c==num:
        contadorf+=1
        if contadorf==1:
            primerf=num
        if contadorf==3:
            tercerf=num
        if contadorf==4:
            cuartof=num
if primerf>tercerf:
    if primerf>cuartof:
        print(f"el mayor fibonacci es el primero=={primerf}")
        if tercerf<cuartof:
            print(f"el menor fibonacci es el tercero=={tercerf}")

        else:  
            print(f"el menor fibonacci es el cuarto=={cuartof}")  
    else:
        print(f"el mayor fibonacci es el cuarto=={cuartof}")
        if tercerf<primerf:
            print(f"el menor fibonacci es el tercero=={tercerf}")

        else:  
            print(f"el menor fibonacci es el primero=={primerf}")
else:
    if tercerf>cuartof:
        print(f"el mayor fibonacci es el tercero=={tercerf}")
        if cuartof<primerf:
            print(f"el menor fibonacci es el cuarto=={cuartof}")

        else:  
            print(f"el menor fibonacci es el primero=={primerf}")
    else: 
        print(f"el mayor fibonacci es el cuarto=={cuartof}")
        if tercerf<primerf:
            print(f"el menor fibonacci es el tercero=={tercerf}")

        else:  
            print(f"el menor fibonacci es el primero=={primerf}")
    