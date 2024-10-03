matriz_legajos_choferes = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35]
]

matriz_recaudaciones = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def ingresar_legajo():
    legajo = int(input("Chofer, ingrese su numero de legajo: "))
    return legajo

def validacion_legajo(legajo, matriz_legajos_choferes):
    for fila in matriz_legajos_choferes:
        if legajo in fila:
            return True
    return False

def validacion_linea():
    while True:
        linea = int(input("Chofer, ingrese el numero de linea: "))
        if linea >= 1 and linea <= 3:
            return linea
        else:
            print("Chofer, las lineas son: 1/2/3")

def validacion_coche():
    while True:
        coche = int(input("Chofer, ingrese el numero de coche: "))
        if coche >= 1 and coche <= 5:
            return coche
        else:
            print("Chofer, solo existen 5 coches")

def validacion_recaudo():
    while True:
        recaudo = int(input("Chofer, ingrese el numero de recaudo: "))
        if recaudo >= 0:
            return recaudo
        else:
            print("Chofer, debe ingresar un recaudo real")

def cargar_planilla():
    legajo = ingresar_legajo()
    if not validacion_legajo(legajo, matriz_legajos_choferes):
        print("Chofer, su legajo no es valido")
        return

    while True:
        linea = validacion_linea()
        coche = validacion_coche()
        recaudo = validacion_recaudo()
        
        matriz_recaudaciones[linea-1][coche-1] += recaudo

        print(f"Recaudación registrada: Línea {linea}, Coche {coche}, Recaudo {recaudo}")
        continuar = input("Chofer, quiere ingresar otra recaudacion? (si/no): ")

        if continuar != 'si':
            break

def mostrar_recaudacion_por_coche_y_linea():
    print("\nRecaudaciones por coche y línea:")
    for i in range(len(matriz_recaudaciones)): #fila
        for j in range(len(matriz_recaudaciones[i])): #columna
            print(f"Línea {i+1}, Coche {j+1}: {matriz_recaudaciones[i][j]}", end="\t")
        print()
        
def mostrar_recaudacion_por_linea():
    print("\nRecaudación total por línea:")
    for i in range(len(matriz_recaudaciones)): #fila
        total_linea = 0
        for j in range(len(matriz_recaudaciones[i])): #columna
            total_linea += matriz_recaudaciones[i][j]
        print(f"Línea {i+1}: {total_linea}")

def mostrar_recaudacion_por_coche():
    print("\nRecaudación total por coche:")
    for j in range(len(matriz_recaudaciones[0])): #columna
        total_coche = 0
        for i in range(len(matriz_recaudaciones)): #fila
            total_coche += matriz_recaudaciones[i][j]
        print(f"Coche {j+1}: {total_coche}")
        
def mostrar_recaudacion_total():
    total = 0
    for i in range(len(matriz_recaudaciones)):  #fila
        for j in range(len(matriz_recaudaciones[i])):  #columna
            total += matriz_recaudaciones[i][j]
    print(f"\nRecaudación total: {total}")
    
def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1. Cargar planilla")
        print("2. Mostrar recaudación por coche y línea")
        print("3. Calcular y mostrar recaudación por línea")
        print("4. Calcular y mostrar recaudación por coche")
        print("5. Calcular y mostrar recaudación total")
        print("6. Salir")
        
        opcion = input("Chofer, elija una opcion: ")
        
        match opcion:
            case '1':
                cargar_planilla()
            case '2':
                mostrar_recaudacion_por_coche_y_linea()
            case '3':
                mostrar_recaudacion_por_linea()
            case '4':
                mostrar_recaudacion_por_coche()
            case '5':
                mostrar_recaudacion_total()
            case '6':
                print("Chofer, usted eligió salir del programa")
                break
            case _:
                print("Chofer, esa opcion no es valida")

mostrar_menu()
