

"""returns the index[s] of s in lst"""
occurence = lambda s, lst: (i for i, e in enumerate(lst) if e == s)


def allDuplicates(s):
    """
    returns true if all characters in a string are duplicates
    returns False if length of string is 1
    """
    assert len(s) != 1

    for i in range(1):
        for j in range(i + 1, len(s)):
            if s[i] != s[j]:
                return False

    return True