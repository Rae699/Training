def classify(number: int) -> str:
    """Classify a number as 'perfect', 'abundant', or 'deficient' based on its aliquot sum."""
    
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    # Calculate aliquot sum: sum of all divisors of `number` except itself
    aliquot_sum = 0
    for i in range(1, number):
        if number % i == 0:
            aliquot_sum += i

    # Classify based on comparison
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"