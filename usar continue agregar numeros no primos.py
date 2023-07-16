#Agregar a un vector los no primos usando continue

def no_primos():
    no_primos = []
    while True:
        num = input('Precione "c" para terminar, Ingrese un numero:  ')
        try:
            if num == "c":
                return no_primos
            else:
                num = int(num)
                condicion = 1
                dividores = 0
                while condicion <= num:
                    if num % condicion == 0:
                        dividores += 1
                    condicion += 1
                if dividores == 2:
                    continue
                else:
                    no_primos.append(num)
        except ValueError:
            print("Entrada no valida, intente con otro valor")

no_primos = no_primos()
print(no_primos)