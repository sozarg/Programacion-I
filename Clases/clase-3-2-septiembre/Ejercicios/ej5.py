#Alumno: Terrile Mateo
#División 111
#5
# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
def encontrar_maximo(primer_numero, segundo_numero, tercer_numero):
    if primer_numero > segundo_numero and primer_numero > tercer_numero:
        maximo = primer_numero
    elif segundo_numero > tercer_numero:
        maximo = segundo_numero
    else:
        maximo = tercer_numero
        
    return maximo

#MAIN

primer_numero = input("Ingrese el primer numero: ")
primer_numero = int(primer_numero)
segundo_numero = input("Ingrese el segundo numero: ")
segundo_numero = int(segundo_numero)
tercer_numero = input("Ingrese el tercer numero: ")
tercer_numero = int(tercer_numero)

resultado = encontrar_maximo(primer_numero, segundo_numero, tercer_numero)

print(resultado)

