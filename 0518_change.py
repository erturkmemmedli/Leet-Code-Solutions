class Solution:
    def change(self, amount: int, coins: list) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        dp[0][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                dp[i][j] = dp[i-1][j]
                if j >= coins[i-1]:                  
                    dp[i][j] += dp[i][j - coins[i-1]]
        return dp[-1][-1]
        
# Alternative solution

class Solution1:
    def change(self, amount: int, coins: list) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(amount + 1):
                if j >= coins[i]:                  
                    dp[j] += dp[j - coins[i]]
        return dp[-1]
