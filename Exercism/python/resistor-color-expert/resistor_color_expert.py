from typing import List
import pytest

def resistor_label(colors: List[str]) -> str:
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

    tolerance_dict = {
        "grey": '0.05',
        "violet": '0.1',
        "blue": '0.25',
        "green": '0.5',
        "brown": '1',
        "red": '2',
        "gold": '5',
        "silver": '10'
    }

    if not isinstance(colors, list) or not all(isinstance(c, str) for c in colors):
        raise TypeError("Input must be a list of strings.")

    if len(colors) not in [1, 3, 4, 5]:
        raise ValueError("Invalid number of color bands.")

    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    try:
        digits = [color_dict[c] for c in colors[:-2]]
        multiplier = color_dict[colors[-2]]
        tolerance = tolerance_dict[colors[-1]]
    except KeyError as e:
        raise ValueError(f"Invalid color: {e}")

    if len(colors) == 3:
        value = (10 * digits[0] + digits[1]) * (10 ** digits[2])
    elif len(colors) == 4:
        value = (10 * digits[0] + digits[1]) * (10 ** multiplier)
    elif len(colors) == 5:
        value = (100 * digits[0] + 10 * digits[1] + digits[2]) * (10 ** multiplier)

    # Choose unit and convert value to float for formatting
    value_display = float(value)
    if value >= 1_000_000:
        value_display /= 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        value_display /= 1_000
        unit = "kiloohms"
    else:
        unit = "ohms"

    # Format with up to 2 decimal places if needed
    value_str = (
        f"{int(value_display)}"
        if value_display.is_integer()
        else f"{value_display:.2f}".rstrip('0').rstrip('.')
    )
    result = f"{value_str} {unit}"

    if len(colors) in [4, 5]:
        result += f" ±{tolerance}%"

    return result

#**********************************************************************
#                               TEST                                  * 
#**********************************************************************
def test_label_ohms():
    assert resistor_label(['orange', 'orange', 'black']) == "33 ohms"
    assert resistor_label(['brown', 'black', 'black']) == "10 ohms"

def test_label_kiloohms():
    assert resistor_label(['orange', 'orange', 'red']) == "3.3 kiloohms"
    assert resistor_label(['blue', 'green', 'yellow']) == "650 kiloohms"

def test_label_megaohms():
    assert resistor_label(['green', 'black', 'white']) == "50 megaohms"

def test_invalid_color():
    with pytest.raises(ValueError):
        resistor_label(['banana', 'green', 'red'])

def test_too_few_colors():
    with pytest.raises(ValueError):
        resistor_label(['brown'])

def test_empty_input():
    with pytest.raises(ValueError):
        resistor_label([])

def test_invalid_type():
    with pytest.raises(TypeError):
        resistor_label({'brown', 'green', 'red'})

def test_tolerance():
    assert resistor_label(["orange", "orange", "blue", "red"]) == "33 megaohms ±2%"
    assert resistor_label(["orange", "orange", "black", "red"]) == "33 ohms ±2%"
    assert resistor_label(["blue", "grey", "brown", "violet"]) == "680 ohms ±0.1%"
    assert resistor_label(["orange", "orange", "yellow", "black", "brown"]) == "334 ohms ±1%"
    assert resistor_label(["red", "green", "yellow", "yellow", "brown"]) == "2.54 megaohms ±1%"
    assert resistor_label(["blue", "grey", "white", "brown", "brown"]) == "6.89 kiloohms ±1%"
    assert resistor_label(["brown", "black", "brown", "yellow", "violet"]) == "1.01 megaohms ±0.1%"