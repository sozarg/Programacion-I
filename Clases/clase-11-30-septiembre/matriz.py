matriz = [
    [5,9,4,2],
    [5,9,7,3],
    [1,0,3,6],
    [7,5,2,1],
    [1,1,7,3]]

for i in range(len(matriz)):#filas
    for j in range(len(matriz[i])):#columnas
        print(matriz[i][j], end="\t")
    print()

print("-"*15)
for j in range(len(matriz[0])):#columnas
    for i in range(len(matriz)):#filas
        print(matriz[i][j], end="\t")
    print()