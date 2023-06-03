class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        self.memo = {}
        cuts += [0, n]
        cuts.sort()
        return self.dp(cuts, 0, len(cuts) - 1)

    def dp(self, cuts, left, right):
        if right - left <= 1:
            return 0

        if (left, right) in self.memo:
            return self.memo[(left, right)]

        result = cuts[right] - cuts[left] + min(self.dp(cuts, left, i) + self.dp(cuts, i, right) for i in range(left+1, right))
        self.memo[(left, right)] = result
        return result
