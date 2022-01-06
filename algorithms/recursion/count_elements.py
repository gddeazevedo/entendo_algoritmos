def count_elements(array: list[int]) -> int:
    if array == []:
        return 0

    return 1 + count_elements(array[1:])
