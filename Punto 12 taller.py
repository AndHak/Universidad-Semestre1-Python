cd = int(input("Digite la cantidad de datos"))
sum_factorial_primos = 0
sum_factorial_fib = 0
cp = 0
cf = 0

for i in range(cd):
    num = int(input("digite el dato->"))
    div = 0
    con = 1
    
    while con <= num:
        if num % con == 0:
            div += 1
        con += 1
        
    if div == 2:
        cp += 1
        z = 1
        temp_num = num
        while temp_num > 0:
            z *= temp_num
            temp_num -= 1
        sum_factorial_primos += z
    else:
        a = 0
        b = 1
        c = 0
        while c < num:
            c = a + b
            a = b
            b = c
        if c == num:
            cf += 1
            s = 1
            temp_num = num
            while temp_num > 0:
                s *= temp_num
                temp_num -= 1
            sum_factorial_fib += s

if cp > 0:
    prom_primos = sum_factorial_primos / cp
else:
    prom_primos = 0
    print("No hay numeros primos")
    
if cf > 0:
    prom_fib = sum_factorial_fib / cf
else:
    prom_fib = 0
    print("No hay numeros fibonaccis")

if prom_fib > 0 and prom_primos > 0:
    if prom_fib > prom_primos:
        print(f"El promedio de los factoriales de los números Fibonacci es {prom_fib}, siendo mayor que el promedio de los factoriales de los números primos que es {prom_primos}")
    else:
        print(f"El promedio de los factoriales de los números primos es {prom_primos}, siendo mayor que el promedio de los factoriales de los números Fibonacci que es {prom_fib}")
