from typing import List, Any
import pytest

def find_anagrams(word: str, candidates: List[str]) -> list:
    """
    Find anagrams of a given word from a list of candidate words.
    An anagram is a rearrangement of letters to form a new word.
    
    This function takes a target word and a list of candidate words, 
    and returns a list of candidates that are anagrams of the target word. 
    The comparison is case-insensitive, but the returned anagrams maintain
    their original case. 

    Args:
        word (str): The target word to find anagrams for.
        candidates (List[str]): A list of candidate words to check against the target word.

    Returns:
        list: A list of candidate words that are anagrams of the target word.

    Example:
        >>> find_anagrams("stone", ["stone", "tones", "banana", "tons", "notes", "Seton"])
        ["tones", "notes", "Seton"]

    Performance:
        - Time complexity: O(n * m log m), where n is the number of candidate words and m is the length of the longest candidate word.
        - Space complexity: O(n * m), where n is the number of candidate words and m is the length of the longest candidate word.
    """
    # Handle empty candidates list
    if not candidates:
        return []
    
    # Sort the letters of the target word in lowercase for comparison
    # Create a list of sorted words in lowercase
    sorted_word = sorted(word.lower())
    
    # Initialize result list
    result = []
    
    # Check each candidate
    for candidate in candidates:
        # Skip non-string candidates
        if not isinstance(candidate, str):
            continue
            
        # Skip if candidate is the same word (case-insensitive)
        if candidate.lower() == word.lower():
            continue
            
        # Sort the letters of the candidate in lowercase
        # Create a list of sorted candidates charachters in lowercase
        sorted_candidate = sorted(candidate.lower())
        
        # If the sorted letters match, it's an anagram
        if sorted_word == sorted_candidate:
            result.append(candidate)
            
    return result


# Tests
def test_find_anagrams():
    assert find_anagrams("stone", ["stone", "tones", "banana", "tons", "notes", "Seton"]) == ["tones", "notes", "Seton"]
    
    # Empty list test
    assert find_anagrams("word", []) == []
    
    # No anagrams test
    assert find_anagrams("hello", ["world", "goodbye"]) == []
    
    # Case insensitivity test
    assert find_anagrams("Listen", ["Silent", "LISTEN", "enlist"]) == ["Silent", "enlist"]
    
    # Non-string elements test
    assert find_anagrams("abc", ["abc", "cab", 123, "bca"]) == ["cab", "bca"]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_find_anagrams()