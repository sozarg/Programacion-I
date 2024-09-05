#Alumno: Terrile Mateo
#División 111
#1
# Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

def determinar_area(base, altura):
    area = base * altura
    return area

#MAIN

base = input("Ingrese la base: ")
base = int(base)
altura = input("Ingrese la altura: ")
altura = int(altura)

area = determinar_area(base, altura)

print(f"El area del rectangulo es: {area}")