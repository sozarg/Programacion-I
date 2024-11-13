# Actividad
# Un cuadrado mágico es una matriz cuadrada en la que la suma de los números en cada fila, cada columna y cada diagonal principal es la misma. Esto se conoce como constante mágica del cuadrado.
# La misma se calcula: 
# M = n*(n2 + 1)/2
# Formalmente, un cuadrado mágico de orden n, es una matriz cuadrada de nxn donde los números enteros del 1 al n2  están dispuestos de tal manera que la suma de los números en cada fila, cada columna y cada diagonal principal es igual a la misma constante mágica.
# Deberán desarrollar un programa que determine si el cuadrado de valores ingresado por el usuario es o no un cuadrado mágico. Tener en cuenta todas las validaciones posibles.

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        filas = [valor_inicial] * cantidad_columnas
        matriz += [filas]
    return matriz

#secuencial
def cargar_matriz(matriz: list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Ingrese el valor en la posicion ({i}:{j})"))
    return matriz

def mostrar_matriz(matriz:list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()

def mostrar_primer_diagonal(matriz:list) -> list:
    for i in range(len(matriz)):
        print(matriz[i][i])
        for j in range(len(matriz[i])):
            print(matriz[i][i])

matriz = inicializar_matriz(3,3,0)
cargar_matriz(matriz)
mostrar_matriz(matriz)
mostrar_primer_diagonal(matriz)