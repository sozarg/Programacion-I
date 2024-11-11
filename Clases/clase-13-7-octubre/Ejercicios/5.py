#Mateo Terrile DIV 111
#5
#Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma

cadena = "buen dia"

def suprimir_vocales(cadena:str) -> str:
    vocales = "aeiou"
    cadena_nueva = ""
    for caracter in cadena:
        if caracter not in vocales:
            cadena_nueva += caracter
    return cadena_nueva

resultado = suprimir_vocales(cadena)
print(resultado)