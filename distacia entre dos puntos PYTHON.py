import math

def calcular_distancia(x1, y1, x2, y2):
  """Calcula la distancia entre dos puntos en un plano cartesiano.

  Args:
    x1: Coordenada x del primer punto.
    y1: Coordenada y del primer punto.
    x2: Coordenada x del segundo punto.
    y2: Coordenada y del segundo punto.

  Returns:
    La distancia entre los dos puntos.
  """

  # Aplicamos la fórmula de la distancia
  distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  return distancia

# Pedimos al usuario que ingrese las coordenadas
print("Ingrese las coordenadas del primer punto:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("Ingrese las coordenadas del segundo punto:")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

# Llamamos a la función para calcular la distancia
resultado = calcular_distancia(x1, y1, x2, y2)

# Imprimimos el resultado
print("La distancia entre los dos puntos es:", resultado)