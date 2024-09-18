def es_primo(num):

  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def generar_matriz_primos():
  
  matriz = []
  contador = 2
  while len(matriz) < 5:
    fila = []
    while len(fila) < 5:
      if es_primo(contador):
        fila.append(contador)
      contador += 1
    matriz.append(fila)
  return matriz

matriz_primos = generar_matriz_primos()

for fila in matriz_primos:
    print(fila)