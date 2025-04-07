def is_valid(isbn: str) -> bool:
    """Validate an ISBN-10 string (with or without hyphens).
    
    Args:
        isbn (str): A string representing the ISBN-10 to validate.

    Returns:
        bool: True if the ISBN is valid, False otherwise.
    
    Examples:
    >>> is_valid("3-598-21508-8")
    True
    >>> is_valid("3-598-21507-X")
    True
    >>> is_valid("3-598-21507-A")
    False

    Performance:
        Time complexity: O(n), where n = 10 (fixed length), so it's constant time.
        Space complexity: O(1), no extra space needed apart from a few vars.
    """
    print(f"Raw input: {isbn}")
    
    # Remove hyphens
    isbn = isbn.replace("-", "")
    print(f"Cleaned input: {isbn}")

    if len(isbn) != 10:
        print("Invalid length")
        return False

    total = 0

    for i in range(10):
        char = isbn[i]
        if i == 9 and char.upper() == 'X':
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            print(f"Invalid character at position {i}: {char}")
            return False

        weight = 10 - i
        product = value * weight
        total += product

    result = total % 11 == 0
    return result

#  Assertions for testing
assert is_valid("3-598-21508-8") == True
assert is_valid("3-598-21507-X") == True
assert is_valid("359821507X") == True
assert is_valid("3598215079") == False
assert is_valid("3-598-21507-A") == False
assert is_valid("123456789X") == True
assert is_valid("1234567890") == False
assert is_valid("3-598-21508") == False  # too short

print("\nAll tests passed!")