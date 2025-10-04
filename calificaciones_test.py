from calificaciones import nota_teoria,nota_continua,genera_mensaje
from calificaciones_ui import solicita_notas,mostrar_notas
print(nota_teoria(9.1,7.2))
print(nota_teoria(4.0, 6.0))
print(nota_teoria(4.0, 3.0))
print(nota_teoria(None, 3.0))
print(nota_teoria(9.0, None))
print(nota_teoria(None, None))



print(nota_continua(9.6, 9.9, 10.0, 9.8, 9.7, 9.5))
print(nota_continua(4.4, 4.9, 5.1, 4.7, 4.6, 4.8))
print(nota_continua(4.0, 6.0, 4.0, 3.0, 5.0, None))
print(nota_continua(9.0, None, 4.0, 3.0, 4.5, None))
print(nota_continua(9.0, 5.0, 4.0, None, 4.5, None))
print (genera_mensaje(6,5,6))
print(genera_mensaje(4,6,4))
print(genera_mensaje(7,3,4))
print(genera_mensaje(4,3,3.5))

datos=solicita_notas()
mostrar_notas(datos)
nombre,teoria,practica=datos
nota_final=nota_continua(teoria[0], teoria[1], teoria[2], teoria[3], practica[0], practica[1])
print(f"La nota final de {nombre} es:{nota_final:.2f}")
