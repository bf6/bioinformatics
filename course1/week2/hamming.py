import pyperclip
from collections import defaultdict

BASES = ['A','C','T','G']

COMPLEMENTS = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def reverse_complement(pattern):
    complement = "".join([COMPLEMENTS[b] for b in pattern])
    return complement[::-1]

def hamming(first: str, second: str):
    """
    Compare hamming distance between first and second strings
    """
    if len(first) != len(second):
        raise Exception('Strings must be of equal length')
    distance = 0
    for i in range(0,len(first)):
        if first[i] != second[i]:
            distance += 1
    return distance

def approx_match(pattern: str, text: str, distance: int):
    """
    Return indexes of all instances of `text` in `pattern` with a
    hamming distance of `distance`
    """
    if distance > len(pattern):
        raise Exception('Distance greater than length of pattern')
    indexes = []
    for i in range(0, len(text) - len(pattern) + 1):
        if hamming(pattern, text[i:i+len(pattern)]) <= distance:
            indexes.append(i)
    return indexes

def countd(pattern: str, text: str, distance: int):
    """
    Return the times `pattern` appears in `text` with at most
    hamming distance `distance`
    """
    return len(approx_match(pattern, text, distance))

def neighbors(pattern: str, d: int):
    """
    Find all neighbors to `pattern` with at most `d` hamming distance
    """
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A','C','G','T']
    neighborhood = []
    suffix_neighbors = neighbors(pattern[1:], d)
    for string in suffix_neighbors:
        if hamming(pattern[1:], string) < d:
            for base in BASES:
                neighborhood.append(base + string)
        else:
            neighborhood.append(pattern[0] + string)
    return neighborhood

def frequent_words(text: str, k: int, d: int):
    """
    Find most frequent `k`-mers in `text` with max hamming distance `d`
    """
    freq_words = defaultdict(int)
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]
        neighbs = neighbors(pattern, d)
        for neighb in neighbs:
            if hamming(pattern, neighb) <= d:
                freq_words[neighb] += 1
    freq_words = dict(freq_words)
    max_val = 0
    for k, v in freq_words.items():
        if v > max_val:
            max_val = v
    freq_words = " ".join([k for k, _ in freq_words.items() if _ == max_val])
    pyperclip.copy(freq_words)
    return freq_words

def frequent_words_reverse_complement(text: str, k: int, d: int):
    """
    Like frequent_words but also counts reverse complements
    """
    kmers = defaultdict(int)
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]
        neighbs = neighbors(pattern, d)
        for n in neighbs:
            kmers[n] += 1
            kmers[reverse_complement(n)] += 1
    freq_words = dict(kmers)
    max_val = 0
    for k, v in freq_words.items():
        if v > max_val:
            max_val = v
    freq_words = " ".join(sorted([k for k, _ in freq_words.items() if _ == max_val]))
    pyperclip.copy(freq_words)
    return freq_words
