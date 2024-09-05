def pedir_numero(mensaje, minimo, maximo, mensaje_error):
    numero = input(mensaje)
    numero = int(numero)
    while numero < minimo or numero > maximo:
        numero = input(mensaje_error)
        numero = int(numero)
    
    return numero

legajo_alumno = pedir_numero("Ingreso legajo: ", 1, 1000, "Error. Reingrese legajo: ")

edad_alumno = pedir_numero("Ingrese la edad: ", 18, 65, "La edad esta fuera de rango. Reingrese: ")