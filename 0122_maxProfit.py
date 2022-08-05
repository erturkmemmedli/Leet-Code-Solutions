class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                dp[i] = dp[i-1] + prices[i] - prices[i-1]
                dp[i-1] = 0
        return sum(dp)
