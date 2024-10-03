matriz = [
    [5,4,9,10],
    [9,8,7,15],
    [3,1,5,11]
    ]

for j in range(len(matriz[0])):
    for i in range(len(matriz)):
        print(matriz[i][j], end="\t")
    print()