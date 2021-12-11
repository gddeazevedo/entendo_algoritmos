from typing import Any


def binary_search(array: list[Any], item: Any) -> Any | None:
    low = 0
    high = len(array) - 1

    while low <= high:
        half = (low + high) // 2
        guess = array[half]

        if guess == item: # Found the item
            return half
        elif guess > item: # Guess is too high
            high = half - 1
        else: # Guess is too low
            low = half + 1

    return None # Item not found
