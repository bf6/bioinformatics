complements = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def ReverseComplement(pattern: str):
    """
    Returns the reverse complement of `pattern`

    Ex:
    > ReverseComplement('AATACG')
    > 'CGTATT'
    """
    complement = "".join([complements[b] for b in pattern])
    return complement[::-1]
