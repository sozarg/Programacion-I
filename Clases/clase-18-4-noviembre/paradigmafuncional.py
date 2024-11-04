def sumar(a, b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(a, b, operacion):
    resultado = operacion(a, b)
    return resultado
#############
# variable = sumar
# # print(id(variable))
# # print(id(sumar))

# resultado = variable(5,9)
# print(resultado)

###########################

for operacion in operaciones:
    resultado = operacion(11,5)
    