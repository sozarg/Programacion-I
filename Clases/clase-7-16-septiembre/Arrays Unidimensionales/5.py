#Alumno: Terrile Mateo
#División 111
#5
#Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def buscar_posiciones_maximas(mi_lista: list) -> list:
    bandera_maximo = True
    maximo = 0
    cantidad_maximos = 0
    posiciones = [-1] * len(mi_lista)

    for i in range(len(mi_lista)):
        if mi_lista[i] > maximo or bandera_maximo == True:
            maximo = mi_lista[i]
            bandera_maximo = False

    for i in range(len(mi_lista)):
        if mi_lista[i] == maximo:
            posiciones[cantidad_maximos] = i
            cantidad_maximos += 1
    
    return posiciones[:cantidad_maximos]


numeros_enteros = [5, 3, -2, 8, 7]
posiciones_maximo = buscar_posiciones_maximas(numeros_enteros)

for p in posiciones_maximo:
    print(f"El valor máximo se encuentra en la posición {p + 1}")
