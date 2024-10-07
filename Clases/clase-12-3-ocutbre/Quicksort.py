def swap(a: int, b: int):
    return b,a

def particionar(array, low, high):
    pivote = array[high] #El pivote sera el ultimo elemento de la lista
    i = low - 1
        
    for j in range(low, high):
        
        if array[j] <= pivote:
            i += 1
            array[i], array[j] = swap(array[i], array[j])
    
    array[i + 1], array[high] = swap(array[i + 1], array[high] )
    
    return i + 1
    
def quick_sort(array, low, high):

    if low < high:
        pi = particionar(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

vector = [2,9,-9,6,-4,2,0,3,-1]
quick_sort(vector, 0, len(vector) - 1)


for i in range(len(vector)):
    print(vector[i])
