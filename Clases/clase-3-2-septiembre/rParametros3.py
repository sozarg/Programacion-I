def determinar_paridad(numero:int)->str:
    if numero % 2 == 0:
        mensaje = "Es par"
    else:
        mensaje = "Es impar"
        
    return mensaje

resultado = determinar_paridad(8)
print(resultado)