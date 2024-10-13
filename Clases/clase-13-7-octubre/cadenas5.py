cadena = "hola como esta la comision 111?"

def reemplazar_caracter(cadena: str, caracter_a_reemplazar: str, caracter_reemplazo) -> str:
    """_summary_

    Args:
        cadena (str): _description_
        caracter_a_reemplazar (str): _description_
        caracter_reemplazo (_type_): _description_

    Returns:
        str: _description_
    """
    cadena_reemplazada = ""
    for i in range(len(cadena)):
        caracter = cadena[i]
        if caracter == caracter_a_reemplazar:
            caracter = caracter_reemplazo
        
        cadena_reemplazada += caracter
    
    return cadena_reemplazada

cadena = "hola como esta la comision 111?"

cadena_nueva = reemplazar_caracter(cadena, "o", "*")
print(cadena_nueva)