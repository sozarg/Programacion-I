#Mateo Terrile DIV 111
#1
# Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
# Por ej:
# cadena = “murcielaguito”

def determinar_cantidad_vocales(cadena: str) -> dict:
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for caracter in cadena:
        if caracter in conteo_vocales:  
            conteo_vocales[caracter] += 1  
    
    return conteo_vocales

cadena = "murcielaguito"
resultado = determinar_cantidad_vocales(cadena)
print(resultado)
