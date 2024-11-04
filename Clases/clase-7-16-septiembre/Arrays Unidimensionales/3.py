#Alumno: Terrile Mateo
#División 111
#3
#Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

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

lista_numeros = [6, 8, -4, 8, 2]

promedio_resultado = calcular_promedio(lista_numeros)
if promedio_resultado != None:
    print(promedio_resultado)
else:
    print("error: lista vacia o no hay nuimeros positivos")