"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return 'un' + word 


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string.

    The string consists of the prefix followed by the words with prefix prepended,
    separated by ' :: '.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with prefix applied.
    """
    
    prefix = vocab_words[0]
    
    # Start with the prefix as first word
    result = [prefix]
    
    # Add prefix to each remaining word
    for word in vocab_words[1:]:
        #concatenate strings
        result.append(prefix + word)
        
    # Join all words with ' :: ' separator
    return ' :: '.join(result)



def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    # Store the result in a variable
    result = word
    
    if word[-5:] == "iness":
        result = word[:-5] + "y"
    elif word[-4:] == "ness":  # Use elif instead of else with condition
        result = word[:-4]
        
    return result



def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    #Step 1 = Split the sentence that is a unique string into substrings
    #This built-in always returns a list of string
    #Using such method without argument will split on any whitespace but in our case, 
    # the aarg " " would have worked too as we dont care of \n.
    
    sentence = sentence.rstrip('.')
    words = sentence.split()
    word = words[index]
    
    return word + 'en'
