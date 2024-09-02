#Alumno: Terrile Mateo
#División 111
#10 Ingresar un número. Determinar si el número es primo o no.

numero = int(input("Ingrese un número: "))
es_primo = True 

if numero < 2:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False 
            break

if es_primo == True:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
