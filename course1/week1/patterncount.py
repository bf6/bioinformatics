from collections import defaultdict

def PatternCount(genome: str, pattern: str):
    """
    Return count of occurrences of `pattern` in `genome`
    """
    count = 0
    k = len(pattern)
    for x in range(0, len(genome) - k + 1):
        if genome[x:x+k] == pattern:
            count += 1
    return count

def FrequentPatterns(genome: str, k: int):
    """
    Return most frequent kmers of length `k` in `genome`
    """
    frequent_patterns = defaultdict(int)
    for x in range(0, len(genome) - k + 1):
        frequent_patterns[genome[x:x+k]] += 1
    max_count = max(frequent_patterns.values())
    most_frequent = {k:v for k,v in frequent_patterns.items() if v == max_count}
    return " ".join([m for m in most_frequent])
