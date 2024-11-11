#Mateo Terrile DIV 111
#2
#Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera ocurrencia de dicho caracter, o -1 en caso de que no esté.

def encontrar_primera_ocurrencia(cadena: str, caracter:str) -> int:
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i
    return -1
resultado = encontrar_primera_ocurrencia("hola","o")
print(resultado)