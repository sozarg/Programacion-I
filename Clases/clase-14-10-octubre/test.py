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
def maxima_cantidad_kilos_por_cereal(matriz_existencia:list) -> None:
    nombre_cereales = ["Maiz", "Trigo", "Cebada", "Centeno"]
    for j in range(len(matriz_existencia[0])):
        kilos_almacenados_por_cereal = 0
        kilos_almacenados_por_cereal = matriz_existencia[0][j]
        for i in range(len(matriz_existencia)):
            if matriz_existencia[i][j] > kilos_almacenados_por_cereal:
                kilos_almacenados_por_cereal = matriz_existencia[i][j]
        print(f"Cereal: {nombre_cereales[j]} | Maxima cantidad de kilos almacenados: {kilos_almacenados_por_cereal}")

def deposito_con_mayor_recaudacion(matriz_existencia:list) -> None:
    deposito_mas_alto = 0
    contador_depositos = 0
    for i in range(len(matriz_existencia)):
        acumulador_depositos = 0
        for j in range(len(matriz_existencia[i])):
            acumulador_depositos += matriz_existencia[i][j]
            if acumulador_depositos > deposito_mas_alto:
                deposito_mas_alto = acumulador_depositos
                contador_depositos = i + 1
    print(f"El deposito con mayor recaudacion es el numero {contador_depositos }con {deposito_mas_alto}kg")

#Cantidad de depositos que hayan almacenado mas de 50000 kilos entre los 4 cereales
def depositos_entre_los_cereales(matriz_existencia:list) -> None:
    contador_depositos = 0
    for i in range(len(matriz_existencia)):
        deposito_cereal = 0
        for j in range(len(matriz_existencia[i])):
            deposito_cereal += matriz_existencia[i][j]
        if deposito_cereal > 50000:
            contador_depositos += 1
            print(f"El deposito numero {i + 1} cuenta con mas de 50.0000kg entre los 4 cereales")
    print(f"La cantidad de depositos superior a 50.000kg es de: {contador_depositos} depositos")
        
def porcentaje_kilos_cereal(matriz_existencia: list) -> None:
    nombre_cereales = ["Maiz", "Trigo", "Cebada", "Centeno"]
    total_kilos = 0
    porcentaje_final = 0
    
    for i in range(len(matriz_existencia)):
        for j in range (len(matriz_existencia[i])):
            total_kilos += matriz_existencia[i][j]

    for j in range(len(matriz_existencia[0])):
        acumulador_depositos = 0
        for i in range(len(matriz_existencia)):
            acumulador_depositos += matriz_existencia[i][j]
        if total_kilos > 0:
            porcentaje_final = (acumulador_depositos / total_kilos) * 100
            print(f"{nombre_cereales[j]} | Porcentaje: {porcentaje_final:.2f}%")
        else: 
            print(f"Error, vuelva a intentarlo")

#Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor.
# def informe_por_deposito(matriz_existencias: list) -> None:
#     recaudaciones = [0] * len(matriz_existencias)  # Inicializar la lista con ceros

#     for i in range(len(matriz_existencias)):
#         acumulador_por_fila = 0
#         for j in range(len(matriz_existencias[i])):
#             acumulador_por_fila += matriz_existencias[i][j]
#         recaudaciones[i] = acumulador_por_fila  # Asignar el total a la lista en la posición i
#         print(f"dee {recaudaciones}")
#     # Ordenamiento manual de mayor a menor (algoritmo de burbuja)
#     for i in range(len(recaudaciones)):
#         for j in range(len(recaudaciones) - 1 - i):
#             if recaudaciones[j] < recaudaciones[j + 1]:  # Cambiar el orden a mayor que
#                 # Intercambiar
#                 recaudaciones[j], recaudaciones[j + 1] = recaudaciones[j + 1], recaudaciones[j]
#     print(f"{recaudaciones}")

def informe_por_deposito(matriz_existencias: list) -> None:
    # Inicializar la lista de recaudaciones como una lista de tuplas con números de depósito y kilos en 0
    recaudaciones = [0] * len(matriz_existencias)
    
    # Calcular la cantidad total de kilos por depósito
    for i in range(len(matriz_existencias)):
        acumulador_por_fila = 0
        for j in range(len(matriz_existencias[i])):
            acumulador_por_fila += matriz_existencias[i][j]
        # Actualizar la tupla en la lista recaudaciones
        recaudaciones[i] = (i + 1, acumulador_por_fila)  # Guardar el número de depósito y la recaudación
        print(f"Total de kilos en depósito {i + 1}: {acumulador_por_fila}")

    # Ordenamiento manual de mayor a menor usando el algoritmo de burbuja sin usar métodos de listas
    for i in range(len(recaudaciones)):
        for j in range(len(recaudaciones) - 1 - i):
            if recaudaciones[j][1] < recaudaciones[j + 1][1]:
                # Intercambiar las tuplas completas para mantener el número de depósito y el total juntos
                temp = recaudaciones[j]
                recaudaciones[j] = recaudaciones[j + 1]
                recaudaciones[j + 1] = temp

    # Imprimir la lista de recaudaciones ordenada
    print("\nRecaudaciones por depósito ordenadas de mayor a menor:")
    for i in range(len(recaudaciones)):
        print(f"Depósito {recaudaciones[i][0]}: {recaudaciones[i][1]} Kg")

matriz_existencias = [
    [5000, 5000, 5000, 5000],  # Depósito 1
    [5000, 6000, 7000, 600],  # Depósito 2
    [8000, 10000, 66000, 15000],  # Depósito 3
    [12000, 18000, 20000, 11000],  # Depósito 4
]

# Mostrar la matriz de existencias
mostrar_matriz(matriz_existencias)

# Llamamos a la función para mostrar el cereal con menos kilos por depósito
cereal_menos_almacenado_por_deposito(matriz_existencias)
maxima_cantidad_kilos_por_cereal(matriz_existencias)
deposito_con_mayor_recaudacion(matriz_existencias)
depositos_entre_los_cereales(matriz_existencias)
porcentaje_kilos_cereal(matriz_existencias)
informe_por_deposito(matriz_existencias)

