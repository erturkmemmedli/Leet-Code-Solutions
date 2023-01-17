class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        T[i][2][0] = max(T[i-1][2][0], T[i-1][2][1] + prices[i])
        T[i][2][1] = max(T[i-1][2][1], T[i-1][1][0] - prices[i])
        T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
        T[i][1][1] = max(T[i-1][1][1], -prices[i])
        where k = 1 and T[i][0][0] = 0
        """
        T_i_1_0 = 0
        T_i_1_1 = -float('inf')
        T_i_2_0 = 0
        T_i_2_1 = -float('inf')
        for price in prices:
            T_i_2_0 = max(T_i_2_0, T_i_2_1 + price)
            T_i_2_1 = max(T_i_2_1, T_i_1_0 - price)
            T_i_1_0 = max(T_i_1_0, T_i_1_1 + price)
            T_i_1_1 = max(T_i_1_1, -price)
        return T_i_2_0
