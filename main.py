import algorithms
import random


if __name__ == '__main__':
    array = [random.randint(1, 100) for _ in range(10)]
    print(array)
    print(algorithms.quick_sort(array))
