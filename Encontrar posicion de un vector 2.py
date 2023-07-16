print("\n\n         ESTANTERIA DE MEDICAMENTOS          \n\n")

def medicamentos():
    medicamentos = []
    while True:
        agregar_medicamento = str(input("\nNombre del medicamento:   "))
        print('presione "0" para terminar')
        if agregar_medicamento == "0":
            return medicamentos
        else:
            medicamentos.append(agregar_medicamento)

medicamentos = medicamentos()

print(medicamentos)

print("\n   Buscar en estanteria  \n")
buscar = str(input("Ingrese el nombre del medicamento:  "))

for i in range(len(medicamentos)):
    if medicamentos[i] == buscar:
        print('El medicamento', buscar, 'se encuentra en el estante', i+1)