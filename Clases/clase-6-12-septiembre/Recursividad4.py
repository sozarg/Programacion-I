def calcular_factorial(numero:int) -> int:
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero -1)
    
    return resultado

factorial = calcular_factorial(5)
print(factorial)