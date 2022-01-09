from typing import Any


def quick_sort(array: list[Any]) -> list[Any]:
    if len(array) < 2: # Caso-base: arrays com 0 ou 1 elementos
        return array

    pivot = array[0] # Caso recursivo
    smallers = [i for i in array[1:] if i <= pivot] # Subarray de elementos menores que o pivot
    biggers = [i for i in array[1:] if i > pivot] # Subarray de elementos maiores que o pivot

    return quick_sort(smallers) + [pivot] + quick_sort(biggers)
