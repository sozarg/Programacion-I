# Desarrolle una función que reciba una cadena de caracteres y verifique si todos los caracteres en la cadena son números romanos, es decir, si pertenecen al conjunto de símbolos: 
#     I, V, X, L, C, D, y M. Si todos los caracteres son números romanos, la función debe devolver True. Si alguno de los caracteres no es un número romano, la función debe devolver False.

# La función debe estar debidamente documentada y adornada.

# Entregar el ejercicio por online GDB

romanos = "IVXLCDM"
cadena = "IVML"
def verificar_romanos(romanos:list, cadena:str) -> bool:
    """
    Verifica si todos los caracteres son numeros romanos

    Args:
        romanos (list): list
        cadena (str): _description_

    Returns:
        bool: _description_
    """
    for i in range(len(cadena)):
        if cadena[i] not in romanos:
            return False
    return True

resultado = verificar_romanos(romanos,cadena)
print(resultado)