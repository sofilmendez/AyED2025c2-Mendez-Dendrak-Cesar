#aca va el codigo que ejecuta el experimento
import random
import matplotlib.pyplot as plt
from modules.modulo1 import bubble_sort, quick_sort, radix_sort, medir_tiempo

if __name__ == "__main__":
    tamanos = range(1, 200)
    tiempos_burbuja = []
    tiempos_quick = []
    tiempos_radix = []
    tiempos_sorted = []

    for n in tamanos:
        lista = [random.randint(10000, 99999) for _ in range(n)]

        tiempos_burbuja.append(medir_tiempo(bubble_sort, lista))
        tiempos_quick.append(medir_tiempo(quick_sort, lista))
        tiempos_radix.append(medir_tiempo(radix_sort, lista))
        tiempos_sorted.append(medir_tiempo(sorted, lista))

    plt.plot(tamanos, tiempos_burbuja, label="Burbuja")
    plt.plot(tamanos, tiempos_quick, label="Quicksort")
    plt.plot(tamanos, tiempos_radix, label="Radix Sort")
    plt.plot(tamanos, tiempos_sorted, label="Sorted (built-in)")
    plt.xlabel("Tamaño de la lista")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.title("Comparación de algoritmos de ordenamiento")
    plt.show()
