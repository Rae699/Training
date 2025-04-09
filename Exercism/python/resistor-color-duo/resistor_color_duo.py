from typing import List
import pytest

def value(colors: List[str]) -> int:
    """Take color names as input and output a two-digit number
    based on the first two colors.

    Args:
        colors (list): A list of color names (strings).

    Returns:
        int: The resistor color code of the first two colors.

    Raises:
        ValueError: If the color list is empty or contains an invalid color.

    Examples:
    >>> value(['brown', 'green'])
    15
    >>> value(['brown', 'green', 'violet'])
    15
    
    Performance:
        - Time: O(1), since only first two elements are checked in constant time
        - Space: O(1), constant dictionary and no extra data structures
    """

    if not colors:
        raise ValueError('Colors list is empty!')

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

    # Only care about the first two colors
    try:
        a = color_dict[colors[0]]
        b = color_dict[colors[1]]
    except KeyError as e:
        raise ValueError(f'Invalid color: {e.args[0]}') from e
    except IndexError:
        raise ValueError('At least two colors are required!')
    return int(f"{a}{b}")

#**** TEST
def test_value_basic():
    assert value(['brown', 'green']) == 15
    assert value(['brown', 'green', 'violet']) == 15
    assert value(['black', 'white']) == 9
    assert value(['red', 'blue']) == 26

def test_value_invalid_color():
    with pytest.raises(ValueError):
        value(['banana', 'green'])

def test_value_too_short():
    with pytest.raises(ValueError):
        value(['brown'])
