#M = n*(n2 + 1)/2

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]
def es_cuadrado_magico(matriz:list)-> list:
    n = len(matriz)
    constante_magica = n*(n**2 + 1)/2

    for fila in matriz:
        suma_fila = 0
        for valor in fila:
            suma_fila += valor
        if suma_fila != constante_magica:
            return False

    for columna in range(len(matriz)):
        suma_columna = 0
        for fila in range(len(matriz)):
            suma_columna += matriz[fila][columna]
        if suma_columna != constante_magica:
            return False

    return True

resultado = es_cuadrado_magico(matriz)
print(resultado)