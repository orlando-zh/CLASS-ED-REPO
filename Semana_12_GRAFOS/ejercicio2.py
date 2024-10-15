class GrafoMusical: 
    def __init__(self): 
        self.grafo = {} 
 
    def agregar_cancion(self, cancion): 
        if cancion not in self.grafo: 
            self.grafo[cancion] = [] 
 
    def agregar_transicion(self, cancion_origen, cancion_destino): 
        if cancion_origen in self.grafo and cancion_destino in self.grafo: 
            self.grafo[cancion_origen].append(cancion_destino) 
 
    def mostrar_grafo(self): 
        for cancion, transiciones in self.grafo.items(): 
            print(f"{cancion} puede saltar a: {', '.join(transiciones) if transiciones else 'Ninguna'}") 
 
    def buscar_cancion(self, cancion): 
        if cancion in self.grafo: 
            transiciones = self.grafo[cancion] 
            return f"{cancion} puede saltar a: {', '.join(transiciones) if transiciones else 'Ninguna'}" 
        return f"{cancion} no se encuentra en el grafo." 

reproductor = GrafoMusical() 
reproductor.agregar_cancion('LUZ - Lil Supa') 
reproductor.agregar_cancion('Créeme - Chuchú Bermudas') 
reproductor.agregar_cancion('RITUAL - Lil Supa') 
reproductor.agregar_cancion('No me interesa - Chuchú Bermudas') 
 
reproductor.agregar_transicion('LUZ - Lil Supa', 'Créeme - Chuchú Bermudas') 
reproductor.agregar_transicion('LUZ - Lil Supa', 'RITUAL - Lil Supa') 
reproductor.agregar_transicion('RITUAL - Lil Supa', 'No me interesa - Chuchú Bermudas') 
reproductor.agregar_transicion('RITUAL - Lil Supa', 'No me interesa - Chuchú Bermudas') 
 
reproductor.mostrar_grafo() 

cancion_buscar = input("Ingrese el nombre de la canción que desea buscar: ") 
resultado = reproductor.buscar_cancion(cancion_buscar) 
print(resultado)
