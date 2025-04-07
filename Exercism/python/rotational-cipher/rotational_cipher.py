import string

def rotate(text: str, key: int) -> str:
    """
    Applies a Caesar cipher (rotational cipher) to the input text using the specified key.

    The Caesar cipher shifts each letter by a fixed number of positions in the alphabet.
    It preserves the case of letters and leaves non-alphabetic characters unchanged.

    Args:
        text (str): The input string to be encrypted.
        key (int): The shift amount (0-26). A key of 0 or 26 returns the original string.

    Returns:
        str: The encrypted string with characters shifted by the given key.

    Examples:
        >>> rotate("omg", 5)
        'trl'
        >>> rotate("c", 0)
        'c'
        >>> rotate("Cool", 26)
        'Cool'
        >>> rotate("The quick brown fox jumps over the lazy dog.", 13)
        'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.'

    Performance:
        - Time complexity: O(n), where n is the length of the input string.
        - Space complexity: O(n) for storing the resulting string.
    """

    # Input validations
    assert isinstance(text, str), "Input text must be a string."
    assert isinstance(key, int), "Key must be an integer."
    assert 0 <= key <= 26, "Key must be in the range [0, 26]."

    result = []

    for char in text:
        if char.islower():
            # Shift within lowercase letters
            index = (ord(char) - ord('a') + key) % 26
            result.append(chr(ord('a') + index))
        elif char.isupper():
            # Shift within uppercase letters
            index = (ord(char) - ord('A') + key) % 26
            result.append(chr(ord('A') + index))
        else:
            # Keep non-alphabet characters unchanged
            result.append(char)

    return ''.join(result)