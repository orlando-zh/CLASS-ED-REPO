consultas = []

while True:
    print("--- VIENVENIDOS A CONSULTAS UNIVO ---")
    print("1. Consultar Inicio de ciclo")
    print("2. consultar mensualidad ")
    print("3. Consultar Finalidad de ciclo")
    print("4. Salir")
    print("-------------------------------")

    opc = input("Selecciona una opción (1-4): ")

    if opc == '1':
        print(f"EL INICIO DE CICLO COMIENZA EL 16 DE ENERO 2025")

    elif opc == '2':
        print("LA MENSUALIDAD ES DE $110.00")
    
    elif opc == '3':
        print("EL FINAL DE CICLO ES 15 DE NOVIEMBRE")

    elif opc == '4':
        print("Saliendo del sistema.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

