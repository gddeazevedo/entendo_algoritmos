from typing import Any


def merge(array_1: list[Any], array_2: list[Any]) -> list[Any]:
    new_array = []

    while array_1 != [] and array_2 != []:
        if array_1[0] < array_2[0]:
            new_array.append(array_1.pop(0))
        else:
            new_array.append(array_2.pop(0))

    return new_array + array_1 + array_2


def merge_sort(array: list[Any]) -> list[Any]:
    if len(array) < 2:
        return array

    n = len(array)
    half = (n - 1) // 2

    array_1 = merge_sort(array[:half+1])
    array_2 = merge_sort(array[half+1:n])

    return merge(array_1, array_2)
