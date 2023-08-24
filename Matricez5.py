granja_A = [[10,22,33,45],
            [11,12,12,13],
            [14,15,77,43]]
granja_B = [[66,44,22,55],
            [1,2,3,4],
            [4,6,5,7]]

def sumar_granjas(m1,m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] + m2[i][j])
        return m3
    else:
        return None
    
c = sumar_granjas(granja_A, granja_B)

if c == None:
    print("No se pueden sumar")
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")


