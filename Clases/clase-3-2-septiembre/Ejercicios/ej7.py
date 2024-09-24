#Alumno: Terrile Mateo
#División 111
#7
# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
def detectar_primos(numero:int) -> bool:
    es_primo = True
    if numero < 2:
        es_primo = False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False 
            break
    return es_primo
#MAIN

numero = int(input("Ingrese un numero: "))
resultado = detectar_primos(numero)
print(resultado)

