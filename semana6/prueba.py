DatosBasicos ={"Nombres": "Juan Carlos",
                "Apellidos": "perez Garcia",
                "DUI": "010205025-9",
                "Fecha_Nacimiento": "23/03/1980",
                "Luagar_Nacimiento": "Soya City",
                "Nacionalidad": "Salvadoreña",
                "Estado_Civil": "Complocado",
                }

print("\nDetalle del diccionario")
print("=============================")

print("\nClaves del diccionario: " , DatosBasicos.keys())
print("\nValores del diccionario: " , DatosBasicos.values())
print("\nelementos del diccionario: " , DatosBasicos.items())

print("\nInscripcion del curso") 
print("===================================")

print("\nDatos del parcipates")
print("===================================")

print("DUI",DatosBasicos["DUI"])
print("Nombres completo: ",DatosBasicos["Nombres"]+" "+DatosBasicos["Apellidos"])
