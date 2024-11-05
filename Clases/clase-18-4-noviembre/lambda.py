def calcular(a, b, operacion):
    return operacion(a,b)

resultado = calcular(5, 7, lambda a,b: a - b * 2)
print(resultado)

resultado = calcular(5, 7, lambda a,b: a>b)
print(resultado)