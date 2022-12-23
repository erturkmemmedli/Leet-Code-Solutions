class Solution:
    def numOfWays(self, n: int) -> int:
        sameAtEdges, allDifferent = 24, 30
        if n == 1: return 12
        if n == 2: return sameAtEdges + allDifferent
        for _ in range(n-2):
           small = sameAtEdges // 2 + allDifferent * 2 // 5
           big = sameAtEdges // 2 + allDifferent * 3 // 5
           sameAtEdges = small * 4
           allDifferent = big * 5
        return (sameAtEdges + allDifferent) % 1000000007
