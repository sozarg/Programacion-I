#Alumno: Terrile Mateo
#División 111
#4
# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
def determinar_paridad(numero:int)->bool:
    if numero % 2 == 0:
        es_par = True
    else:
        es_par = False
        
    return es_par
##MAIN##
resultado = determinar_paridad(7)
print(resultado)