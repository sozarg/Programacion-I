def modificar_lista(lista):
    print(id(lista))
    
    lista[2] = 1000
    print(id(lista))
    
lista = [4,9,8]
print(id(lista))
modificar_lista(lista)

print(lista)