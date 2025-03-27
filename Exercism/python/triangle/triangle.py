def is_triangle(sides: list[float]) -> bool:
    """Determine if the sides can form a valid triangle.
    
    A triangle is valid if:
    - It has exactly 3 sides
    - All sides are positive
    - The sum of any two sides is greater than the third side
    
    Args:
        sides: List of three numbers representing triangle sides
        
    Returns:
        bool: True if it forms a valid triangle, False otherwise
        
    Examples:
        >>> is_triangle([2, 2, 2])
        True
        >>> is_triangle([0, 0, 0])
        False
        >>> is_triangle([1, 1, 3])
        False
    """
    # Check if it has exactly 3 sides in the list provided as arg
    if len(sides) != 3:
        return False
        
    # Unpack each side
    a, b, c = sides
    
    # Bool test, hence we prefer using not so we can express properly the test
    if not all(side > 0 for side in sides):
        return False
    
    # Bool test of the sides
    return a + b > c and b + c > a and a + c > b


def equilateral(sides: list[float]) -> bool:
    """Determine if a triangle is equilateral (all sides equal).
    
    Args:
        sides: List of three numbers representing triangle sides
        
    Returns:
        bool: True if all sides are equal, False otherwise
        
    Examples:
        >>> equilateral([2, 2, 2])
        True
        >>> equilateral([2, 3, 2])
        False
    """
    #Check for the shape to be a triangle
    if not is_triangle(sides):
        return False
        
    # Return true if the check above was false (inner) and, 
    # there is only one length for set(sides), as a set contains unique value only
    return len(set(sides)) == 1


def isosceles(sides: list[float]) -> bool:
    """Determine if a triangle is isosceles (at least 2 sides equal).
    
    Args:
        sides: List of three numbers representing triangle sides
        
    Returns:
        bool: True if at least 2 sides are equal, False otherwise
        
    Examples:
        >>> isosceles([2, 2, 1])
        True
        >>> isosceles([2, 3, 4])
        False
    """
    #Check for the shape to be a triangle
    if not is_triangle(sides):
        return False
    
    # Return true if the check above was false (inner) and, 
    # there is max 2 sides in the set, as a set contains unique value only   
    return len(set(sides)) <= 2


def scalene(sides: list[float]) -> bool:
    """Determine if a triangle is scalene (no sides equal).
    
    Args:
        sides: List of three numbers representing triangle sides
        
    Returns:
        bool: True if no sides are equal, False otherwise
        
    Examples:
        >>> scalene([3, 2, 1])
        True
        >>> scalene([2, 3, 2])
        False
    """
    #Check for the shape to be a triangle
    if not is_triangle(sides):
        return False
    
    # Return true if the check above was false (inner) and, 
    # there is exactly 3 sides in the set, as a set contains unique value only   
    return len(set(sides)) == 3







#**********************************************************************
#       Using a decoreator to wrap the lower order functions 
#                   and test for is_triangle 
#**********************************************************************

def is_triangle(sides: list[float]) -> bool:
    """Determine if the sides can form a valid triangle.
    
    A triangle is valid if:
    - It has exactly 3 sides
    - All sides are positive
    - The sum of any two sides is greater than the third side
    
    Args:
        sides: List of three numbers representing triangle sides
        
    Returns:
        bool: True if it forms a valid triangle, False otherwise
        
    Examples:
        >>> is_triangle([2, 2, 2])
        True
        >>> is_triangle([0, 0, 0])
        False
        >>> is_triangle([1, 1, 3])
        False
    """
    # Check if it has exactly 3 sides in the list provided as arg
    if len(sides) != 3:
        return False
        
    # Unpack each side
    a, b, c = sides
    
    # Bool test, hence we prefer using not so we can express properly the test
    if not all(side > 0 for side in sides):
        return False
    
    # Bool test of the sides
    return a + b > c and b + c > a and a + c > b


def triangle_validator(f: Callable[[List[float]], bool]) -> Callable[[List[float]], bool]:
    """Decorator to ensure a function only runs on valid triangles."""
    def wrapper(sides: List[float]) -> bool:
        return is_triangle(sides) and f(sides)
    return wrapper


@triangle_validator
def equilateral(sides: list[float]) -> bool:
    """Determine if a triangle is equilateral (all sides equal).
    
    Args:
        sides: List of three numbers representing triangle sides
        
    Returns:
        bool: True if all sides are equal, False otherwise
        
    Examples:
        >>> equilateral([2, 2, 2])
        True
        >>> equilateral([2, 3, 2])
        False
    """  
    # Return true if the check above was false (inner) and, 
    # there is only one length for set(sides), as a set contains unique value only
    return len(set(sides)) == 1


@triangle_validator
def isosceles(sides: list[float]) -> bool:
    """Determine if a triangle is isosceles (at least 2 sides equal).
    
    Args:
        sides: List of three numbers representing triangle sides
        
    Returns:
        bool: True if at least 2 sides are equal, False otherwise
        
    Examples:
        >>> isosceles([2, 2, 1])
        True
        >>> isosceles([2, 3, 4])
        False
    """
    # Return true if the check above was false (inner) and, 
    # there is max 2 sides in the set, as a set contains unique value only   
    return len(set(sides)) <= 2


@triangle_validator
def scalene(sides: list[float]) -> bool:
    """Determine if a triangle is scalene (no sides equal).
    
    Args:
        sides: List of three numbers representing triangle sides
        
    Returns:
        bool: True if no sides are equal, False otherwise
        
    Examples:
        >>> scalene([3, 2, 1])
        True
        >>> scalene([2, 3, 2])
        False
    """
    # Return true if the check above was false (inner) and, 
    # there is exactly 3 sides in the set, as a set contains unique value only   
    return len(set(sides)) == 3
