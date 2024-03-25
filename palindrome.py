def palindrome_reorder(string: str):
    """
        Retorna una cadena que resulta de reordenar los caracteres de `string`
        de tal forma que se pueda formar un palíndromo. Si esto no es posible,
        retorna "NO SOLUTION".
    """
    length = len(string)
    # Una lista de caracteres que se convertirán en el palííndromo
    # resultante. Usamos una lista por la facilidad para modificarla
    # por índice.
    palindrome_list = [""] * length

    # Primero, relacionamos cada caracter de `string` 
    # con la cantidad de veces que aparece
    char_frequencies = {}
    for char  in string:
        if char in char_frequencies:
            char_frequencies[char] += 1
        else:
            char_frequencies[char] = 1
    
    # Si hay algún carácter de frecuencia impar, 
    # lo pondremos en el centro.
    middle_char = None
    # Nuestra posición actual en el palíndromo
    palindrome_list_index = 0
    # Ahora, por cada carácter
    for char in char_frequencies.keys():
        freq = char_frequencies[char]
        # Si la frecuencia es impar
        if freq % 2 == 1:
            # Nos aseguramos de establecer
            # el caracter de en medio, de no existir
            if not middle_char :
                middle_char = char
            else:
            # Si se llega a este punto, existe
            # más de un caracter con una frecuencia impar.
            # Por lo tanto, no se puede realizar un palíndromo.
                return "NO SOLUTION"
        
        # Usamos la frecuencia de caracteres obtenida
        # para agregar al palíndromo el mismo carácter
        # la cantidad correcta de veces
        for _ in range(freq // 2):
            # Colocamos el mismo caractér en la posición
            # actual, y en la posición opuesta.
            palindrome_list[palindrome_list_index] = char
            palindrome_list[length - palindrome_list_index - 1] = char

            # Nos movemos por la lista aumentando el índice
            palindrome_list_index += 1
    
    # Si encontramos un carácter de frecuencia impar
    # lo colocamos en el medio.
    if middle_char:
        palindrome_list[length // 2] = middle_char

    return "".join(palindrome_list)


assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
assert palindrome_reorder("neuqeun") == "neuquen", "Error en el caso de prueba"
assert palindrome_reorder("bbcccaa") == "bcacacb", "Error en el caso de prueba"
assert palindrome_reorder("anilnia") == "anilina", "Error en el caso de prueba"
assert palindrome_reorder("asdasdsad") == "NO SOLUTION", "Error en el caso de prueba"
assert palindrome_reorder("aabbbccc") == "NO SOLUTION", "Error en el caso de prueba"

print("Todas las pruebas pasaron")
