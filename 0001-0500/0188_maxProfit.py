class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        1. Base cases:
        T[-1][k][0] = 0, T[-1][k][1] = -Infinity
        T[i][0][0] = 0, T[i][0][1] = -Infinity

        2. Recurrence relations:
        T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])

        k is arbitrary. 
        '''
        if k >= len(prices) // 2:
            T_i_k_0 = 0
            T_i_k_1 = -float('inf')
            for price in prices:
                T_i_k_0_old = T_i_k_0
                T_i_k_0 = max(T_i_k_0, T_i_k_1 + price)
                T_i_k_1 = max(T_i_k_1, T_i_k_0_old - price)
            return T_i_k_0
        T_i_k_0 = [0] * (k + 1)
        T_i_k_1 = [-float('inf')] * (k + 1)
        for price in prices:
            for j in range(k, 0, -1):
                T_i_k_0[j] = max(T_i_k_0[j], T_i_k_1[j] + price)
                T_i_k_1[j] = max(T_i_k_1[j], T_i_k_0[j - 1] - price)
        return T_i_k_0[k]
