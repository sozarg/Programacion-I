#Alumno: Terrile Mateo
#División 111
#2
#Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base:int, exponente: int)-> int:
    if exponente == 0:
        return 1
    else:
        if exponente > 0:
            return base * calcular_potencia(base, exponente -1)

resultado = calcular_potencia(2,4)
print(resultado)