from typing import List
import pytest

def label(colors: List[str]) -> str:
    if len(colors) != 3:
        raise ValueError("Exactly three color bands are required")

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

    try:
        a = color_dict[colors[0]]
        b = color_dict[colors[1]]
        multiplier = color_dict[colors[2]]
    except KeyError as e:
        raise ValueError(f"Invalid color: {e}")

    raw_value = (10 * a + b) * (10 ** multiplier)

    # Determine appropriate unit
    if raw_value >= 1_000_000_000:
        display_value = raw_value / 1_000_000_000
        unit = "gigaohms"
    elif raw_value >= 1_000_000:
        display_value = raw_value / 1_000_000
        unit = "megaohms"
    elif raw_value >= 1_000:
        display_value = raw_value / 1_000
        unit = "kiloohms"
    else:
        display_value = raw_value
        unit = "ohms"

    if float(display_value).is_integer():
        return f"{int(display_value)} {unit}"
    else:
        return f"{display_value:.1f} {unit}"


#**********************************************************************
#                               TEST                                  * 
#**********************************************************************
def test_label_ohms():
    assert label(['orange', 'orange', 'black']) == "33 ohms"
    assert label(['brown', 'black', 'black']) == "10 ohms"

def test_label_kiloohms():
    assert label(['orange', 'orange', 'red']) == "3.3 kiloohms"
    assert label(['brown', 'black', 'yellow']) == "100 kiloohms"

def test_label_megaohms():
    assert label(['green', 'black', 'white']) == "50 megaohms"

def test_invalid_color():
    with pytest.raises(ValueError):
        label(['banana', 'green', 'red'])

def test_too_few_colors():
    with pytest.raises(ValueError):
        label(['brown'])

def test_empty_input():
    with pytest.raises(ValueError):
        label([])

def test_invalid_type():
    with pytest.raises(TypeError):
        label({'brown', 'green', 'red'})