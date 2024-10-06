lista = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3]

import time
start = time.time()

# Algoritmo de burbuja
for i in range(len(lista)-1):
    for j in range(len(lista)-1-i):  # Comparar elementos adyacentes
        if lista[j] < lista[j + 1]:  # Cambia el < a > para orden ascendente
            # Intercambia los elementos
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

for i in range(len(lista)):
    print(lista[i])

end = time.time()
dif = end - start
print(dif * 1000)  # Tiempo en milisegundos
