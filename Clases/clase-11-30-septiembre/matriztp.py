matriz_legajos_choferes = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35]
]

def ingresar_legajo():
    legajo = int(input("Chofer, ingrese su numero de legajo: "))
    return legajo

def validacion_legajo(legajo, matriz_legajos_choferes):
    for fila in matriz_legajos_choferes:
        if legajo in fila:
            return True
    return False

def cargar_planilla():
    linea = int(input("Chofer, ingrese el numero de linea"))
    
def validacion_linea():
    while True:
        linea = int(input("Chofer, ingrese el numero de linea: "))
        if linea < 1 or linea > 3:
            return linea
        else:
            print("Chofer, la linea debe ser del 1 al 3")
        
def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1. Cargar planilla")
        print("2. Mostrar recaudación por coche y línea")
        print("3. Calcular y mostrar recaudación por línea")
        print("4. Calcular y mostrar recaudación por coche")
        print("5. Calcular y mostrar recaudación total")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
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
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, intenta nuevamente.")

mostrar_menu()