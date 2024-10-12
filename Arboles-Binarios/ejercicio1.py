class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.raiz:
            self.raiz = nuevo_nodo
            return
        
        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo_nodo
                    break
                else:
                    actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = nuevo_nodo
                    break
                else:
                    actual = actual.derecho

    def recorrido_inorden(self):
        resultado = []
        stack = []
        actual = self.raiz

        while True:
            if actual is not None:
                stack.append(actual)
                actual = actual.izquierdo
            elif stack:
                actual = stack.pop()
                resultado.append(actual.valor)
                actual = actual.derecho
            else:
                break

        return resultado
    def visualizar_arbol(self, nodo, nivel=0, prefijo="Root: "):
        """ Función para visualizar el árbol binario """
        if nodo is not None:
            print(" " * (nivel * 4) + prefijo + str(nodo.valor))
            self.visualizar_arbol(nodo.izquierdo, nivel + 1, "Izq: ")
            self.visualizar_arbol(nodo.derecho, nivel + 1, "Der: ")

arbol = ArbolBinario()

valores = [5, 3, 8, 1, 4, 7, 9]
for valor in valores:
    arbol.insertar(valor)
    
print("Recorrido Inorden:", arbol.recorrido_inorden())


print("\nVisualización del árbol binario:")
arbol.visualizar_arbol(arbol.raiz)