# Disponemos de los siguientes datos obtenidos de una lista de reproducción del cantante Emanero:

# Tema: “Karina | J mena | Angela - Sinvergüenza”
# Vistas: “45.8 millones”
# Duración: “228” 
# Link: “https://www.youtube.com/watch?v=AhZvCgk1Ay4” 
# Fecha Lanzamiento: “2023-12-05”

# Nos piden desarrollar las siguientes funciones, para un posterior análisis de la lista de reproducción.
# obtener_colaboradores(str) -> list: recibe como parámetro el título del tema y retorna una lista con todos los colaboradores.
# obtener_nombre_tema(str) -> str: retorna el nombre del tema.
# convertir_vistas_numerico(str)->int: convertirá la cantidad de vistas a un número entero expresado en millones.
# convertir_duracion_numerico(str)->int: convertirá la duración a un número entero.
# obtener_codigo(str)->str: retorna el código de la url recibida como parámetro.
# formatear_fecha(str): retorna la fecha recibida por parámetro como un objeto de tipo fecha 😉

def obtener_colaboradores(titulo_tema:str) -> list:
    lista_colaboradores = ["Karina", "J mena", "Angela"]
    return lista_colaboradores

def obtener_nombre_tema() -> str:
    titulo_tema = "Karina | J mena | Angela - Sinvergüenza"
    return titulo_tema

def convertir_vistas_numerico(vistas:str)->int:
    vistas = "45.8"
    vistas_numerico = int(vistas)
    vistas_numerico = vistas_numerico * 1000000
    return vistas_numerico

def convertir_duracion_numerico(duracion:str)->int:
    duracion = "228"
    duracion_numerico = int(duracion)
    return duracion_numerico

def obtener_codigo(link:str)->str: 
    link = "https://www.youtube.com/watch?v=AhZvCgk1Ay4"
    return link

