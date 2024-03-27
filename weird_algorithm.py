def weird_algorithm(start_number: int):
    """
        Crea una lista a partir de la aplicación de las siguientes reglas:
            - n comienza siendo start_number
            - Si n es par, el nuevo valor es n / 2
            - Si n es impar, el nuevo valor de n es 3*n + 1
            - Si n es uno, termina el algoritmo.
    """
    assert start_number > 0, "`start_number` debe ser positivo."
    current_number = start_number
    number_list = [current_number]
    while current_number != 1:
        # Si n es par
        if current_number % 2 == 0:
            # Se divide por 2
            current_number = current_number // 2
        else:
            # Si es impar, se multiplica por 3 y se agrega 1
            current_number = 3 * current_number + 1
        # n se agrega a la lista
        number_list.append(current_number)
    return number_list

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
assert weird_algorithm(5) == [5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
assert weird_algorithm(4) == [4, 2, 1], "Error en el caso de prueba"


print("Todas las pruebas pasaron.")
