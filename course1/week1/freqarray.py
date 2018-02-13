from collections import defaultdict
import itertools

MAP = {'A':0, 'C':1, 'G':2, 'T':3}
REVERSEMAP = {v:k for k,v in MAP.items()}
BASES = ['A','C','G','T']

def SymbolToNumber(symbol: str):
    """
    Return the decimal representation of nucleotide base `symbol`
    """
    return MAP[symbol]

def NumberToSymbol(number: int):
    """
    Return the string representation of nucleotide base `number`
    """
    return REVERSEMAP[number]

def initializeKmers(k: int):
    """
    Initialize list of all k-mers of length `k`
    """
    tuples = list(itertools.product(BASES, repeat=k))
    return ["".join(t) for t in tuples]

def PatternToNumber(pattern: str):
    """
    Return the decimal representation of nucleotide sequence `pattern`
    """
    if not pattern:
        return 0
    symbol = pattern[-1]
    prefix = pattern[0:-1]
    return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def NumberToPattern(idx: int, k: int):
    """
    Return the string representation of the nucleotide sequence
    of length `k` identified by decimal representation `idx`
    """
    if idx >= 4**k:
        return Exception('Bad input')
    pattern = ''
    quotient = idx
    remainder = 0
    for x in range(0,k):
        remainder = quotient % 4
        quotient = quotient / 4
        pattern += NumberToSymbol(remainder)
    return pattern[::-1]

def ComputingFrequencies(genome: str, k: int):
    """
    Return the frequency array for words of length `k` in `genome`
    """
    freq_array = {p:0 for p in initializeKmers(k)}
    for x in range(0, len(genome) - k + 1):
        freq_array[genome[x:x+k]] += 1
    return " ".join([str(x) for x in freq_array.values()])

