def score(x: float, y: float) -> int:
    """Calculate the points scored in a single toss of a Darts game.
        - If the dart lands outside the target, player earns no points (0 points).
        - If the dart lands in the outer circle of the target, player earns 1 point.
        - If the dart lands in the middle circle of the target, player earns 5 points.
        - If the dart lands in the inner circle of the target, player earns 10 points.
    
    Args:
        x: x-coordinate of where the dart lands
        y: y-coordinate of where the dart lands
    
    Note:
        - The outer circle has a radius of 10 units
        - The middle circle has a radius of 5 units
        - The inner circle has a radius of 1 unit
        - The circles are concentric defined by the coordinates (0, 0)
    
    Returns:
        The points earned by a dart landing at point (x, y)
    """
    # Calculate distance from center using Pythagorean theorem
    distance = (x**2 + y**2)**0.5
    
    # Check which circle the dart lands in
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0
        
