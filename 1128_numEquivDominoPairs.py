from collections import defaultdict
from math import factorial

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        D = defaultdict(int)
        for domino in dominoes:
            if domino[0] <= domino[1]:
                D[str(domino[0]) + str(domino[1])] += 1
            else:
                D[str(domino[1]) + str(domino[0])] += 1
        pairs = 0
        for value in D.values():
            if value >= 2:
                pairs += factorial(value) // (factorial(value-2) * 2)
        return pairs
