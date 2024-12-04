Algoritmo DistanciaEntreDosPuntos
	// Declaración de variables
	Definir x1, y1, x2, y2, distancia Como Real
	// Entrada de datos
	Escribir 'Ingrese la coordenada x del primer punto: '
	Leer x1
	Escribir 'Ingrese la coordenada y del primer punto: '
	Leer y1
	Escribir 'Ingrese la coordenada x del segundo punto: '
	Leer x2
	Escribir 'Ingrese la coordenada y del segundo punto: '
	Leer y2
	// Cálculo de la distancia
	distancia <- Raiz((x2-x1)^2+(y2-y1)^2)
	// Salida de resultados
	Escribir 'La distancia entre los dos puntos es: ', distancia
FinAlgoritmo
