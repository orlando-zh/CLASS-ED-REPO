numeros = []
for i in range(7):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

numero_mayor = max(numeros)
print(f"El número mayor es:", int(numero_mayor))