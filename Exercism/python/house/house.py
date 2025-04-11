def recite(start_verse, end_verse):
    """
    Recite the nursery rhyme 'This is the House that Jack Built'.
    Constructs verses recursively by embedding previous phrases.
    """
    
    subjects = [
        "the house that Jack built.",
        "the malt",
        "the rat",
        "the cat",
        "the dog",
        "the cow with the crumpled horn",
        "the maiden all forlorn",
        "the man all tattered and torn",
        "the priest all shaven and shorn",
        "the rooster that crowed in the morn",
        "the farmer sowing his corn",
        "the horse and the hound and the horn"
    ]
    
    actions = [
        "",  # no action for the base case
        "that lay in",
        "that ate",
        "that killed",
        "that worried",
        "that tossed",
        "that milked",
        "that kissed",
        "that married",
        "that woke",
        "that kept",
        "that belonged to"
    ]
    
    def build_verse(n):
        """Build a single verse recursively."""
        if n == 0:
            return f"This is {subjects[0]}"
        else:
            lines = [f"This is {subjects[n]}"]
            for i in range(n, 0, -1):
                lines.append(f"{actions[i]} {subjects[i - 1]}")
            return "\n".join(lines)

    # Return the list of verses from start_verse to end_verse
    return [build_verse(i - 1) for i in range(start_verse, end_verse + 1)]