from typing import Any


def binary_search(array: list[Any], item: Any) -> Any | None:
    low = 0
    high = len(array) - 1

    while low <= high:
        half = (high + low) // 2
        guess = array[half] # check central element

        if guess == item: # Item is found
            return half
        elif guess > item: # Guess is greater than the item
            high = half - 1
        else: # Guess is smaller than the item
            low = half + 1

    return None
