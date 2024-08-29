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

tope = 0
i = True

# A)

while tope < 10 and i == True:
    tope +=1
    nombre_empleado = input("Ingrese el nombre del empleado")
    edad_empleado = int(input("Ingrese la edad del empleado"))
    while edad_empleado < 18:
        edad_empleado = int(input("ERROR,Ingrese la edad del empleado"))
    genero_empleado = input("Ingrese el genero del empleado (Masculino - Femenino - Otro)")
        while genero_empleado != "Masculino" and genero_empleado != "Femenino" and genero_empleado != "Otro"
