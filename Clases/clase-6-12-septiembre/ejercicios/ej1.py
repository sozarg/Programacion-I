#Alumno: Terrile Mateo
#División 111
#1
#Realizar una función recursiva que calcule la suma de los primeros números naturales:
def sumar_naturales(numero: int) -> int:
    if numero == 1:
        return 1
    else:
        return numero + sumar_naturales(numero - 1)

resultado = sumar_naturales(10)
print(resultado)
