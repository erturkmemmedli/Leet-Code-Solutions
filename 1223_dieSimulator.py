class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * 7 for _ in range(n + 1)]
        dp[0][6] = 1
        for i in range(1, n + 1):
            temp = 0
            for j in range(6):
                for k in range(i - 1, max(-1, i - 1 - rollMax[j]), -1):
                    dp[i][j] += dp[k][-1] - dp[k][j]
                temp += dp[i][j]
            dp[i][-1] = temp
        return dp[-1][-1] % (10 ** 9 + 7)
