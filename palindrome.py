def palindrome_reorder(string: str):
    """
        Retorna una cadena que resulta de reordenar los caracteres de `string`
        de tal forma que se pueda formar un palíndromo. Si esto no es posible,
        retorna "NO SOLUTION".
    """
    length = len(string)
    palindrome_list = [ "" for i in range(length) ]
    # Primero, relacionamos cada caracter de `string` 
    # con la cantidad de veces que aparece
    char_frequencies = {}
    for char  in string:
        if char in char_frequencies:
            char_frequencies[char] += 1
        else:
            char_frequencies[char] = 1

    # Ahora, por cada carácter
    middle_char = None
    for i, char in enumerate(char_frequencies.keys()):
        # Si la frecuencia es impar
        if char_frequencies[char] % 2 == 1:
            # Nos aseguramos de establecer
            # el caracter de en medio, de no existir
            if not middle_char :
                middle_char = char
            else:
            # Si se llega a este punto, existe
            # más de un caracter con una frecuencia impar.
            # Por lo tanto, no se puede realizar un palíndromo.
                return "NO SOLUTION"
        
        palindrome_list[i] = char
        palindrome_list[length - i - 1] = char

    if middle_char:
        palindrome_list[length // 2] = middle_char

    return "".join(palindrome_list)


assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
assert palindrome_reorder("neuqeun") == "neuquen", "Error en el caso de prueba"
assert palindrome_reorder("bbcccaa") == "bcacacb", "Error en el caso de prueba"
assert palindrome_reorder("anilnia") == "anilina", "Error en el caso de prueba"
assert palindrome_reorder("asdasdsad") == "NO SOLUTION", "Error en el caso de prueba"

print("Todas las pruebas pasaron")
