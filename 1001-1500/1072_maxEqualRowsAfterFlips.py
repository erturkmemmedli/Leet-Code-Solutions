from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        return max(Counter(tuple(x ^ r[0] for x in r) for r in matrix).values())
