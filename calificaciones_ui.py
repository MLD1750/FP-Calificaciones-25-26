from calificaciones import*
def solicita_notas():
    nombre=(input("Introduzca su nombre:"))
    examenT1=float(input("Introduzca la nota del examen teórico 1:"))
    examenT2=float(input("Introduzca la nota del examen teórico 2:"))
    examenT3=float(input("Introduzca la nota del examen teórico 3:"))
    examenT4=float(input("Introduzca la nota del examen teórico 4:"))
    examenP1=float(input("Introduzca la nota del examen práctico 1:"))
    examenP2=float(input("Introduzca la nota del examen práctico 2:"))
    return(nombre,[examenT1,examenT2,examenT3,examenT4],[examenP1,examenP2])
def mostrar_notas(datos):
    nombre,teoria,practica=datos
    print(f"nombre estudiante:{nombre}")
    print(f"Notas teoria:{teoria}")
    print(f"Notas practica:{practica}")