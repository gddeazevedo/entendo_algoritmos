from typing import Any


def binary_search(array: list[Any], item: Any) -> Any | None:
    low = 0 # follows the list part we're searching
    high = len(array) - 1 # follows the list part we're searching

    while low <= high:
        half = (low + high) // 2 # half of the array
        guess = array[half] # checks the central element

        if guess == item: # Item was found
            return half
        elif guess >= item: # Guess is too high
            high = half - 1
        else: # Guess is too low
            low = half + 1

    return None # No item was found
