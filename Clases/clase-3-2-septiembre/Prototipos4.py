def sumar_4(un_numero, otro_numero):
    suma = un_numero + otro_numero
    return suma
# lo mas optimo

#MAIN

suma = sumar_4(3,8)
print(suma)

un_numero = input("Ingrese un numero: ")
un_numero = int(un_numero)
otro_numero = input("Ingrese otro numero: ")
otro_numero = int(otro_numero)

resultado = sumar_4(un_numero, otro_numero)

print(resultado)