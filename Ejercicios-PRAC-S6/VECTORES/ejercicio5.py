def invertir_vector():

    vector = []
    for i in range(6):
        numero = int(input(f"Ingrese el numero {i+1}: "))
        vector.append(numero)

    vector_invertido = list(reversed(vector))
    return vector_invertido

resultado = invertir_vector()
print("El vector invertido es:", resultado)