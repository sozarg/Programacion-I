def crear_lista(limite: int, valor: any) -> list:
    lista = [valor] * limite
    return lista

def mostrar_lista(mi_lista: list) -> bool:
    exito = False
    if type (mi_lista) == list:
        exito = True
        for i in range(len(mi_lista)):
            if mi_lista[i] != None:
                print(f"Elemento {i+1}: {mi_lista[i]}")
                
def acumular_valores(mi_lista: list) -> int:
    acumulador = 0
    for i in range(len(mi_lista)):
        if mi_lista[i] != None:
            acumulador += mi_lista[i]
            
    return acumulador

lista_numeros = crear_lista(10, None)

seguir = "si"
while seguir == "si":
    numero = int(input("Ingrese un numero positivo: "))
    posicion = int(input("Ingrese una posicion: "))
    #validar 1- len(lista)
    lista_numeros[posicion-1] = numero #1
    
    seguir = input("Desea ingresar otro numero? si/no")
    
mostrar_lista(mi_lista = lista_numeros, valor_filtro = None)
acumulador = acumular_valores(mi_lista = lista_numeros, valor_filtro = None)
