def max_value(array: list[int]) -> int:
    if len(array) == 2: # Caso base
        if array[0] > array[1]:
            return array[0]
        
        return array[1]

    sub_max = max_value(array[1:])

    if array[0] > sub_max:
        return array[0]

    return sub_max
