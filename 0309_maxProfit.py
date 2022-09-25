class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        k (number of transactions) is infinity here
        we have additional constraint such as cooldown
        T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        T[i][k][1] = max(T[i-1][k][1], T[i-2][k-1][0] - prices[i]) = max(T[i-1][k][1], T[i-2][k][0] - prices[i])
        since k - 1 = k for k = infinity
        '''
        T_i_k_0_pre = 0
        T_i_k_0 = 0
        T_i_k_1 = -float('inf')
        for price in prices:
            T_i_k_0_old = T_i_k_0
            T_i_k_0 = max(T_i_k_0, T_i_k_1 + price)
            T_i_k_1 = max(T_i_k_1, T_i_k_0_pre - price)
            T_i_k_0_pre = T_i_k_0_old
        return T_i_k_0
