#Alumno: Terrile Mateo
#División 111
#2
# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def determinar_area(radio):
    area = 3.1416 * (radio ** 2)
    return area

#MAIN

radio = float(input("Ingrese la radio: "))

area = determinar_area(radio)

print(f"El area del circulo: {area}")