def find_all(string: str, substr: str):
    """
    Return the starting indices of all occurrences of
    `substr` in `string`
    """
    start = 0
    while True:
        start = string.find(substr, start)
        if start == -1: return
        yield start
        start += 1
