def is_isogram(string: str) -> bool:
    """Determine if a word or phrase is an isogram. An isogram 
    (also known as a "non-pattern word") is a word or phrase 
    without a repeating letter, however spaces and hyphens 
    are allowed to appear multiple times.
    
    Args:
        - string: the text to check for isogram
    
    Return:
        - True if it is an isogram.
        - False, otherwise.
        
    Examples:
        >>> is_isogram("lumberjacks")
        True       
    """
    string = string.lower()
    letters = [c for c in string if c.isalpha()]
    return len(letters) == len(set(letters))
