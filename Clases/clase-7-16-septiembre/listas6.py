def mostrar_lista(mi_lista: list)-> bool:
    exito = False
    if type(mi_lista == list):
        exito = True
        for i in range (len(lista)):
            print(f"Elemento {i+1}: {lista[i]}")
            
    return exito
    
####MAIN##
lista = [5, 9, 4, 11, 9]
p = 0
if mostrar_lista(p) == False:
    print("Hubo un error al intentar mostrarr")



# acumulador = 0
# for i in range(len(lista)):
#     acumulador += lista[i]
    
# print(f"La suma es: {acumulador}")

# contador = 0
# for i in range(len(lista)):
#     if lista[i] % 2 == 0:
#         contador +=1

# print(f"Hay {contador} numeros pares")