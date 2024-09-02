def sumar_1():
    un_numero = input("Ingrese un numero: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese otro numero: ")
    otro_numero = int(otro_numero)
    
    suma = un_numero + otro_numero
    
    print(f"La suma es: {suma}")
    
#MAIN - Entry point

sumar_1()
print("Realizamos otra suma...")
sumar_1()