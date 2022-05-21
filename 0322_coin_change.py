class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') if i else 0 for i in range(amount + 1)]
        for i in range(1, amount + 1):
            minimum = float('inf')
            for c in coins:
                if i - c >= 0:
                    minimum = min(minimum, dp[i - c] + 1)
            dp[i] = minimum
        return dp[-1] if dp[-1] != float('inf') else -1
