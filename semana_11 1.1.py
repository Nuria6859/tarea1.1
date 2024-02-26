# Tarea 1.1 semana 11

# Búsqueda en Arreglo Multidimensional

# Definimos la matriz
matriz = [[1, 2, 3], [5, 4, 6], [7, 8, 9]]

# Definimos el valor a buscar
valos_a_buscar = 3

def buscar_en_matriz(matriz, valor):
    # El programa busca en cada fila de la matriz
for i in range(len(matriz)):
    # El programa recorre cada columna de la matriz
for j in range(len(matriz[i])):
    # Si el programa encuentra el valor, retorna su posición
if matriz[i][j] == valos_a_buscar:
    return True, (i, j)

    # Si no encuentra el valor, retorna False
    return False, None

 # Llamamos a a función con matríz y el valor a buscar
encontrado, posición = buscar_en_matriz(matriz, valos_a_buscar)

# Se imprime el resultado
# Si es verdadero
if encontrado:
    print(f"El valor{valor_a_buscar}se encontró en la posición {posición}de la matríz.")
# Si es falso
else:
    print(f"El valor{valor_a_buscar} no se encuentra en la matriz.")

    # Fin del programa