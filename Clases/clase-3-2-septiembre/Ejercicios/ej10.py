#Alumno: Terrile Mateo
#División 111
#10
# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def pedir_numero():
    numero = int(input("Ingrese un numero: "))    
    return numero

resultado = pedir_numero()
print(f"El numero es: {resultado}")