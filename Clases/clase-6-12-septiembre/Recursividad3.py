#planteo sin recursividad
def calcular_factorial(numero: int) -> int:
    cuenta = 1
    for i in range(numero, 0, -1):
        cuenta *=  i
        print(cuenta)
    return cuenta

factorial = calcular_factorial(5)
print(factorial)     