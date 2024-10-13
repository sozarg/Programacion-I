# Una empresa se dedica al almacenamiento y posterior distribución de
# cereales en el interior del país. Para ello cuentan con 20 depósitos en CABA,
# que generalmente se encuentran en las inmediaciones de las estaciones del
# ferrocarril.

# Los depósitos pueden almacenar 4 tipos diferentes de cereales: maíz, trigo,
# cebada y centeno.

# La oficina central, recibe mensualmente una planilla de existencias donde se
# indican las existencias de cada cereal para cada depósito.

# Realizar un menú de opciones:
# 1. Obtener existencias: para ello deberá crear una función que cargue la
# existencia de cada grano en todos los depósitos. Los valores estarán
# comprendidos entre 5000 Kg y 20000 Kg.

# 2. Calcular por cada depósito la cantidad total de kilos almacenados entre
# todos los cereales.

# 3. Nombre del cereal que almaceno menos kilos en cada depósito.

# 4. Máxima cantidad de kilos almacenados de cada cereal.

# 5. Depósito con mayor recaudación, teniendo en cuenta que disponemos
# de un vector con los valores por kilo de cada tipo de cereal.

# 6. Cantidad de depósitos que hayan almacenado más de 50000 kilos
# entre los 4 cereales.

# 7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados.
# Además mostrar el nombre del cereal con el máximo porcentaje.

# 8. Generar un informe con la recaudación de cada depósito, ordenada de
# mayor a menor.
from os import system
    #j tipo_cereal
    #i depositos
    #[Maiz], [Trigo], [Cebada, [Centeno]

def cargar_existencias(matriz_existencia:list, mensaje:str, mensaje_error:str, minimo:int, maximo:int) -> None:
    for i in range(len(matriz_existencia)):
        for j in range(len(matriz_existencia[0])):
            while True:
                valor = int(input(mensaje))
                
                if validar_valor(valor,minimo,maximo):
                    matriz_existencia[i][j] = valor
                    break
                else:
                    print(mensaje_error)
    
def validar_valor(valor:int, minimo:int, maximo:int) -> bool:
    return valor >= minimo and valor <= maximo

def mostrar_matriz(matriz_existencia:list)->None:
    for i in range(len(matriz_existencia)):
        for j in range(len(matriz_existencia[0])):
            print(matriz_existencia[i][j], end="\t")
        print()

def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz= []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def suma_kilos_existencias(matriz_existencia:list) -> None:
    suma_valores = 0
    for i in range(len(matriz_existencia)):
        for j in range(len(matriz_existencia[0])):
            suma_valores += matriz_existencia[i][j]
    print(f"\nSuma total: {suma_valores}")

def cereal_menos_almacenado_por_deposito(matriz_existencia: list) -> None:
    nombre_cereales = ["Maiz", "Trigo", "Cebada", "Centeno"]
    for i in range(len(matriz_existencia)):
        menor_valor = matriz_existencia[i][0]
        menor_indice = 0
        for j in range(1,len(matriz_existencia[i])):
            if matriz_existencia[i][j] < menor_valor:
                menor_valor = matriz_existencia[i][j]
                menor_indice = j
        menor_cereal = nombre_cereales[menor_indice]
        print(f"En el depósito {i + 1}, el cereal menos almacenado es: {menor_cereal}")
            
def mostrar_menu():
    while True:
        print("| Menú |")
        print("1. Obtener existencias")
        print("2. Cantidad total de kilos almacenados entre todos los cereales (por deposito)")
        print("3. Nombre del cereal que almaceno menos kilos en cada deposito")
        print("4. Maxima cantidad de kilos almacenados en cada cereal.")
        print("5. Deposito con mayor recaudacion")
        print("6. Cantidad de depositos que hayan almacenado mas de 5000 kilos entre los 4 cereales")
        print("7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados.")
        print("8. Generar un informe con la recaudacion de cada deposito")
        print("9. Salir del Menú")
        
        opcion = input("Señor, elija una opción: ")
        
        match opcion:
            case "1":
                matriz_existencias = crear_matriz(2, 4, 0)  # Crear la matriz para 2 depósitos y 4 tipos de cereales
                cargar_existencias(matriz_existencias, "Ingrese la cantidad de granos (entre 5000 y 20000 Kg):", "Valor no válido, inténtelo de nuevo.", 5000, 20000)
                mostrar_matriz(matriz_existencias)
                suma_kilos_existencias(matriz_existencias)
                cereal_menos_almacenado_por_deposito(matriz_existencias)
            #case "2":
                
            
            #case "3":
                
            #case "4":
            
            #case "5":
            
            #case "6":
                
            #case "7":
            
            #case "8":
            
            case "9":
                print("Señor, usted eligió salir del programa")
                break
            case _:
                print("Señor, esa opción no es valida.")

            
mostrar_menu()