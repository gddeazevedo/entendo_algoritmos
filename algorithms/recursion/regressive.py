def regressive(i: int):
    if i < 1:
        return # Caso base
    print(i)
    regressive(i - 1) # Caso recursivo
