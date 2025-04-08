"""
    Resistor Color Code Lookup

    This module provides functionality to interpret the color bands on resistors
    and convert them into their corresponding numerical values based on the
    standard electronic color code.

    Resistors use colored bands to indicate their resistance values. The first two
    bands represent significant digits, each color corresponding to a digit from
    0 to 9. 
"""

def color_code(color: str):
    """ Look up the numerical value associated with a specific color band.
    Color Code Reference:
        black  : 0
        brown  : 1
        red    : 2
        orange : 3
        yellow : 4
        green  : 5
        blue   : 6
        violet : 7
        grey   : 8
        white  : 9

    Mnemonic to remember the color order:
        "Better Be Right Or Your Great Big Values Go Wrong"
    Usage Example:
        >>> color_code('red')
        2
        >>> colors()
        ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    """
    
    color_dict = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    
    if not color:
        raise ValueError("No color provided!")
    
    color = color.lower()
    if color not in color_dict:
        raise ValueError(f"Invalid color: {color}")
    
    return color_dict[color]
    

def colors():
    """
    List all possible color bands in order from 0 (black) to 9 (white).
    """
    return [
            "black", "brown", "red", "orange", "yellow",
            "green", "blue", "violet", "grey", "white"
        ]


# Test cases
assert color_code('white') == 9
assert color_code('red') == 2
assert colors() == ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']