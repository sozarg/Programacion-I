#Alumno: Terrile Mateo
#División 111
#9 Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.
cantidad_divisores = 0
numero = int(input("Ingrese un numero: "))
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
        cantidad_divisores += 1
print("Cantidad de divisores encontrados:", cantidad_divisores)