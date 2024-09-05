def contar(contador):
    print(id(contador))
    contador = 5
    print(id(contador))
    
contador = 5
print(id(contador))

contar(contador)
print(id(contador))