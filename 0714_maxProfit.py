class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0
        minimum = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                result += prices[i] - minimum - fee
                minimum = prices[i] - fee
        return result
