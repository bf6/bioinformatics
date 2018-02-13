import requests


def read_input(url: str, lines: int = None):
    """
    Return `lines` lines from text at `url`
    """
    x = requests.get(url).text
    if not lines:
        return x.splitlines()[1]
    else:
        return x.splitlines()[1:lines+1]

def find_skew(genome: str):
    """
    Return the skew (C - G) at all positions along `genome`
    """
    skew = [0]
    for i, val in enumerate(genome, 1):
        if val == 'G': skew.append(skew[i-1] + 1)
        elif val == 'C': skew.append(skew[i-1] -1)
        else: skew.append(skew[i-1])
    return skew

def find_min_of_skew(skew: list):
    """
    Return minimum value for `skew`
    """
     res = []
     minval = min(skew)
     for i, val in enumerate(skew):
         if val == minval:
             res.append(i)
     return " ".join([str(x) for x in res])

def find_min_and_skew(genome):
    return find_min_of_skew(find_skew(genome))
