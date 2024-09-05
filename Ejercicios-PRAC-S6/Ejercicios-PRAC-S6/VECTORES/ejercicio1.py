def sumar_elementos_vector():
  # Creamos un vector vacío para almacenar los números
  vector = []

  for i in range(5):
    numero = float(input("Ingrese el número {}: ".format(i+1)))
    vector.append(numero)

  suma = 0

  for numero in vector:
    suma += numero

  print("La suma de los elementos del vector es:", int(suma))

sumar_elementos_vector()
