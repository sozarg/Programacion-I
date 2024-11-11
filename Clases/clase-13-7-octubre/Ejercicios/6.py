#Mateo Terrile DIV 111
#6
#Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.

cadena = "El pan del panadero"
subcadena = "pan"

def contador_subcadenas(cadena:str, subcadena:str) -> int:
    contador = 0
    for caracter in cadena:
        if subcadena in cadena:
            contador +=1
    return contador

resultado = contador_subcadenas(cadena,subcadena)
print(resultado)