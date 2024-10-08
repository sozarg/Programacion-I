#Alumno: Terrile Mateo
#División 111

# UTN Technologies
# Actividades


# UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.

# Las posibles aplicaciones son las siguientes:
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA),
# Internet de las cosas (IOT)

# Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

# A) Los datos a ingresar por cada empleado encuestado son:
# nombre del empleado
# edad (no menor a 18)
# género (Masculino - Femenino - Otro)
# tecnologia (IA, RV/RA, IOT)  
# B) Cargar por terminal 10 encuestas.
# C) Determinar:
# Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
# Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
# Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.

i = 0

empleado_masculino = 0
empleado_femenino = 0
empleado_otro = 0

masculino_iot_ia = 0

no_votaron_ia = 0

bandera_mayor_edad = False
masculino_mayor_edad = 0
nombre_masculino_mayor_edad = "No ingresado"
tecnologia_mayor_edad = 0

while i < 10:
    #Ingreso de datos
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    edad_empleado = int(input("Ingrese la edad del empleado: "))
    while edad_empleado < 18:
        edad_empleado = int(input("ERROR,Ingrese la edad del empleado: "))
    genero_empleado = input("Ingrese el genero del empleado (Masculino - Femenino - Otro): ")
    while genero_empleado != "Masculino" and genero_empleado != "Femenino" and genero_empleado != "Otro":
        genero_empleado = input("ERROR, Ingrese el genero del empleado (Masculino - Femenino - Otro): ")
    tecnologia_empleado = input("Ingrese la tecnologia del empleado (IA - RV/RA - IOT): ")
    while tecnologia_empleado != "IA" and tecnologia_empleado != "RV/RA" and tecnologia_empleado != "IOT":
        tecnologia_empleado = input("ERROR, Ingrese la tecnologia del empleado (IA - RV/RA - IOT): ")
    #Procesos
    
    #Empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
    if genero_empleado == "Masculino" and (tecnologia_empleado == "IOT" or tecnologia_empleado == "IA") and edad_empleado >= 25 and edad_empleado <= 50:
        masculino_iot_ia += 1
    
    #Empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
    if genero_empleado != "Femenino" or (edad_empleado < 33 or edad_empleado > 40):
        if tecnologia_empleado != "IA":
            no_votaron_ia += 1
    
    #Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
    
    if genero_empleado == "Masculino" and edad_empleado > masculino_mayor_edad or bandera_mayor_edad == False:
        masculino_mayor_edad = edad_empleado
        nombre_masculino_mayor_edad = nombre_empleado
        tecnologia_mayor_edad = tecnologia_empleado
        bandera_mayor_edad = True
    
    i +=1

#Procesos

#Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
if i > 0:
    porcentaje_no_votaron_ia = (no_votaron_ia * 100) / i
else:
    porcentaje_no_votaron_ia = 0

#Salidas
resultado = (f"Empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive: {masculino_iot_ia} empleados.\n"
             f"Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40: {porcentaje_no_votaron_ia}%\n"
             f"Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género: Nombre: {nombre_masculino_mayor_edad} - Tecnologia: {tecnologia_mayor_edad} - Edad: {masculino_mayor_edad} años")
print(resultado)
