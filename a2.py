def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1) > len(dna2):
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if the sequence contains the proper DNA elements

    >>> is_valid_sequence("GAT")
    True
    >>> is_valid_sequence("PEDO")
    False
    """
    A = dna.count("A")
    T = dna.count("T")
    C = dna.count("C")
    G = dna.count("G")
    nucleotides = A + T + C + G
    if nucleotides < len(dna):
        return False
    else:
        return True


def insert_sequence(dna1, dna2, ind):
    """(str, str, int) -> str

    Return a string with the combination of the 2 DNA sequences, the index int shows where the dna2 will be inserted

    >>> insert_sequence("CCGG", "AT", 2)
    "CCATGG"

    >>> insert_sequence("CC", "A", 2)
    "CCA"
    """
    return dna1[:ind]+ dna2 + dna1[ind:]


