from itertools import pairwise
from heapq import nlargest, nsmallest

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairwised = [a + b for a, b in pairwise(weights)]
        largest = sum(nlargest(k - 1, pairwised))
        smallest = sum(nsmallest(k - 1, pairwised))
        return largest - smallest

# Alternative solution

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        large = []
        small = []

        for i in range(1, len(weights)):
            heappush(small, weights[i] + weights[i - 1])
            heappush(large, - weights[i] - weights[i - 1])

        largest = 0
        smallest = 0
        step_small = k - 1
        step_large = k - 1

        while step_small > 0:
            smallest += heappop(small)
            step_small -= 1
        
        while step_large > 0:
            largest += -heappop(large)
            step_large -= 1

        return largest - smallest
