def cuenta_regresiva(numero:int)->None:
    if numero != -1:
        print(numero)
        cuenta_regresiva(numero -1)
        
cuenta_regresiva(10)