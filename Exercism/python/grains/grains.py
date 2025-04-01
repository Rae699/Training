def square(number: int) -> int:
    """Determine the number of grains on a specific square of the chessboard.

    Args:
        number (int): The specific square we are looking for the number 
        of grains stored on.

    Returns:
        int: Number of grains on that specific square.
        
    Raises:
        ValueError: If the square number is not between 1 and 64.
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
        
    chessboard = range(1, number + 1, 1)
    grain = 0
    
    for square in chessboard:
        if square == 1:
            grain = 1
        else:
            grain *= 2
            
    return grain


def total() -> int:
    """Determine the total number of grains on the chessboard.

    Returns:
        int: Total number of grains on all 64 squares of the chessboard
    """

    # # Using a list comprehension
    # return sum([square(n) for n in range(1, 65)])

    # Using a regular loop
    total = 0
    for n in range(1, 65):
        total += square(n)
    return total
