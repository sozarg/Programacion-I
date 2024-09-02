def sumar_4(un_numero, otro_numero, mensaje, tercer_numero = None):
    print(mensaje)
    suma = un_numero + otro_numero
    if tercer_numero != None:
        suma +=tercer_numero
    return suma

resultado = sumar_4(8,7, "Estoy sumando")
print(resultado)

resultado = sumar_4(8,7, "Estoy sumando")
print(resultado)

sumar_4(4,9,7)
