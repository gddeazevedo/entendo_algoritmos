def array_sum(array: list[int]) -> int:
    '''Este algoritmo utiliza a técnica de Dividir para conquistar'''

    if array == []:
        return 0 # Caso base, o mais simples possível

    # Caso recursivo, diminuindo o problema até chegar ao caso base
    return array[0] + array_sum(array[1:])
