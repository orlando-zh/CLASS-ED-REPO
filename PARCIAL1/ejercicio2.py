numeros_impares = []

for i in range(10):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    if numero % 2 != 0:
        numeros_impares.append(numero)

print("Los números impares ingresados son:", numeros_impares)