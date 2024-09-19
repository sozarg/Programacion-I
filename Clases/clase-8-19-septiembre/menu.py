bandera = True
while bandera == True:
    opcion = input("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\nElija una opcion: ")
    match opcion:
        case "1":
            print("Estoy sumando")
        case "2":
            print("Estoy restando")
        case "3":
            print("Estoy multiplicando")
        case "4":
            print("Estoy dividiendo")
        case "5":
            print("gracias por usar mi super calculadora")
            bandera = False