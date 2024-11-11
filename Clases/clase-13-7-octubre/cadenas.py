# cadena = "hola comision 111"

# sub_cadena = cadena[:]
# print(sub_cadena)

# sub_cadena = cadena[3:9] #range
# print(sub_cadena)

# sub_cadena = cadena[5:]
# print(sub_cadena)

# sub_cadena = cadena[:9]
# print(sub_cadena)

def my_slicing(cadena: str, inicio: int, fin: int) -> str:
    for i in range(inicio, fin):
        print(cadena[i], end = "")
cadena = "hola comision 111"

my_slicing(cadena, 2,12)