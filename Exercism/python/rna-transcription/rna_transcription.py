def to_rna(dna_strand: str) -> str:
    """Determine the RNA complement of a given DNA sequence.

    Args:
        - dna_strand: A string of DNA nucleotides.

    Returns:
        - A string containing the RNA complements of the DNA nucleotides.

    Raises:
        - ValueError: If an invalid character is found.

    Example:
    >>> to_rna('ACGTGGTCTTAA')
    'UGCACCAGAAUU'

    Performance:
        - Time: O(n), where n is the length of dna_strand
        - Space: O(n), for storing the output RNA string
    """
    
    if not dna_strand:
        raise ValueError("DNA strand is empty")

    dna_to_rna = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }

    rna_strand = []
    for nucleotide in dna_strand:
        if nucleotide not in dna_to_rna:
            raise ValueError(f"Invalid nucleotide found: {nucleotide}")
        rna_strand.append(dna_to_rna[nucleotide])

    return ''.join(rna_strand)


# Test
assert to_rna('ACGTGGTCTTAA') == 'UGCACCAGAAUU', 'Invalid match of protein'