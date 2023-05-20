num = int(input("determinador de numero primo"))
contador = 0
condicion = 1
determinador = 2

while condicion <= num:
    if num % condicion == 0:
        contador = contador + 1
    condicion = condicion + 1
if contador <= determinador:
    print(num,"es un numero primo")
else:
    print(num,"no es un numero primo")