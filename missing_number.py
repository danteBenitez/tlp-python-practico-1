def missing_number(count: int, number_list: list[int]) -> int:
    """
        Dada una cantidad de elementos `count`, y una lista que va
        desde 1 hasta `count`, encuentra el primer número faltante.
    """
    # El número que falta es la suma de los números de 1 hasta `count`
    # menos la suma de los que están en la lista.
    return sum(range(1, count + 1)) - sum(number_list)

assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
assert missing_number(3, [1, 3]) == 2, "Error en el caso de prueba"
assert missing_number(3, [1, 2]) == 3, "Error en el caso de prueba"
assert missing_number(4, [1, 3, 4]) == 2, "Error en el caso de prueba"

print("Todas las pruebas pasaron")
