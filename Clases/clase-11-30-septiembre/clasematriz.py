def acumular_pares_matriz(matriz: list) -> int:
    acumulador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] % 2 == 0:
                acumulador += matriz[i][j]
    return acumulador

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

def cargar_matriz(matriz: list)-> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = int(input(f"ingrese un numero: fila [{i}]- Columna[{j}] "))

matriz = crear_matriz(3,4,None)
mostrar_matriz(matriz)
print("-"*10)
cargar_matriz(matriz)
mostrar_matriz(matriz)
acumulador_pares = acumular_pares_matriz(matriz)
print(f" el acumulador de pares es {acumulador_pares}")