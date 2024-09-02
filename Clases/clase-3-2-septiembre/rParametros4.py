def determinar_paridad(numero:int)->bool:
    if numero % 2 == 0:
        es_par = True
    else:
        es_par = False
        
    return es_par

resultado = determinar_paridad(7)
print(resultado)