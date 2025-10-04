def nota_teoria(examenT1,examenT2):
    if examenT1 is None:
        examenT1=0
    if examenT2 is None:
        examenT2=0
    return (examenT1+examenT2)/2
def nota_cuatrimestre1(examenT1,examenT2,examenP1):
        if examenT1 is None:
            examenT1=0
        if examenT2 is None:
            examenT2=0
        if examenP1 is None:
            examenP1=0
        if nota_teoria(examenT1,examenT2) < 4:
            return 0
        else:
             return (0.15*examenT1 + 0.15*examenT2 + 0.7*examenP1)
def nota_cuatrimestre2(examenT3,examenT4,examenP2):
        if examenT3 is None:
            examenT3=0
        if examenT4 is None:
            examenT4=0
        if examenP2 is None:
            examenP2=0
        if nota_teoria(examenT3,examenT4) < 4:
            return 0
        else:
             return (0.15*examenT3 + 0.15*examenT4 + 0.7*examenP2)
def media_cuatrimestre(nota1,nota2):
    return (nota1 + nota2)/2
def nota_continua(examenT1,examenT2,examenT3,examenT4,examenP1,examenP2):
    nota1 = nota_cuatrimestre1(examenT1,examenT2,examenP1)
    nota2 = nota_cuatrimestre2(examenT3,examenT4,examenP2)
    media= media_cuatrimestre(nota1,nota2)
    if nota1<5 or nota2<5:
        return min(4,media)
    else:
        return media
def genera_mensaje(nota_cuatrimestre1,nota_cuatrimestre2,nota_continua):
    if nota_continua>=5:
          print("¡Enhorabuena!Has aprobado la asignatura.")
    elif nota_cuatrimestre1<5 and nota_cuatrimestre2>= 5:
         print ("Debes recuperar el primer trimestre")
    elif nota_cuatrimestre1>=5 and nota_cuatrimestre2<5:
         print("Debes recuperar el segundo cuatrimestre")
    else:
         print("Debes recuperar toda la asignatura")