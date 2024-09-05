def sumar_matriz():

  matriz = []
  print("Por favor, ingresa los elementos de la matriz 3x3 fila por fila:")

  for i in range(3):
    fila = []
    for j in range(3):
      while True:
        try:
          elemento = int(input(f"Ingrese el elemento en la posición ({i+1}, {j+1}): "))
          fila.append(elemento)
          break
        except ValueError:
          print("Entrada inválida. Por favor, ingresa un número entero.")

    matriz.append(fila)

  # Calcular la suma de todos los elementos
  suma_total = 0
  for fila in matriz:
    for elemento in fila:
      suma_total += elemento

  print("La matriz ingresada es:")
  for fila in matriz:
    print(fila)

  print("La suma de todos los elementos de la matriz es:", suma_total)

sumar_matriz()