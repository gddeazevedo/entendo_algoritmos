from typing import Any


def get_smallest_element_index(array: list[Any]) -> int:
    smallest_element_index = 0 # Current smallest element index
    smallest_element = array[0] # Current smallest element

    for index in range(1, len(array)):
        if array[index] < smallest_element:
            smallest_element = array[index]
            smallest_element_index = index

    return smallest_element_index


def selection_sort(array: list[Any]) -> list:
    new_array = []

    for _ in range(len(array)):
        smallest_index = get_smallest_element_index(array) # Find the smallest element index
        new_array.append(array.pop(smallest_index))

    return new_array
