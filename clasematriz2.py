def mostrar_matriz(matriz:list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end="\t")
        print()
        
def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz= []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def sumar_matrices(primer_matriz: list, segunda_matriz: list) -> list:
    resultado = crear_matriz(len(primer_matriz), len(primer_matriz[0]), None)
    for i in range(len(resultado)):
        for j in range(len(resultado[0])):
            resultado[i][j] = primer_matriz[i][j] + segunda_matriz[i][j]
    return resultado

matriz_a = [
    [4,8],
    [3,9],
    [2,1]
]

matriz_b = [
    [2,3],
    [6,3],
    [7,9]
]

suma = sumar_matrices(matriz_a, matriz_b)
mostrar_matriz(suma)