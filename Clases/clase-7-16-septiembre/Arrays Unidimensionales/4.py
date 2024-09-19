#Alumno: Terrile Mateo
#División 111
#4
#Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

def buscar_posicion_maxima(mi_lista: list) -> int:
    bandera_maximo = True
    posicion = -1
    maximo = 0
    for i in range(len(mi_lista)):
        if mi_lista[i] > maximo or bandera_maximo == True :
            maximo = mi_lista[i]
            posicion = i
            bandera_maximo = False
            
    return posicion

numeros_enteros = [5, 3, -2, 7]
posicion_maximo = buscar_posicion_maxima(numeros_enteros) + 1
print(posicion_maximo)