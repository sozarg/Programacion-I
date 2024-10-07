# Crear una función llamada ordenar_vector que reciba como parámetro un vector de números enteros y lo ordene de forma ascendente. La función debe implementar como algoritmo de ordenamiento el método de la burbuja.
# Además, como parámetro opcional debe recibir un booleano (que por default está en False), que en caso de ser True ordena el vector en forma descendente.

# Crear una función que reciba como parámetro un vector de números enteros. La función debe mostrar los números negativos de forma decreciente y luego los positivos de forma creciente. 
# Nota: solo se puede usar un vector, y se debe utilizar la menor cantidad de estructuras repetitivas.

controlador_ascendente = False
lista = [5,7,1,2,6,4,3,8,9]
def ordenar_vector(lista: list, controlador_ascendente: bool) -> list:
    for i in range(len(lista)-1):
        
        for j in range(len(lista)-1-i):
            if (controlador_ascendente and lista[j] > lista[j + 1]) or (not controlador_ascendente and lista[j] < lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
    return lista
    
metodo_burbuja = ordenar_vector(lista, controlador_ascendente)
print(metodo_burbuja)

# Crear una función intercalar_vectores que reciba dos vectores de números enteros ordenados en orden ascendente, y devuelva un único vector también ordenado. 
# La función debe tener un parámetro opcional descendente para que el vector resultante esté en orden descendente.

vector_a = [10,20,30,40,50]
vector_b = [15,25,35,45,55]

def intercalar_vectores(vector_a:int, vector_b:int):
    vector_c = []
    for i in range(len(vector_c)-1):
        for j in range(len(vector_c)-1-i):
            if vector_c[j] < vector_c[j + 1]:
                vector_c[j], vector_c[j + 1] = vector_c[j + 1], vector_c[j]
    return vector_c

intercalo_vectores = intercalar_vectores(lista, controlador_ascendente)
print(intercalo_vectores)