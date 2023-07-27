# Función para imprimir una línea de adornos
def print_separator():
    print("------------------------------------------------------------------------------------")

# Función para imprimir encabezados de la tabla puestos en orden descendente por promedio
def print_headers():
    print("Puestos   Código     Nombre                 Nota 1   Nota 2   Nota 3   Nota Final")
    print_separator()

# Función para imprimir encabezados de aprobados y reprobados
def print_headers2():
    print("Código     Nombre                 Nota 1   Nota 2   Nota 3   Nota Final")
    print_separator()

# Función para agregar estudiantes con sus códigos
def agregar_estudiante():
    print("Agregar estudiantes:")
    while True:
        agregar = input("¿Desea agregar un estudiante? (s/n): ")
        if agregar.lower() == "n":
            break
        elif agregar.lower() == "s":
            try:
                estudiante = input("Ingrese el nombre del estudiante: ")
                codigo = input("Ingrese el código del estudiante: ")
                codigo_de_estudiantes.append(codigo)
                nombre_de_estudiantes.append(estudiante)
            except ValueError:
                print("Código o nombre del estudiante no válido")
        else:
            print("Valor no válido, escoja s/n (sí/no)")

# Llamar la función para agregar estudiantes antes de ejecutar la siguiente función
codigo_de_estudiantes = []
nombre_de_estudiantes = []
agregar_estudiante()

# Diccionario para almacenar las notas de cada estudiante, es más fácil que usar vectores o matrices
notas_de_estudiantes = {}

# Función para agregar las notas de los estudiantes
def agregarnotas():
    print("\nAgregar notas de estudiantes:")
    while True:
        ingresar_notas = input("¿Desea ingresar notas? (s/n): ")
        if ingresar_notas.lower() == "n":
            break
        elif ingresar_notas.lower() == "s":
            print("Estudiantes disponibles con sus respectivos códigos:")
            # Se usa zip para iterar simultáneamente sobre dos listas (códigos y nombres)
            for codigo, nombre in zip(codigo_de_estudiantes, nombre_de_estudiantes):
                print(f"Código: {codigo} | Nombre: {nombre}")
            
            elegir_estudiante = input("Digite el código del estudiante: ")
            if elegir_estudiante in codigo_de_estudiantes:
                print(f"Estudiante escogido: {nombre_de_estudiantes[codigo_de_estudiantes.index(elegir_estudiante)]}")
                print("Las notas van desde 0.0 hasta 5.0 ")
                condicion_nota_minima = 0
                condicion_nota_maxima = 5
                try:
                    nota1 = float(input("Ingrese la primera nota (30% de la nota final): "))
                    if nota1 <= condicion_nota_maxima and nota1 >= condicion_nota_minima:
                        nota2 = float(input("Ingrese la segunda nota (30% de la nota final): "))
                        if nota2 <= condicion_nota_maxima and nota2 >= condicion_nota_minima:
                            nota3 = float(input("Ingrese la tercera nota (40% de la nota final): "))
                            if nota3 <= condicion_nota_maxima and nota3 >= condicion_nota_minima:
                                # Guardar las notas en el diccionario con el código del estudiante como clave
                                notas_de_estudiantes[elegir_estudiante] = [nota1, nota2, nota3]
                            else:
                                print("Nota no válida")
                        else:
                            print("Nota no válida")
                    else:
                        print("Nota no válida")
                except ValueError:
                    print("Nota no válida")
            else:
                print("Código de estudiante no existe")
        else:
            print("Valor no válido, escoja s/n (sí/no)")

# Llamar a la función para agregar las notas de los estudiantes
agregarnotas()

# Ordenar los estudiantes por su promedio (mayor a menor) utilizando el algoritmo de Bubble Sort que es fácil e intuitivo
# Además, se usa .items y list para obtener una lista de tuplas con los códigos y las notas de cada estudiante
lista_estudiantes = list(notas_de_estudiantes.items())
n = len(lista_estudiantes)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        promedio1 = lista_estudiantes[j][1][0] * 0.3 + lista_estudiantes[j][1][1] * 0.3 + lista_estudiantes[j][1][2] * 0.4
        promedio2 = lista_estudiantes[j + 1][1][0] * 0.3 + lista_estudiantes[j + 1][1][1] * 0.3 + lista_estudiantes[j + 1][1][2] * 0.4
        if promedio1 < promedio2:
            lista_estudiantes[j], lista_estudiantes[j + 1] = lista_estudiantes[j + 1], lista_estudiantes[j]

