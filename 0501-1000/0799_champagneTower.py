class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured]
        for _ in range(query_row):
            new_level = [0] * (len(dp) + 1)
            for i in range(len(dp)):
                pour = (dp[i] - 1) / 2
                if pour > 0:
                    new_level[i] += pour
                    new_level[i + 1] += pour
            dp = new_level
        return min(dp[query_glass], 1)
