def response(hey_bob: str) -> str:
    """Process input and return Bob's response based on the input pattern.

    Bob is a lackadaisical teenager. In conversation, his responses are very limited.
    
    Args:
        hey_bob (str): The input string to process

    Returns:
        str: Bob's response based on the input pattern:
            - Question: "Sure."
            - Yelling: "Whoa, chill out!"
            - Yelling a question: "Calm down, I know what I'm doing!"
            - Empty or whitespace: "Fine. Be that way!"
            - Default: "Whatever."
    """
    # Remove leading/trailing whitespace
    hey_bob = hey_bob.strip()
    
    # Handle empty or whitespace-only input
    if not hey_bob:
        return "Fine. Be that way!"
    
    # Check if it's a question (ends with ?)
    is_question = hey_bob.endswith('?')
    
    # Check if it's yelling (contains letters and is all uppercase)
    is_yelling = hey_bob.isupper() and any(c.isalpha() for c in hey_bob)
    
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_yelling:
        return "Whoa, chill out!"
    else:
        return "Whatever."