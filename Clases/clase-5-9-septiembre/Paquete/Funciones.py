from .Otro_Modulo import prueba
TAMAÑO_PANTALLA = 500

def saludar(mensaje:str) -> None:
    prueba()
    print(mensaje)
    
def saludar_alumno(nombre: str, mensaje: str) -> None:
    print(f"Hola, {nombre}. {mensaje}")
    
def saludar_profesor(nombre: str, materia: str) -> None:
    print(f"Hola soy el profe {nombre} de la materia {materia}")