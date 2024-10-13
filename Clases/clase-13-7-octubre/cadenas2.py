cadena_1 = "hola"
cadena_2 = "como estan"
cadena_3 = cadena_1 + ". " + cadena_2 #agrego punto y espacio
print(id(cadena_3))
print(cadena_3)
cadena_3 += "?"
print(cadena_3)

cadena_3 = f"{cadena_1}. {cadena_2}?"
print(cadena_3)

print("-"*10)

for i in range(70):
    print("-", end = "")