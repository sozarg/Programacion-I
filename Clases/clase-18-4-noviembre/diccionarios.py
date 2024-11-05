def crear_boton(color_fondo, texto, accion):
    boton = {}
    boton["color fondo"] = color_fondo
    boton["texto"] = texto
    boton["accion"] = accion
    return crear_boton

def saludar():
    print("Hola mundo")

def sumar_numeros():
    return 3 + 5

def pedir_numero():
    numero = int(input("ingrese un numero: "))
    return numero

boton_1 = crear_boton("rojo", "saludar", saludar)
boton_2 = crear_boton("azul", "sumar", sumar_numeros)
boton_3 = crear_boton("verde", "Ingreso de numero", pedir_numero)
while True:
    opcion = int(input(" 1. Saludar\n2. Sumar\n3. Pedir numero\n4. Salir\n Elija opcion"))
    match opcion:
        case 1: 
            boton_1["accion"]()
        case 2:
            resultado = boton_2["accion"]()
            print(resultado)
        case 3:
            numero = boton_3["accion"]()
            print("El numero ingresado es: ", numero)
        case 4:
            break