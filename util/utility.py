import copy

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


class Frequency:
    def __init__(self, individual):
        """Utility class for calculating frequency in an individual"""
        self.d = dict().fromkeys(individual, 1)
        self.ind = copy.copy(individual)
        self.ind.sort()
        self._calFrequency()

    def _calFrequency(self):
        """calculates frequency of each element in an individual"""
        for i in range(1, len(self.ind)):
            if self.ind[i] == self.ind[i - 1]:
                self.d[self.ind[i]] = self.d[self.ind[i]] + 1

    def __getitem__(self, key):
        """returns the occurence of an element in an individual"""
        return self.d[key]

    def anyDuplicates(self):
        """ returns true if there are any duplicates, false otherwise"""
        for e in self.d:
            if self.d[e] >= 2:
                return True
        return False

    def areAllUnique(self):
        """returns true if elements are all unique, false otherwise"""
        return not self.anyDuplicates()

    def teardown(self):
        del self
