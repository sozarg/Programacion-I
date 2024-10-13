# cadena = "hola"
# letra = "a"
# orden = ord(letra)
# nueva_orden = orden - 32
# letra_mayuscula = chr(nueva_orden)
# print(letra_mayuscula)

cadena = "hola como esta la comision 111?"
cadena_mayuscula = ""
for i in range(len(cadena)):
    caracter = cadena[i]
    if caracter >= "a" and caracter <= "z":
        letra_mayuscula = chr(ord(cadena[i])-32)
    else:
        letra_mayuscula = caracter
        
    cadena_mayuscula += letra_mayuscula
    
print(cadena_mayuscula)