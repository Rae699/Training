def is_pangram(sentence):
    """Determine if a sentence is a pangram.
    
    Args:
        sentence (str): A string.
    
    Returns:
        bool: True if the sentence contains all 26 letters of the alphabet at least once, False otherwise.
    
    Examples:
    >>> is_pangram("The quick brown fox jumps over the lazy dog")
    True
    """
    sentence_lowercase = sentence.lower()
    
    letters_in_sentence = set()
    for letter in sentence_lowercase:
        if letter.isalpha():  # only consider letters
            letters_in_sentence.add(letter)
    
    return len(letters_in_sentence) == 26

    #Pythonic way using comprehension
    # return len(set(char for char in sentence.lower() if char isalpha())) == 26