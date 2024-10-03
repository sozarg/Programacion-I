lista = [2,9,-9,6,-4,2,0,3,-1]
#de mayor a menor (?
for i in range(len(lista)-1): #verde
    for j in range(i+1, len(lista)): #naranja
        if lista[i] < lista[j]:
            c= lista[i]
            lista[i] = lista[j]
            lista[j] = c

for i in range(len(lista)):
    print(lista[i])