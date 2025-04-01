def steps(number: int) -> int:
    """Determine the number of steps to reach one following these rules:
        - If number is even, divide by 2,
        - If number is off, multiply by 3 and add 1
    
    Args:
        - Numbers: An integer, that cant be 0 or negative.
    
    Return:
        - An integer equal to the number of steps to reach 1.
        
    Examples:
        - 12 ➜ 6 ➜ 3 ➜ 10 ➜ 5 ➜ 16 ➜ 8 ➜ 4 ➜ 2 ➜ 1
        Return 9 because it took 9 steps from 6 to reach 1    
    """
    
    if not number > 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    
    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        count += 1
    return count


print(steps(12))