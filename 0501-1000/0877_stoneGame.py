class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

# Alternative solution

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for i in range(1, n):
            step = n - i
            for j in range(step):
                dp[j][j+i] = max(piles[j] - dp[j+1][j+i], piles[j+i] - dp[j][j+i-1])
        return dp[0][-1] > 0
