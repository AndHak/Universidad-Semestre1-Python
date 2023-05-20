num = int(input("Ingresa un número para generar su tabla de multiplicar: "))
print("Tabla de multiplicar del ", num)

multiplicador = 1

while multiplicador <= 10:
    resultado = num * multiplicador
    print(num,"x",multiplicador,"=",resultado)
    
    multiplicador = multiplicador + 1
