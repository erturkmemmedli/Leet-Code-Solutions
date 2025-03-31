from itertools import pairwise
from heapq import nlargest, nsmallest

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairwised = [a + b for a, b in pairwise(weights)]
        largest = sum(nlargest(k - 1, pairwised))
        smallest = sum(nsmallest(k - 1, pairwised))
        return largest - smallest
