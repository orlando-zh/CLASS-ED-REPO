def contar_positivos():
    vector = []
    contador_positivos = 0

    for i in range(8):
        numero = float(input(f"Ingrese el número {i+1}: "))
        vector.append(numero)

        if numero > 0:
            contador_positivos += 1

    print(f"Hay {contador_positivos} números positivos en el vector.")

contar_positivos()