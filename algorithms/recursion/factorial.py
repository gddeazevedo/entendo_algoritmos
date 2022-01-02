def factorial(n: int) -> int | str:
    if n < 0:
        return 'Does not exist factorial of negative number'

    if n == 1 or n == 0:
        return 1

    return n * factorial(n - 1)
