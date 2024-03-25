def missing_number(count: int, number_list: list[int]) -> int:
    """
        Dada una cantidad de elementos `count`, y una lista que va
        desde 1 hasta `count`, encuentra el primer número faltante.
    """
    # Por cada número desde cero hasta `count`...
    for i in range(count):
        # Como el primer elemento (1) está en la posición cero,
        # la posición i debe coincidir con i + 1.
        if number_list[i] != i + 1:
            # Si no coincide, encontramos el número faltante 
            # y lo retornamos.
            return i + 1

assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
assert missing_number(3, [1, 3]) == 2, "Error en el caso de prueba"
assert missing_number(4, [1, 3, 4]) == 2, "Error en el caso de prueba"

print("Todas las pruebas pasaron")
