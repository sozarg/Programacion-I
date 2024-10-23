lista = [3,9,8,2]
#lista.append(9) #se agrega a lo ultimo
#lista.insert(1,44) #se coloca en la posicion que le ordenes
#lista.remove(9) #saca la primera ocurrencia, osea el primer 9 que encuentre
#elemento = lista.pop(2) #el pop saca el numero la posicion que yo le diga y la puedo guardar en otro lado
#print(elemento)
#print()
#for elemento in lista:
#    print(elemento)
    
#index = lista.index(9) # te dice donde esta la posicion del numero q le indico
#print(index)

lista.sort(reverse=True) #ordena mayor a menor
for elemento in lista:
    print(elemento)

lista.clear() #la borra
for elemento in lista:
    print(elemento)
    
# tambien
# Usa del variable para eliminar una variable.
# Usa del lista para eliminar una lista completa.
# Usa del lista[índice] para eliminar un elemento específico de la lista.