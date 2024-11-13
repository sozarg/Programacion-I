#Mateo Terrile Div 111
# CASO INVESTIGACIÓN CRIMINAL: CSI UTN 

# Se ha encontrado una muestra de ADN en el lugar de un crimen, que contiene la siguiente secuencia de bases nitrogenadas: “CGTTTAATG”. La investigación ha revelado tres posibles sospechosos que estaban cerca de la escena del crimen, cada uno con su propia muestra de ADN:
# Juan Pérez
# Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"
# María Rodríguez
# Muestra de ADN: "AACGTTTAATGTTCTAAGCTGCG"
# Carlos Sánchez
# Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"

# Para resolver el caso, nos piden que desarrollemos un programa que compare las combinaciones de bases nitrogenadas de la muestra encontrada con las muestras de los sospechosos. 
# Mostrar el nombre por pantalla en caso de encontrar al asesino, o la leyenda “SON TODOS INOCENTES”. 

# def comparar_combinaciones(muestra_adn:str, nombre_primer_sospechoso: str, adn_primer_sospechoso: str, nombre_segundo_sospechoso: str, adn_segundo_sospechoso: str, nombre_tercer_sospechoso: str, adn_tercer_sospechoso: str) -> str:
#     if muestra_adn in adn_primer_sospechoso:
#         nombre_asesino = nombre_primer_sospechoso
#     elif muestra_adn in adn_segundo_sospechoso:
#         nombre_asesino = nombre_segundo_sospechoso
#     elif muestra_adn in adn_tercer_sospechoso:
#         nombre_asesino = nombre_tercer_sospechoso
#     else:
#         return "Son todos inocentes"
#     return nombre_asesino

# resultado = comparar_combinaciones("CGTTTAATG","Juan Perez","CGGGGCTAAAATTTTTTACGATCG","Maria Rodriguez","AACGTTTAATGTTCTAAGCTGCG","Carlos Sanchez","CGGGGCTAAAATTTTTTACGATCG")
# print(resultado)

def comparar_combinaciones(muestra_adn: str, nombres:list, muestras_sospechosos:list) -> str:
    for i in range(len(nombres)):
        if muestra_adn in muestras_sospechosos[i]:
            return nombres[i]
    return "son todos inocentes"

nombres = ["Juan Perez", "Maria Rodriguez", "Carlos Sanchez"]
muestras_sospechosos = ["CGGGGCTAAAATTTTTTACGATCG", "AACGTTTAATGTTCTAAGCTGCG", "CGGGGCTAAAATTTTTTACGATCG"]

resultado = comparar_combinaciones("CGTTTAATG", nombres, muestras_sospechosos)
print(resultado)