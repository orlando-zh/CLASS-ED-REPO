def multiplicar_matrices_2x2():

    matriz1 = [[0] * 2 for _ in range(2)]
    matriz2 = [[0] * 2 for _ in range(2)]
    resultado = [[0] * 2 for _ in range(2)]

    print("Ingrese los elementos de la primera matriz:")
    for i in range(2):
        for j in range(2):
            matriz1[i][j] = float(input(f"Ingrese el elemento ({i+1},{j+1}): "))

    print("\nIngrese los elementos de la segunda matriz:")
    for i in range(2):
        for j in range(2):
            matriz2[i][j] = float(input(f"Ingrese el elemento ({i+1},{j+1}): "))

    # Realizar la multiplicación de matrices
    for i in range(2):
        for j in range(2):
            for k in range(2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    print("\nEl resultado de la multiplicación es:")
    for fila in resultado:
        print(fila)

multiplicar_matrices_2x2()