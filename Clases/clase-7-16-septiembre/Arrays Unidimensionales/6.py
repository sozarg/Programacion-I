#Alumno: Terrile Mateo
#División 111
#6
#Escribir una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.

def reemplazar_nombres(lista_nombres: list, nombre_a_reemplazar: str, reemplazo: str) -> int:
    contador = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_a_reemplazar:
            lista_nombres[i] = reemplazo 
            contador += 1
    return contador

nombres = ["Juan", "María", "Juan", "Carlos", "Juan"]
reemplazos_realizados = reemplazar_nombres(nombres, "Juan", "Pedro")
print(f"Nombres después del reemplazo: {nombres}")
print(f"Cantidad de reemplazos: {reemplazos_realizados}")
