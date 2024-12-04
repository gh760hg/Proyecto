def segundos_en_dias(dias):
  """Calcula el número de segundos en una cantidad dada de días.

  Args:
    dias: El número de días.

  Returns:
    El número de segundos en los días especificados.
  """

  segundos_por_minuto = 60
  minutos_por_hora = 60
  horas_por_dia = 24

  segundos_totales = dias * horas_por_dia * minutos_por_hora * segundos_por_minuto
  return segundos_totales

# Ejemplo de uso:
numero_dias =5
resultado = segundos_en_dias(numero_dias)
print(f"En {numero_dias} días hay {resultado} segundos.")