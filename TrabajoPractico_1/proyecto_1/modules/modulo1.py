# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
import random
import time
import matplotlib.pyplot as plt

# -------------------------
# 1. Algoritmo: Burbuja
# -------------------------
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# -------------------------
# 2. Algoritmo: Quicksort
# -------------------------
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)

# -------------------------
# 3. Algoritmo: Radix Sort
# -------------------------
def counting_sort_para_radix(lista, posicion):
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10

    for num in lista:
        indice = (num // posicion) % 10
        conteo[indice] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    i = n - 1
    while i >= 0:
        indice = (lista[i] // posicion) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1

    for i in range(n):
        lista[i] = salida[i]

def radix_sort(lista):
    maximo = max(lista)
    posicion = 1
    while maximo // posicion > 0:
        counting_sort_para_radix(lista, posicion)
        posicion *= 10
    return lista

# -------------------------
# 4. Medición de tiempos
# -------------------------
def medir_tiempo(algoritmo, lista):
    copia = lista.copy()
    inicio = time.time()
    algoritmo(copia)
    fin = time.time()
    return fin - inicio

# -------------------------
# 5. Main
# -------------------------
if __name__ == "__main__":
    tamanos = range(1, 1001)  # de 1 a 1000
    tiempos_burbuja = []
    tiempos_quick = []
    tiempos_radix = []
    tiempos_sorted = []

    for n in tamanos:
        lista = [random.randint(10000, 99999) for _ in range(n)]  # números de 5 dígitos

        tiempos_burbuja.append(medir_tiempo(bubble_sort, lista))
        tiempos_quick.append(medir_tiempo(quick_sort, lista))
        tiempos_radix.append(medir_tiempo(radix_sort, lista))
        tiempos_sorted.append(medir_tiempo(sorted, lista))

    # -------------------------
    # 6. Gráfico
    # -------------------------
    plt.plot(tamanos, tiempos_burbuja, label="Burbuja")
    plt.plot(tamanos, tiempos_quick, label="Quicksort")
    plt.plot(tamanos, tiempos_radix, label="Radix Sort")
    plt.plot(tamanos, tiempos_sorted, label="Sorted (built-in)")
    plt.xlabel("Tamaño de la lista")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.title("Comparación de algoritmos de ordenamiento")
    plt.show()

    # -------------------------
    # 7. Complejidad
    # -------------------------
    print("Complejidades teóricas:")
    print("Burbuja: O(n^2) -> Comparaciones dobles, peor caso cuadrático.")
    print("Quicksort: O(n log n) promedio, O(n^2) peor caso si pivote malo.")
    print("Radix Sort: O(n * k) donde k es la cantidad de dígitos.")
    print("sorted(): usa Timsort -> O(n log n) promedio y mejor caso casi ordenado O(n).")

