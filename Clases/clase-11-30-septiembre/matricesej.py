# Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
# Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
# Menú:
# Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). Si el chofer existe cargará la recaudación del viaje indicando
# línea y coche (no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validados. 
# Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). Cada coche de cada línea puede tener varias recaudaciones diarias.
# Mostrar la recaudación de cada coche y línea (mostrar la matriz).
# Calcular y mostrar recaudación por línea.
# Calcular y mostrar recaudación por coche.
# Calcular y mostrar la recaudación total.
# Salir.
# Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y verificación de existencia de legajo, cálculos, etc.
# Inputs
# 1 nro legajo
# 2 si esta ok
# 2.1 pido la linea y el coche valido
# 2.2 pido la recaudacion

def pedir_legajo():
    legajo = int(input("Ingrese su numero de legajo: "))
    return legajo

def validar_legajo(legajo, matriz_legajos):
    for fila in matriz_legajos:
        if legajo in fila:
            return True
    return False

def pedir_linea_y_coche():
    linea = int(input("Ingrese el numero de linea (1 a 3): "))
    coche = int(input("Ingrese el numero de coche (1 a 5): "))
    return linea, coche

def validar_linea_y_coche(linea, coche):
    if 1 <= linea <= 3 and 1 <= coche <= 5:
        return True
    return False

def cargar_recaudacion(matriz_recaudaciones, linea, coche, recaudacion):
    matriz_recaudaciones[linea-1][coche-1].append(recaudacion)


def recaudacion_por_linea(matriz_recaudaciones):
    for i in range(3):  # 3 líneas
        total_linea = 0
        for j in range(5):  # 5 coches por línea
            total_linea += sum(matriz_recaudaciones[i][j])  # Sumar las recaudaciones de todos los coches
        print(f"Recaudación total de la línea {i + 1}: {total_linea}")
        
def recaudacion_por_coche(matriz_recaudaciones):
    for i in range(3):  # 3 líneas
        for j in range(5):  # 5 coches por línea
            total_coche = sum(matriz_recaudaciones[i][j])
            print(f"Recaudación del coche {j + 1} de la línea {i + 1}: {total_coche}")

def recaudacion_total(matriz_recaudaciones):
    total = 0
    for i in range(3):
        for j in range(5):
            total += sum(matriz_recaudaciones[i][j])
    print(f"Recaudación total de la empresa: {total}")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Cargar planilla")
    print("2. Mostrar recaudación por coche")
    print("3. Mostrar recaudación por línea")
    print("4. Mostrar recaudación total")
    print("5. Otra opción (si la hay)")
    print("6. Salir del sistema")
    return int(input("Seleccione una opción: "))

def flujo_principal():
    # Matriz de legajos (ejemplo con números aleatorios)
    matriz_legajos = [
        [101, 102, 103, 104, 105],
        [106, 107, 108, 109, 110],
        [111, 112, 113, 114, 115]
    ]
    
    # Matriz de recaudaciones (vacía al inicio, se irá llenando con listas)
    matriz_recaudaciones = [[[] for _ in range(5)] for _ in range(3)]

    while True:
        opcion = mostrar_menu()
        
        if opcion == 1:
            legajo = pedir_legajo()
            if validar_legajo(legajo, matriz_legajos):
                linea, coche = pedir_linea_y_coche()
                if validar_linea_y_coche(linea, coche):
                    recaudacion = float(input("Ingrese el monto de la recaudación: "))
                    cargar_recaudacion(matriz_recaudaciones, linea, coche, recaudacion)
                    print("Recaudación cargada exitosamente.")
                else:
                    print("Línea o coche no válidos.")
            else:
                print("Legajo no válido.")
        
        elif opcion == 2:
            recaudacion_por_coche(matriz_recaudaciones)
        
        elif opcion == 3:
            recaudacion_por_linea(matriz_recaudaciones)
        
        elif opcion == 4:
            recaudacion_total(matriz_recaudaciones)
        
        elif opcion == 5:
            print("Otra opción, si aplica.")
        
        elif opcion == 6:
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el flujo principal
flujo_principal()
