def mostrar_lista(mi_lista: list):
    if type(mi_lista == list):
        for i in range (len(lista)):
            print(f"Elemento {i+1}: {lista[i]}")
    
####MAIN##
lista = [5, 9, 4, 11, 9]

mostrar_lista(lista)



# acumulador = 0
# for i in range(len(lista)):
#     acumulador += lista[i]
    
# print(f"La suma es: {acumulador}")

# contador = 0
# for i in range(len(lista)):
#     if lista[i] % 2 == 0:
#         contador +=1

# print(f"Hay {contador} numeros pares")