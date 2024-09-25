#Alumno: Terrile Mateo
#División 111
#11
# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def pedir_numero():
    numero = float(input("Ingrese un numero: "))    
    return numero

resultado = pedir_numero()
print(f"El numero es: {resultado}")