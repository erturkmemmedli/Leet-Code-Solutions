class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                dp[i] = dp[i-1] + prices[i] - prices[i-1]
                dp[i-1] = 0
        return sum(dp)

# Alternative solution

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        at i-th stock, at most k transactions, 0/1 at the end means how many stocks left at hand
        k (number of transactions) is infinity here
        T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i]) = max(T[i-1][k][1], T[i-2][k][0] - prices[i])
        since k - 1 = k for k = infinity
        '''
        T_i_k_0 = 0
        T_i_k_1 = -float('inf')
        for price in prices:
            T_i_k_0_old = T_i_k_0
            T_i_k_0 = max(T_i_k_0, T_i_k_1 + price)
            T_i_k_1 = max(T_i_k_1, T_i_k_0_old - price)
        return T_i_k_0
