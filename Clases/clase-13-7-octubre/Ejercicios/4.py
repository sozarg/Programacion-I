#Mateo Terrile DIV 111
#4
#Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos consecutivos.

cadena = "buenas tardes"

def suprimir_caracteres_repetidos(cadena: str) -> str:
    cadena_nueva = ""
    ultimo_caracter = None
    for caracter in cadena:
        if caracter != ultimo_caracter:
            cadena_nueva += caracter
            ultimo_caracter = caracter
    return cadena_nueva

cadena = "buuueeennaaasss"
resultado = suprimir_caracteres_repetidos(cadena)
print(resultado)
