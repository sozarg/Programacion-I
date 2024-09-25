#Alumno: Terrile Mateo
#División 111
#9
# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. 
# La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

def tabla_multiplicacion(numero, inicio, fin):
    for multiplicador in range(inicio, fin + 1):
        total = numero * multiplicador
        print(f"| {numero} | X | {multiplicador} | RESULTADO: {total}")

# MAIN
numero = int(input("Ingrese un numero: "))
inicio = int(input("Ingrese el multiplicador inicial (si no elegis nada por defecto seria 1): ") or 1)
fin = int(input("Ingrese el multiplicador final (si no elegis nada por defecto seria 10): ") or 10)

resultado = tabla_multiplicacion(numero, inicio, fin)
