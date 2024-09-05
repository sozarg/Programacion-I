#Alumno: Terrile Mateo
#División 111
#4 Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:
numero = int(input("Ingrese un numero: "))
for i in range(0, 11):
    tabla = numero * i
    print(f"{numero} x {i} = {tabla}")
