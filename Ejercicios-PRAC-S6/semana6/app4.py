filas = int(input("Ingresa el numero de filas: "))
columnas = int(input("Ingrese el numeros de Columnas: "))

matriz = [["A" for _ in range(columnas)] for _ in range(filas)]

print("\nLa matriz resultante es: ")

for fila in matriz:
    print(fila)