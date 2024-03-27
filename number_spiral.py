def number_spiral(row: int, col: int) -> int:
    """
        Retorna el elemento de la columna `col` y fila `row`
        de una matriz espiral como la siguiente:

        1  | 2  | 9   | 10 | 25
        4  | 3  | 8   | 11 | 24
        5  | 6  | 7   | 12 | 23
        16 | 15 | 14  | 13 | 22    
        17 | 18 | 19  | 20 | 21
    """
    max_index = max(row, col)
    min_index = min(row, col)
    # Podemos calcular el elemento de la diagonal (index, index)
    # fijándonos que (index - 1)**2 es el valor máximo de la submatriz
    # cuadrada de longitud index - 1. La cantidad de posiciones
    # a agregar es igual al index en sí.
    closest_diagonal_value = (max_index-1)**2 + max_index
    if row == col: 
        return closest_diagonal_value

    # Ahora podemos calcular el valor buscado
    # moviéndonos a través del brazo de la espiral en la 
    # dirección correcta

    direction = None
    # Si el índice máximo es par...
    if max_index % 2 == 0:
        # La dirección del brazo es negativa
        direction = -1
    else: 
        # Si no,
        # La dirección del brazo es positiva
        direction = 1
    
    # Si la fila es mayor que la columna, 
    # hay que moverse a través de las filas,
    # en dirección contraria a la del brazo.
    if col < row:
        direction = -direction

    return closest_diagonal_value + ((max_index - min_index) * direction)

assert number_spiral(1, 1) == 1, number_spiral(1, 1)
assert number_spiral(2, 1) == 4, number_spiral(2, 1)
assert number_spiral(3, 1) == 5, number_spiral(3, 1)
assert number_spiral(4, 1) == 16, number_spiral(4,1)
assert number_spiral(1, 2) == 2, number_spiral(1, 2)
assert number_spiral(2, 2) == 3, number_spiral(2, 2)
assert number_spiral(3, 2) == 6, number_spiral(3, 2)
assert number_spiral(4, 2) == 15, number_spiral(4, 2)

assert number_spiral(4, 3) == 14, number_spiral(4, 3)
assert number_spiral(1, 3) == 9, number_spiral(1, 3)

print("Todas las pruebas pasaron")


