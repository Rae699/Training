def is_armstrong_number(number: int) -> bool:
    """Determine if a number is an Armstrong number.

    Args:
        number (int): The number to test.

    Returns:
        bool: True if Armstrong number, False otherwise
        
    Examples:
        - 9 is an Armstrong number, because 9 = 9^1 = 9
        - 10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
        - 153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
        - 154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
    """
    exponent = len(str(number))
    total = sum(int(n) ** exponent for n in str(number))
    
    return number == total