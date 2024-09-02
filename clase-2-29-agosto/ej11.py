#Alumno: Terrile Mateo
#División 111
#11 Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.
contador_primos = 0

numero = input("Ingrese un numero:")
numero = int(numero)

for x in range(2, numero + 1):
    es_primo = True
    
    for i in range(2, x):
        if x % i == 0:
            es_primo = False
            break

    if es_primo == True:
        print(f"{x} Es primo")
        contador_primos += 1
        
print(f"Se encontraron {contador_primos} numeros primos")