#Alumno: Terrile Mateo
#División 111
#6
# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos
# y devolver el resultado.

def calcular_potencia(base, exponente):
    potencia = base ** exponente
    return potencia

#MAIN

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = calcular_potencia(base, exponente)
print(resultado)