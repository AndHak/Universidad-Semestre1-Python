#Se tiene una cantidad de números dada donde hay varios primos determinar 
#las tablas de multiplicar que están entre el primo menor y primo mayor.
cantidad=int(input("Digite la cantidad de datos->"))
contadorp=0
pmayor=0
pmenor=0
for r in range(cantidad):
    num=int(input("Digite un dato->"))
    cdivisores=0
    i=1
    while i<=num:
        if num%i==0:
            cdivisores+=1
        i+=1
    if cdivisores==2:
        contadorp+=1
        if contadorp==1:
            pmenor=num
            pmayor=num
        else:
            if num<pmenor:
                pmenor=num
            elif num>pmayor:
                pmayor=num
        
if contadorp<2:
    print("no hay los suficientes numeros primos")
else:
    for p in range(pmenor, pmayor+1):
        print(f"Tabla de multiplicar para {p}:")
        contador_tablas=1 
        while contador_tablas<10:
            tabla=p*contador_tablas
            print(f"{p} x {contador_tablas} = {tabla}")
            contador_tablas+=1
            


