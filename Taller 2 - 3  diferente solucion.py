#3.	Se tiene un vector con datos numéricos eliminar los datos que sean primos y Fibonacci.

numeros_no_fibonaccis_y_no_primos = []

def super_funcion():
    super_funcion = []
    while True:
        try:
            num = input('Presion "c" para terminar, Ingrese un numero:  ')
            if num == "c":
                return super_funcion
            else:
                num = int(num)
                num1 = 0
                num2 = 1
                secuencia = 0
                fibonacci = False
                while secuencia <= num:
                    secuencia = num1 + num2
                    num1 = num2
                    num2 = secuencia
                    if secuencia == num:
                        fibonacci = True
                condicion = 1
                divisores = 0
                primo = False
                while condicion <= num:
                    if num % condicion == 0:
                        divisores += 1
                    condicion += 1
                if divisores == 2:
                    primo = True
                if not primo and not fibonacci:
                    numeros_no_fibonaccis_y_no_primos.append(num)
        except ValueError:
            print('Valor invalido, Ingrese un valor valido')

super_funcion()

print("Los numeros que no son primos ni fibonaccis son:  ", numeros_no_fibonaccis_y_no_primos)