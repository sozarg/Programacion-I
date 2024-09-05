def calificar_alumno(nombre: str, presente: bool, nota1: float = None, nota2: float = None) -> float|str:
    """_summary_

    Args:
        nombre (str): nombre del alumno
        presente (bool): si estuvo presente en el examen o no
        nota1 (float, optional): nota del primer examen. Defaults to None.
        nota2 (float, optional): nota del segundo examen. Defaults to None.

    Returns:
        float|str: el promedio de notas o ausente
    """
    #calcula el promedio de notas si el alumno estuvo presente
    #nombre: nombre del alumno - presente: si estuvo presente en el examen o no
    #nota1 nota del primer examen - nota2 nota del segundo examen
    #retorna el promedio de notas o ausente
    nota_final= "Ausente"
    print(f"Calificando al alumno: {nombre}...")
    if presente:
        nota_final = (nota1 + nota2) / 2
        
        return nota_final
nota_final = calificar_alumno("Juan", True, 7,8)
print(nota_final)
    
    