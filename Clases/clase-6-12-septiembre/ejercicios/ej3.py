#Alumno: Terrile Mateo
#División 111
#3
#Realizar una función recursiva que permita realizar la suma de los dígitos de un número:
def sumar_digitos(numero: int)->int:
    if numero == 0:
        return 0
    else:
        return numero % 10 + sumar_digitos(numero // 10)

resultado = sumar_digitos(55)
print(resultado)
