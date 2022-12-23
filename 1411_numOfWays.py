class Solution:
    def numOfWays(self, n: int) -> int:
        sameAtEdges = allDifferent = small = big = 6
        if n == 1: return sameAtEdges + allDifferent
        for _ in range(n - 1):
           sameAtEdges = small * 4
           allDifferent = big * 5
           small = sameAtEdges // 2 + allDifferent * 2 // 5
           big = sameAtEdges // 2 + allDifferent * 3 // 5
        return (sameAtEdges + allDifferent) % 1000000007
