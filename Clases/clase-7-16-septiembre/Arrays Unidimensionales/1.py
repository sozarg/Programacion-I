#Alumno: Terrile Mateo
#División 111
#1
#Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.

def calcular_promedio(mi_lista: list) -> float:
    acumulador = 0
    promedio = None
    if len(mi_lista) != 0: 
        for i in range(len(mi_lista)):
            acumulador += mi_lista[i]
        promedio = acumulador / len(mi_lista)
        
    return promedio

lista_numeros = [6, 8, 6, 8, 7]

promedio_resultado = calcular_promedio(lista_numeros)
if promedio_resultado != None:
    print(promedio_resultado)
else:
    print("Error, lista vacia")
    