def sumar_2(un_numero, otro_numero): #Parametros formales
    suma = un_numero + otro_numero
    print(f"La suma es: {suma}")
    
#MAIN

un_numero = input("Ingrese un numero: ")
un_numero = int(un_numero)
otro_numero = input("Ingrese otro numero: ")
otro_numero = int(otro_numero)

sumar_2(un_numero, otro_numero) #Parametros actuales
sumar_2(7, 1) #Parametros Actuales