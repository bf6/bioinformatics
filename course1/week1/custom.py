from collections import defaultdict
import pyperclip


def import_genome_from_file(filestr: str):
    """
    Reads genome from .txt file
    """
    file = open(filestr, 'r')
    return file.read()

def get_kmers(genome: str, k: int):
    """
    Find words of length `k` (and their occurrence) in `genome`
    """
    kmers = defaultdict(int)
    for x in range(0, len(genome)):
        kmers[genome[x:x+k]] += 1
    return kmers

def get_kmers_and_indices(genome: str, k: int):
    """
    Find words of length `k` along with their occurence, first and
    last appearance in `genome`
    """
    kmers = defaultdict(lambda: {
        'occurrences': 0, 'first_position': None, 'last_position': None})
    for x in range(0, len(genome) - k + 1):
        kmer = genome[x:x+k]
        kmers[kmer]['occurrences'] += 1
        if kmers[kmer]['first_position'] is None:
            kmers[kmer]['first_position'] = x
        kmers[kmer]['last_position'] = x
    return kmers

def get_clumps(genome: str, k: int, L: int, t: int):
    """
    Given `genome`, find all `k`-mers that appear at least `t`
    times in a window `L` nucleotides long.
    """
    kmers = defaultdict(list)
    clumps = []
    for x in range(0, len(genome) - k + 1):
        pattern = genome[x:x+k]
        kmers[pattern].append(x)
        while kmers[pattern][-1] + k - kmers[pattern][0] > L:
            kmers[pattern].pop(0)
        if len(kmers[pattern]) >= t:
            clumps.append(pattern) if pattern not in clumps else None
    return clumps

def get_clumps_from_file(filestr: str, k: int, L: int, t: int):
    """
    Get `k`-mer clumps in a genome from a file
    """
    genome = import_genome_from_file(filestr)
    return get_clumps(genome, k, L, t)

def copy_clumps_to_clipboard(genome, k, L, t):
    clumps = get_clumps(genome, k, L, t)
    pyperclip.copy(" ".join(clumps))

def copy_clumps_to_clipboard_from_file(filestr, k, L, t):
    clumps = get_clumps_from_file(filestr, k, L, t)
    pyperclip.copy(" ".join(clumps))
