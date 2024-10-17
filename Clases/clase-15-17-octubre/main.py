from Class_Personaje import *

mi_personaje = Personaje(40, "Thor", False, True, "Invocar rayos", 500)
otro_personaje= Personaje(25, "Spiderman", True, False, "Muerte instantanea", 250)

print(mi_personaje.retornar_descripcion())
print(otro_personaje.retornar_descripcion())