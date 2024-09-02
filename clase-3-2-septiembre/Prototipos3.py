def sumar_3():
    un_numero = input("Ingrese un numero: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese otro numero: ")
    otro_numero = int(otro_numero)
    
    suma = un_numero + otro_numero
    
    return suma
    
#MAIN - Entry point

resultado = sumar_3()
print(f"El resultado de la suma es: {resultado}")