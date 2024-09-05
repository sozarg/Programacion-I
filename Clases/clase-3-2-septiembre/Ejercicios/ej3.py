#Alumno: Terrile Mateo
#División 111
#3
# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def verificar_paridad(paridad,mensaje_par,mensaje_impar):
    paridad = input(paridad)
    paridad = int(paridad)
    if paridad % 2 == 0:
        paridad = print(mensaje_par)
    else:
        paridad = print(mensaje_impar)
        

#MAIN

paridad= verificar_paridad("Ingrese un numero: ", "Es par", "Es impar")