# Imprimir los resultados ordenados por promedio (mayor a menor)
print("\nResultados:")
print_separator()
print("Puestos de los estudiantes:")
print_headers()
# Se usa enumerate y start=1 para obtener el puesto de cada estudiante
for puesto, (codigo, notas) in enumerate(lista_estudiantes, start=1):
    # Se usa index para obtener el nombre del estudiante a partir del código
    nombre_estudiante = nombre_de_estudiantes[codigo_de_estudiantes.index(codigo)]
    promedio = (notas[0] * 0.3 + notas[1] * 0.3 + notas[2] * 0.4)
    # Se utilizan format strings (f-strings) para formatear y alinear los datos en la tabla
    print(f"{puesto:<12}{codigo:<10}{nombre_estudiante:<24}{notas[0]:<9.2f}{notas[1]:<9.2f}{notas[2]:<9.2f}{promedio:<10.2f}")
print_separator()

# Calcular el promedio de la clase, la nota mayor y la nota menor
suma_promedios = 0
nota_mayor = 0
nota_menor = 5
codigo_nota_mayor = ""
nombre_nota_mayor = ""
codigo_nota_menor = ""
nombre_nota_menor = ""

for codigo, notas in notas_de_estudiantes.items():
    promedio_estudiante = notas[0] * 0.3 + notas[1] * 0.3 + notas[2] * 0.4
    suma_promedios += promedio_estudiante
    
    # Iterar sobre las notas de cada estudiante para encontrar la nota mayor y menor
    for nota in notas:
        if nota < nota_menor:
            nota_menor = nota
            codigo_nota_menor = codigo
            nombre_nota_menor = nombre_de_estudiantes[codigo_de_estudiantes.index(codigo)]
        if nota > nota_mayor:
            nota_mayor = nota
            codigo_nota_mayor = codigo
            nombre_nota_mayor = nombre_de_estudiantes[codigo_de_estudiantes.index(codigo)]

promedio_clase = suma_promedios / len(notas_de_estudiantes)

# Imprimir los resultados estadísticos
print("\nResultados estadísticos:")
print_separator()
print(f"Promedio de la clase: {promedio_clase:.2f}")
print(f"Nota más alta: {nota_mayor:.2f} | Código del estudiante: {codigo_nota_mayor} | Nombre del estudiante: {nombre_nota_mayor}")
print(f"Nota más baja: {nota_menor:.2f} | Código del estudiante: {codigo_nota_menor} | Nombre del estudiante: {nombre_nota_menor}")
print_separator()

# Obtener los estudiantes aprobados (promedio >= 3) y reprobados (promedio < 3)
estudiantes_aprobados = []
estudiantes_reprobados = []

for codigo, notas in notas_de_estudiantes.items():
    promedio_estudiante = notas[0] * 0.3 + notas[1] * 0.3 + notas[2] * 0.4
    if promedio_estudiante >= 3:
        estudiantes_aprobados.append((codigo, notas))
    else:
        estudiantes_reprobados.append((codigo, notas))

# Imprimir los estudiantes que aprobaron
print("\nEstudiantes que aprobaron:")
print_headers2()
for codigo, notas in estudiantes_aprobados:
    nombre_estudiante = nombre_de_estudiantes[codigo_de_estudiantes.index(codigo)]
    promedio = (notas[0] * 0.3 + notas[1] * 0.3 + notas[2] * 0.4)
    print(f"{codigo:<12}{nombre_estudiante:<23}{notas[0]:<9.2f}{notas[1]:<9.2f}{notas[2]:<12.2f}{promedio:<10.2f}")
print_separator()

# Imprimir los estudiantes que reprobaron
print("\nEstudiantes que reprobaron:")
print_headers2()
for codigo, notas in estudiantes_reprobados:
    nombre_estudiante = nombre_de_estudiantes[codigo_de_estudiantes.index(codigo)]
    promedio = (notas[0] * 0.3 + notas[1] * 0.3 + notas[2] * 0.4)
    print(f"{codigo:<12}{nombre_estudiante:<23}{notas[0]:<9.2f}{notas[1]:<9.2f}{notas[2]:<12.2f}{promedio:<10.2f}")
print_separator()