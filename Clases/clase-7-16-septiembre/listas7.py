def mostrar_lista(mi_lista: list)-> bool:
    exito = False
    if type(mi_lista == list):
        exito = True
        for i in range (len(mi_lista)):
            print(f"Elemento {i+1}: {mi_lista[i]}")
            
    return exito
    

def acumular_valores(mi_lista: list)-> int:
    acumulador = 0
    for i in range(len(mi_lista)):
        acumulador += mi_lista[i]
        return acumulador
####MAIN##
lista = [5, 9, 4, 11, 9]
otra = [3,8]

if mostrar_lista(lista) == False:
    print("Hubo un error al intentar mostrar")

suma = acumular_valores(lista)
suma2 = acumular_valores(otra)
total = suma + suma2
print(f"La suma es: {total}")



# acumulador = 0
# for i in range(len(lista)):
#     acumulador += lista[i]
    
# print(f"La suma es: {acumulador}")

# contador = 0
# for i in range(len(lista)):
#     if lista[i] % 2 == 0:
#         contador +=1

# print(f"Hay {contador} numeros pares")