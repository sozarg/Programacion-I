#Mateo Terrile DIV 111
#6
#Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.

ejemplo="El pan del panadero"

def contar_subcadena(cadena:str, sub_cadena:str)->int | None:
    # palabras= cadena.lower() #Otra manera
    sub_palabras = sub_cadena.lower() #Esta linea se mantiene en otra manera
    palabras= cadena.lower().split(" ")
    contador=0
    for i in palabras:
        if sub_cadena in i:
            contador+=1

    # return palabras.count(sub_palabras) #Otra manera
    return contador

a=contar_subcadena(ejemplo, "pan")
print(a)