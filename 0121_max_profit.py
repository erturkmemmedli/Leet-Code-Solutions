class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        minimum = 0
        for i in range(1, len(prices)):
            if prices[i] <= prices[minimum]:
                minimum = i
            else:
                dp[i] = prices[i] - prices[minimum]
        return max(dp)
