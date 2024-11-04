#Alumno: Terrile Mateo
#División 111
#2
#Escribir una función parecida a la anterior, pero la misma deberá 
#calcular y devolver el promedio de los números positivos.

def calcular_promedio(mi_lista: list) -> float:
    acumulador = 0
    contador = 0
    promedio = None
    if len(mi_lista) > 0: 
        for i in range(len(mi_lista)):
            if mi_lista[i] > 0:
                acumulador += mi_lista[i]
                contador += 1
        if contador > 0:
            promedio = acumulador / contador
        
    return promedio

lista_numeros = [6, 8, -4, 8, 7]

promedio_resultado = calcular_promedio(lista_numeros)
if promedio_resultado != None:
    print(promedio_resultado)
else:
    print("error: lista vacia o no hay nuimeros positivos")