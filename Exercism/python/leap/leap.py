def leap_year(year: int) -> bool:
    """Determine if a given year is a leap year in the Gregorian calendar.
    
    A leap year occurs:
    - In every year that is evenly divisible by 4
    - Unless the year is evenly divisible by 100, in which case it's only a leap
      year if the year is also evenly divisible by 400
    
    Args:
        year: The year to check
        
    Returns:
        bool: True if the year is a leap year, False otherwise
        
    Examples:
        >>> leap_year(1997)
        False
        >>> leap_year(1900)
        False
        >>> leap_year(2000)
        True
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
    #return year % 4 ==0 and year % 100 !=0 or year % 4 == 0