#Alumno: Terrile Mateo
#División 111
#7 Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
numero = int(input("Ingrese un numero: "))
for i in range(numero, 51):
    if i % 2 == 0:
        print(i)