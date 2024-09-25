#Alumno: Terrile Mateo
#División 111
#8
#Crear una función que (utilizando la función del punto 11 de la guía de For), muestre todos los números primos comprendidos entre entre la unidad 
# y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados.

def primos_encontrados(numero):
    contador_primos = 0
    for x in range(2, numero + 1):
        es_primo = True

        for i in range(2, x):
            if x % i == 0:
                es_primo = False
                break

        if es_primo == True:
            print(f"{x} Es primo")
            contador_primos += 1
    return contador_primos

numero = int(input("Ingrese un numero: "))
resultado = primos_encontrados(numero)
print(f"Se encontraron {resultado} numeros primos")