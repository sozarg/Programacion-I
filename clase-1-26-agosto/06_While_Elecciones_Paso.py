import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        mayor_cantidad_votos_flag = True
        menor_cantidad_votos_flag = True
        maximo_votos = 0
        minimo_votos = 0
        acumulador_candidatos = 0
        contador_candidatos = 0
        total_votos = 0
        seguir = True
        while seguir == True:
            nombre_candidato = prompt("X", "Ingrese el nombre del candidato")
            if not nombre_candidato:
                break
            edad_candidato = prompt("X", "Ingrese la edad del candidato")
            edad_candidato = int(edad_candidato)
            while not (edad_candidato >= 25 and edad_candidato < 100):
                edad_candidato = prompt ("X", "ERROR,Ingrese la edad del candidato")
                edad_candidato =int(edad_candidato)
            cantidad_votos = prompt("X", "Ingrese la cantidad de votos")
            cantidad_votos = int(cantidad_votos)
            while not cantidad_votos >= 0:
                cantidad_votos = prompt("X", "Error, no pueden haber votos menores a cero")
                cantidad_votos = int(cantidad_votos)
            
            #A
            if cantidad_votos > maximo_votos or mayor_cantidad_votos_flag == True:
                maximo_votos = cantidad_votos
                candidato_con_mas_votos = nombre_candidato
                mayor_cantidad_votos_flag = False
            #B
            if cantidad_votos < minimo_votos or menor_cantidad_votos_flag == True:
                minimo_votos = cantidad_votos
                candidato_con_menos_votos = nombre_candidato
                edad_menos_votos = edad_candidato
                menor_cantidad_votos_flag = False
            #C
                acumulador_candidatos += edad_candidato
                contador_candidatos += 1
            #D
            total_votos += cantidad_votos

            seguir = question("X", "¿Desea ingresar otro candidato?")

        promedio_total = round(acumulador_candidatos / contador_candidatos)
            
        alert("A", f"El nombre del candidato con mas votos es {candidato_con_mas_votos}")
        alert("B", f"El nombre del candidato con menos votos es {candidato_con_menos_votos} con {edad_menos_votos} años")
        alert("C", f"El promedio de edad de los candidatos es de: {promedio_total}")
        alert("D", f"El total de votos emitidos es de: {total_votos} votos")
               




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
