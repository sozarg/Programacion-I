lista = [5, 9, 4, 11, 9]

for i in range (len(lista)):
    print(f"Elemento {i+1}: {lista[i]}")
    
acumulador = 0
for i in range(len(lista)):
    acumulador += lista[i]
    
print(f"La suma es: {acumulador}")

contador = 0
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        contador +=1

print(f"Hay {contador} numeros pares")