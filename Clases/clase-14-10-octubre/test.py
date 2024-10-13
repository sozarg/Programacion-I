# archivo: cereal_menos_almacenado.py

def cereal_menos_almacenado_por_deposito(matriz_existencia: list) -> None:
    nombre_cereales = ["Maiz", "Trigo", "Cebada", "Centeno"]
    
    for i in range(len(matriz_existencia)):  # Recorremos los depósitos
        menor_valor = matriz_existencia[i][0]
        menor_indice = 0
        
        # Buscamos el cereal con el menor valor
        for j in range(1, len(matriz_existencia[i])):
            if matriz_existencia[i][j] < menor_valor:
                menor_valor = matriz_existencia[i][j]
                menor_indice = j
        
        # Mostramos el cereal con menos cantidad en el depósito i
        print(f"En el depósito {i+1}, el cereal con menos kilos almacenados es {nombre_cereales[menor_indice]} con {menor_valor} kilos.")

def mostrar_matriz(matriz_existencia: list) -> None:
    print("\nMatriz de existencias (kilos de cereales por depósito):")
    for i in range(len(matriz_existencia)):
        for j in range(len(matriz_existencia[i])):
            print(f"{matriz_existencia[i][j]:>6}", end=" ")
        print()
# 4. Máxima cantidad de kilos almacenados de cada cereal.

# Recorre cada cereal (columna)
def maxima_cantidad_kilos_por_cereal(matriz_existencia: list) -> None:
    nombre_cereales = ["Maiz", "Trigo", "Cebada", "Centeno"]
    for j in range(len(matriz_existencia[0])):
        maxima_cantidad = 0
        # Recorre cada deposito (fila)
        for i in range(len(matriz_existencia)):
            if matriz_existencia[i][j] > maxima_cantidad:
                maxima_cantidad = matriz_existencia[i][j]
        print(f"Máxima cantidad de kilos almacenados de cada cereal: {maxima_cantidad} de {nombre_cereales[j]}")

# Matriz con las existencias de cereales por depósito (2 depósitos y 4 cereales en este ejemplo)
matriz_existencias = [
    [8000, 10000, 6000, 15000],  # Depósito 1
    [12000, 9000, 20000, 11000],  # Depósito 2
]

# Mostrar la matriz de existencias
mostrar_matriz(matriz_existencias)

# Llamamos a la función para mostrar el cereal con menos kilos por depósito
cereal_menos_almacenado_por_deposito(matriz_existencias)
maxima_cantidad_kilos_por_cereal(matriz_existencias)
