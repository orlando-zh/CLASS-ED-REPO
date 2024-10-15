class Rutina:
    def __init__(self, hora_inicio=5, minutos_inicio=30):

        self.actividades = []
        self.hora_inicio = hora_inicio
        self.minutos_inicio = minutos_inicio

    def agregar_actividad(self, actividad, horas, minutos):
        self.actividades.append((actividad, horas, minutos))

    def mostrar_rutina(self):
        hora_actual = self.hora_inicio
        minutos_actuales = self.minutos_inicio
        for actividad, horas, minutos in self.actividades:
            hora_fin = hora_actual + horas
            minutos_fin = minutos_actuales + minutos
            if minutos_fin >= 60:
                hora_fin += 1
                minutos_fin -= 60
            print(f"{actividad}: {hora_actual:02d}:{minutos_actuales:02d} - {hora_fin:02d}:{minutos_fin:02d}")
            hora_actual = hora_fin
            minutos_actuales = minutos_fin

    def buscar_actividad(self, actividad):
        for act, horas, minutos in self.actividades:
            if act.lower() == actividad.lower():
                return f"{actividad} se realiza durante {horas} horas y {minutos} minutos."
        return f"{actividad} no se encuentra en la rutina."

    def tiempo_total(self):
        total_horas = 0
        total_minutos = 0
        for _, horas, minutos in self.actividades:
            total_horas += horas
            total_minutos += minutos
        total_horas += total_minutos // 60
        total_minutos %= 60
        return f"Tiempo total de actividades: {total_horas} horas y {total_minutos} minutos."

rutina = Rutina()  
rutina.agregar_actividad('Despertarse', 0, 10)
rutina.agregar_actividad('Ducharse', 0, 15)
rutina.agregar_actividad('Prepararse', 0, 7)
rutina.agregar_actividad('Desayunar', 0, 8)
rutina.agregar_actividad('Tomar el transporte', 0, 5)
rutina.agregar_actividad('Llegar a la univerisad', 1, 50)
rutina.agregar_actividad('Esperar la clase', 0, 40)
rutina.agregar_actividad('Tomar clases', 3, 15)
rutina.agregar_actividad('Tomar el transporte de vuelta', 0, 10)
rutina.agregar_actividad('Volver a casa', 1, 50)

rutina.mostrar_rutina()
print(rutina.buscar_actividad('Despertarse'))
print(rutina.buscar_actividad('Ducharse'))
print(rutina.buscar_actividad('Prepararse'))
print(rutina.buscar_actividad('Desayunar'))
print(rutina.buscar_actividad('Tomar el transporte'))
print(rutina.buscar_actividad('Llegar a la univerisad'))
print(rutina.buscar_actividad('Esperar la clase'))
print(rutina.buscar_actividad('Tomar clases'))
print(rutina.buscar_actividad('Tomar el transporte de vuelta'))
print(rutina.buscar_actividad('Volver a casa'))
print(rutina.tiempo_total())