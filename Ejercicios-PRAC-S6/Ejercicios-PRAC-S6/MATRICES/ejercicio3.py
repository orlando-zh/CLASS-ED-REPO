def transpuesta_matriz():
   
    matriz = []

    print("Ingrese los elementos de la matriz 2x3 fila por fila:")
    for i in range(2):
        fila = []
        for c in range(3):
            elemento = float(input(f"Ingrese el elemento ({i+1},{c+1}): "))
            fila.append(elemento)
        matriz.append(fila)

    transpuesta = [[fila[c] for fila in matriz] for c in range(3)]

    print("Matriz original:")
    for fila in matriz:
        print(fila)

    print("\nMatriz transpuesta:")
    for fila in transpuesta:
        print(fila)

transpuesta_matriz()