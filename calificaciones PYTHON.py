def calcular_promedio(materia):
  """Calcula el promedio de 4 calificaciones de una materia.

  Args:
    materia: El nombre de la materia.

  Returns:
    El promedio de las calificaciones.
  """

  calificaciones = []
  for i in range(4):
    calificacion = float(input(f"Ingrese la calificación {i+1} de {materia}: "))
    calificaciones.append(calificacion)

  promedio = sum(calificaciones) / len(calificaciones)
  return promedio

# Pedimos al usuario el nombre de la materia
materia = input("Ingrese el nombre de la materia: ")

# Llamamos a la función para calcular el promedio
promedio = calcular_promedio(materia)

# Imprimimos el resultado
print(f"El promedio de {materia} es: {promedio}")