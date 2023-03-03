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

# Alternative solution

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.memo = {}
        return self.dp(amount, coins, 0)

    def dp(self, amount, coins, index):
        if amount == 0:
            return 1

        if amount < 0 or index == len(coins):
            return 0

        if (amount, index) in self.memo:
            return self.memo[(amount, index)]

        self.memo[(amount, index)] = self.dp(amount - coins[index], coins, index) + self.dp(amount, coins, index + 1)
        return self.memo[(amount, index)]
