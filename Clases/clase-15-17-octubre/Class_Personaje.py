class Personaje:
    def __init__(self, id, nombre, nano, vuelva, super_poder, poder_pelea): #constructor
        self.id_personaje = id
        self.nombre_personaje = nombre
        self.usa_nanotecnologia = nano
        self.puede_volar = vuelva
        self.super_poder = super_poder
        self.poder_pelea = poder_pelea
    
    def retornar_descripcion(self) -> str:
        string_formato = f"Hola, soy {self.nombre_personaje}.\n"
        if self.usa_nanotecnologia == True:
            string_formato += "Dispongo de nanotecnologia.\n"
        else:
            string_formato += "No dispongo de nanotecnologia hasta que el Sr Stark me haga un traje. \n"
        
        string_formato += f"Mi super poder es: {self.super_poder}.\n"
        string_formato += "*"*50
        
        return string_formato
    
    def volar(self, altura, velocidad):
        if self.puede_volar:
            print(f"Soy {self.nombre_personaje} y estoy volando a una altura de {altura} mts, a una velocidad de: {velocidad}km/h")
        else:
            print(f"{self.nombre_personaje} No puede volar")
    
    def atacar(self, otro_personaje: "Personaje"):
        if self.poder_pelea > otro_personaje.poder_pelea:
            print(f"GANO: {self.nombre_personaje}")
            self.poder_pelea -= otro_personaje.poder_pelea
            otro_personaje.poder_pelea = 0
        elif self.poder_pelea < otro_personaje.poder_pelea:
            print(f"GANO {otro_personaje.nombre_personaje}")
            otro_personaje.poder_pelea -= self.poder_pelea
            self.poder_pelea = 0
        else:
            print("Hubo empate")