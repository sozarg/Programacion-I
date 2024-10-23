from Class_Personaje import *

mi_personaje = Personaje(40, "Thor", False, True, "Invocar rayos", 500)
otro_personaje = Personaje(25, "Spiderman", True, False, "Muerte instantanea", 250)
tercer_personaje = Personaje(10, "IronMan", True, True, "Disparo ultrasonico", 300)

print(mi_personaje.retornar_descripcion())
print(otro_personaje.retornar_descripcion())

mi_personaje.volar(100,200)
otro_personaje.volar(150,300)

otro_personaje.atacar(mi_personaje)
tercer_personaje.atacar(otro_personaje)