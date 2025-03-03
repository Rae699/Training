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
    return ' :: '.join([prefix] + [f"{prefix}{word}" for word in vocab_words[1:]])


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    root = word[:-4]  # Remove 'ness' suffix (4 characters)
    if root.endswith('i'):
        return root[:-1] + 'y'
    return root


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    words = sentence.split()
    adjective = words[index].rstrip('.,!?;:')  # Remove trailing punctuation
    return adjective + 'en' 