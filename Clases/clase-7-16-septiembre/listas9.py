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

def contar_pares(mi_lista: list) ->int:
    contador = 0
    for i in range(len(mi_lista)):
        if mi_lista[i] % 2 == 0:
            contador +=1
    return contador

def cargar_lista(mi_lista: list):
    for i in range(len(mi_lista)):
        numero = int(input("Ingrese un numero: "))
        while numero > 100 or numero < 1:
            numero = int(input("Reingrese un numero: "))
            
        mi_lista[i] = numero
        
def crear_lista(limite: int, valor:any) -> list:
    lista = [valor] * limite
    return lista
####MAIN##
lista = crear_lista(10, valor= -1)


if mostrar_lista(lista) == False:
    print("Hubo un error al intentar mostrar")
