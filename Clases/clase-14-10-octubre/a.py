def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial: any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def validar_valorr(valor:int,, minimo macximo)