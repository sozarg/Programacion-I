#Mateo Terrile DIV 111
#3
#Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido.
def es_palindromo(cadena):
    caracteres_a_eliminar = " ,.;:-"

    cadena_limpia = ""
    for caracter in cadena:
        if caracter not in caracteres_a_eliminar:
            cadena_limpia += caracter.lower()

    cadena_invertida = ""
    for i in range(len(cadena_limpia) - 1, -1, -1):
        cadena_invertida += cadena_limpia[i]


    return cadena_limpia == cadena_invertida

cadena = "A ti, no, bonita"
if es_palindromo(cadena):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")