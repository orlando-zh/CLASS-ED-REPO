class GrafoProductos:
    def __init__(self):
        self.grafo = {}
    
    def agregar_producto(self, producto):
        if producto not in self.grafo:
            self.grafo[producto] = []
    
    def agregar_relacion(self, producto_origen, producto_destino):
        if producto_origen in self.grafo and producto_destino in self.grafo:
            self.grafo[producto_origen].append(producto_destino)
    
    def mostrar_grafo(self):
        for producto, relaciones in self.grafo.items():
            print(f"{producto} tiene relación con: {', '.join(relaciones) if relaciones else 'Ninguna'}")
    
    def buscar_producto(self, producto):
        if producto in self.grafo:
            relaciones = self.grafo[producto]
            return f"{producto} tiene relación con: {', '.join(relaciones) if relaciones else 'Ninguna'}"
        return f"{producto} no se encuentra en el grafo."

# Crear instancia del grafo
productos = GrafoProductos()

# Agregar productos
productos.agregar_producto('Electrónicos')
productos.agregar_producto('Bocinas')
productos.agregar_producto('Audífonos')
productos.agregar_producto('Laptop')
productos.agregar_producto('Walmart')
productos.agregar_producto('Vestimenta')
productos.agregar_producto('Suéteres')
productos.agregar_producto('Camisetas')
productos.agregar_producto('Vestidos')
productos.agregar_producto('Frutas')
productos.agregar_producto('Bananas')
productos.agregar_producto('Uvas Verdes')
productos.agregar_producto('Fresas')

# Agregar relaciones entre productos
productos.agregar_relacion('Electrónicos', 'Bocinas')
productos.agregar_relacion('Electrónicos', 'Audífonos')
productos.agregar_relacion('Electrónicos', 'Laptop')
productos.agregar_relacion('Walmart', 'Electrónicos')
productos.agregar_relacion('Walmart', 'Vestimenta')
productos.agregar_relacion('Walmart', 'Frutas')
productos.agregar_relacion('Frutas', 'Bananas')
productos.agregar_relacion('Frutas', 'Uvas Verdes')
productos.agregar_relacion('Frutas', 'Fresas')
productos.agregar_relacion('Vestimenta', 'Suéteres')
productos.agregar_relacion('Vestimenta', 'Camisetas')
productos.agregar_relacion('Camisetas', 'Vestidos')


productos.mostrar_grafo()

producto_buscar = input("Ingrese el nombre del producto que desea buscar: ")
resultado = productos.buscar_producto(producto_buscar)
print(resultado)
