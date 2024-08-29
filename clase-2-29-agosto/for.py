# rango = range(5,10)
# print(list(rango))

# rango = range(0,10,3)
# print(list(rango))

# rango = range(10,0,-1)
# print(list(rango))

# for i in range(5):
#     print(i)

# lista = ["Azul", "Amarillo", "Rojo"]
# for color in lista:
#     print(color)

# acumulador = 0
# for i in range(5):
#     numero = input("Ingrese un numero: ")
#     numero = int(numero)
#     print(type(numero))
#     acumulador +=numero

# print(acumulador)

# #Ingresar 20 numeros hasta encontrarme con un multiplo de 5

# for i in range(5):
#     numero = input("Ingrese un numero: ")
#     numero = int(numero)
#     if numero % 5 == 0:
#         break
#     print (numero)

#Ingresar hasta 10 numeros solo mostrar los pares
# for i in range(10):
#     numero = input("ingrese un numero: ")
#     numero = int(numero)

#     if numero % 2 != 0:
#         continue

#     print(numero)

for i in range(5):
    print(f"i: {i}")
    for j in range(10):
        print(f"\tj: {j}")
