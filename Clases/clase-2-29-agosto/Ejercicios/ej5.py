#Alumno: Terrile Mateo
#División 111
#5 Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
suma = 0
contador = 0
for i in range(10):
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        break
    suma += numero
    contador += 1 
    promedio = suma / contador
print(f"La suma de todos los numeros es {suma}")
print(f"El promedio de todos los numeros es {promedio}")