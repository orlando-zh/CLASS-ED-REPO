def calcular_promedio():

    suma = 0
    for i in range(10):
        numero = float(input(f"Ingrese el número {i+1}: "))
        suma += numero 

    promedio = suma / 10
    print(f"El promedio de los números ingresados es: {promedio:.0f}")

calcular_promedio()
