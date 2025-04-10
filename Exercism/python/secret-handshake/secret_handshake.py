from typing import List
import pytest

def commands(binary_str: str) -> List[str]:
    """
    Convert a binary string to a sequence of actions in the secret handshake.

    The sequence of actions is determined by the rightmost five digits of the binary string.
    Each digit corresponds to a specific action, and the actions are performed in the order
    of the digits from right to left. If the leftmost digit is 1, the order of actions is reversed.

    Args:
        binary_str (str): A string representing a binary number.

    Returns:
        List[str]: A list of actions corresponding to the binary string.

    Example:
        >>> commands("00011")
        ["wink", "double blink"]
        
    Performance:
        - Time complexity:
        - Space complexity:
    """
    
    if not binary_str or not isinstance(binary_str, str):
            raise ValueError("Input must be a non-empty binary string!")
    
    try:
        n = int(binary_str, 2)
    except ValueError:
        raise ValueError("Invalid binary string!")
    
    actions = [
        "wink",           # bit 0 (rightmost)
        "double blink",   # bit 1
        "close your eyes",# bit 2
        "jump"            # bit 3
    ]
    
    result = [actions[i] for i in range(4) if (n >> i) & 1]
    
    if n & (1 << 4):  # bit 4 = reverse flag
        result.reverse()

    return result

# Test
def test_handshake_commands():
    assert commands("00011") == ["wink", "double blink"]
    assert commands("10011") == ["double blink", "wink"]
    assert commands("11111") == ["jump", "close your eyes", "double blink", "wink"]
    assert commands("00000") == []

def test_invalid_input_type():
    with pytest.raises(ValueError):
        commands(11)  # not a string

def test_invalid_binary_string():
    with pytest.raises(ValueError):
        commands("12A01")

def test_empty_input():
    with pytest.raises(ValueError):
        commands("")