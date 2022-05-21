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

# Alternative solution

class Solution1:
    def coinChange(self, coins, amount):
        MinimumCoins = [0] * (amount + 1)
        for i in range(1, amount + 1):
            MinimumCoins[i] = float('inf')
            for j in coins:
                if i >= j:
                    min_value = MinimumCoins[i - j] + 1
                    if min_value < MinimumCoins[i]:
                        MinimumCoins[i] = min_value
        return MinimumCoins[amount] if MinimumCoins[amount] != float('inf') else -1
