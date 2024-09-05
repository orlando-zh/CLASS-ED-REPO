def diagonal_principal():

    matriz = [[0] * 3 for _ in range(3)]

    print("Ingrese los elementos de la matriz 3x3:")
    for i in range(3):
        for j in range(3):
            while True:
                try:
                    matriz[i][j] = float(input(f"Ingrese el elemento ({i+1},{j+1}): "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    print("\nLa diagonal principal de la matriz es:")
    for i in range(3):
        print(matriz[i][i])

diagonal_principal()