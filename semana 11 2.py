# Tarea 1.2 Semana 11

# Ordenación de Arreglo Multidimensional

def ordenar_fila_ascendente(matriz,fila):

    # Copiamos la fila para no alteral la matriz original
fila_ordenada = matriz[fila].copy()
n = len(fila_ordenada)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if fila_ordenada[j] > fila_ordenada[j + 1]:
            fila_ordenada[j], fila_ordenada[j + 1] = fila_ordenada[j + 1], fila_ordenada[j]
    return fila_ordenada

# Definimos la matriz
matriz = [[21, 121, 44], [95, 48, 62], [12, 84, 58]]

# El programa imprime la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

#fila a ordenar (indicende base 0)
fila_a_ordenar = 1

# El programa ordena la fila en orden ascendente
fila_ordenada = ordenar_fila_ascendente(matriz, fila_a_ordenar)

# Se actualiza la matriz con la fila ordenada
matriz[fila_a_ordenar] = fila_ordenada

# El programa imprime la matriz con la fila ordenada
print("\nMatriz con la fila ordenada en orden ascendente:")
for fila in matriz:
    print(fila)

# Fin del programa

