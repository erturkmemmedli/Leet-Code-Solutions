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

# Alternative solution

class Solution1:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        at i-th stock, at most k transactions, 0/1 at the end means how many stocks left at hand
        k (number of transactions) is infinity here
        we have additional constraint such as fee
        T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i] - fee)
        T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i]) = max(T[i-1][k][1], T[i-2][k][0] - prices[i])
        since k - 1 = k for k = infinity
        '''
        T_i_k_0 = 0
        T_i_k_1 = -float('inf')
        for price in prices:
            T_i_k_0_old = T_i_k_0
            T_i_k_0 = max(T_i_k_0, T_i_k_1 + price - fee)
            T_i_k_1 = max(T_i_k_1, T_i_k_0_old - price)
        return T_i_k_0
