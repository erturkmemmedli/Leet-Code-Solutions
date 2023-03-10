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

# Alternative solution

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            if dp[i-1] + prices[i] - prices[i-1] >= 0:
                dp[i] = dp[i-1] + prices[i] - prices[i-1]
            else:
                dp[i] = 0
        return max(dp)

# Alternative solution

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum = prices[0]
        result = 0
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
                maximum = prices[i]
            else:
                maximum = prices[i]
                result = max(result, maximum - minimum)
        return result

# Alternative solution

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        at i-th stock, at most k transactions, 0/1 at the end means how many stocks left at hand
        k (number of transactions) is 1 here
        T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
        T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - prices[i]) = max(T[i-1][1][1], -prices[i])
        T[i-1][0][0] = 0 since k = 1, thus k - 1 = 0
        '''
        T_i_1_0 = 0
        T_i_1_1 = -float('inf')
        for price in prices:
            T_i_1_0 = max(T_i_1_0, T_i_1_1 + price)
            T_i_1_1 = max(T_i_1_1, -price)
        return T_i_1_0
