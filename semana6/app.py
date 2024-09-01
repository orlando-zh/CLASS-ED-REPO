temperaturas= []
print("por favor, ingresa 10 temperaturas")

for i in range(10):
    temperatura = float(input(f"Temperatura {i + 1}: "))
    temperaturas.append(temperatura)

promedio = sum(temperaturas) / len(temperaturas)

print(f"\nEl promedio de as temperaturas es: {promedio:.2f}")

while True:
    opcion = input("\nVer alguna temperatura? (si o no): ").strip().lower()

    if opcion == "si":
        posicion = int(input("ingrese la posicion del 1 al 10 de la temperatura que deese: "))
        if 1 <= posicion <= 10:
            print(f"la temperatura en la posicion {posicion} es: {temperaturas[posicion - 1]:.2f}")
        else:
            print("posicion fuera de rango. Por faor ingrese un numero entre 1 y 10")
    elif opcion == "no":
        print("cierre del programa")
        break
    else:
        print("por favor, ingresa si o no")